# -*- coding: utf-8 -*-

import typing as T
import io
import gzip
import json

import random
import polars as pl

from learn_polars.vendor.timer import DateTimeTimer

T_RECORD = T.Dict[str, T.Any]


# Pure Python
def write_ndjson_v1(records: T.List[T_RECORD]) -> bytes:
    lines = [json.dumps(record) for record in records]
    return gzip.compress("\n".join(lines).encode("utf-8"))


def read_ndjson_v1(b: bytes) -> T.List[T_RECORD]:
    lines = gzip.decompress(b).decode("utf-8").splitlines()
    return [json.loads(line) for line in lines]


# Polars
def write_ndjson_v2(records: T.List[T_RECORD]) -> bytes:
    df = pl.DataFrame(records)
    buffer = io.BytesIO()
    df.write_ndjson(buffer)
    return gzip.compress(buffer.getvalue())


def read_ndjson_v2(b: bytes) -> T.List[T_RECORD]:
    df = pl.read_ndjson(gzip.decompress(b))
    return df.to_dicts()


def test_read_write_performance():
    """
    Conclusion::

        n_records = 1_000_000

        {
            'Write v1': 3.487125,
            'Write v2': 1.944694,
            'Read v1': 1.504748,
            'Read v2': 0.390745
        }

        n_records = 10_000_000
        {
            'Write v1': 37.561264,
            'Write v2': 19.951817,
            'Read v1': 15.761758,
            'Read v2': 5.038208
        }
    """
    n_records = 1_000
    # n_records = 10_000
    # n_records = 100_000
    # n_records = 1_000_000
    # n_records = 10_000_000
    prefix = "s3://mybucket/data"
    records = [
        {
            "uri": f"{prefix}/{ith}.parquet",
            "size": random.randint(1000 * 1000, 10 * 1000 * 1000),
        }
        for ith in range(1, 1 + n_records)
    ]

    display = True
    # display = False

    result = {}

    with DateTimeTimer("Write v1", display=display) as timer:
        b = write_ndjson_v1(records)
    result["Write v1"] = timer.elapsed
    size1 = len(b)

    with DateTimeTimer("Write v2", display=display) as timer:
        b = write_ndjson_v2(records)
    result["Write v2"] = timer.elapsed
    size2 = len(b)

    with DateTimeTimer("Read v1", display=display) as timer:
        records1 = read_ndjson_v1(b)
    result["Read v1"] = timer.elapsed
    assert len(records1) == n_records
    if n_records <= 1000:
        assert records1 == records

    with DateTimeTimer("Read v2", display=display) as timer:
        records2 = read_ndjson_v2(b)
    result["Read v2"] = timer.elapsed
    assert len(records2) == n_records
    if n_records <= 1000:
        assert records2 == records

    if display:
        print(result)


test_read_write_performance()
