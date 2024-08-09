NDJSON IO
==============================================================================
NDJSON 是 New line delimited JSON 的缩写, 是一种文本格式, 每行是一个 JSON 对象, 这种格式在处理大量数据时非常有用, 因为可以逐行读取, 而不需要一次性读取整个文件. 下面是一个例子:

.. code-block:: javascript

    {"id": 1, "name": "Alice"}
    {"id": 2, "name": "Bob"}
    {"id": 3, "name": "Charlie"}

对 NDJSON 文件的读取我分别测试了用原生 Python 的 json 和用 polars 模块的 read_ndjson / write_ndjson 方法, 结果显示 polars 的速度要快 3-5 倍以上, 数据结构越复杂快的约明显.

下面是我用来测试的脚本:

.. dropdown:: performance_test.py

    .. literalinclude:: ./performance_test.py.py
       :language: python
       :linenos:
