# -*- coding: utf-8 -*-

from learn_polars import api


def test():
    _ = api


if __name__ == "__main__":
    from learn_polars.tests import run_cov_test

    run_cov_test(__file__, "learn_polars.api", preview=False)
