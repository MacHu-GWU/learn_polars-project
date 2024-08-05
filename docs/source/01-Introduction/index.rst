Introduction
==============================================================================


What is Polars
------------------------------------------------------------------------------


Why Polars
------------------------------------------------------------------------------


Polars vs Pandas
------------------------------------------------------------------------------
大部分的用户都是先学了 `Pandas <https://pandas.pydata.org/>`_, 然后被 Polars 出色的性能所吸引过来的. 它和 pandas 虽然 API 很类似, 但是在很多地方有着本质却别, 而就是这些本质区别使得 polars 对于大数据集的处理要高出 pandas 一个甚至数量级. 下面我列出了哪些最关键的区别:

- Apache Arrow: polars 的数据内存基于 apache arrow 而 pandas 基于 numpy, arrow 原生就是高效列存储, 并且对字符串, 也是占据内存的大户, 有着特别的优化, 而且它天生支持并行计算 (多个 CPU 一起干活) 以及 vectorize (用高度优化的 CPU 指令集对大量同类型的数据进行相同的运算) 计算. 这是 polars 在进行 IO 时的性能要远高于 pandas 的核心原因.
- Lazy evaluate: 基本上你对 pandas dataframe 的每一个操作都是即时生效, 而 polars 则是像 Spark 那样大部分操作都是 lazy evaluate, 只有在需要结果的时候才会真正执行. 这样的好处是可以对一系列操作进行优化, 例如合并多个操作到一个执行计划中, 从而减少中间结果的存储和计算. 这是 polars 在对 DataFrame 进行数据分析时的性能要远高于 pandas 的核心原因.

以上两点一个专注于 IO, 一个专注于数据分析, 基本上涵盖了 99% 数据分析以及 ETL 的场景, 使得 polars 在大部分场景下性能都远高于 Pandas.

Ref:

- `Coming from Pandas <https://docs.pola.rs/user-guide/migration/pandas/>`_


Choose a Polars Version
------------------------------------------------------------------------------
Polars 在 2024-07-01 发布了第一个正式版本 1.0.0. 在生产环境中推荐使用 ``polars>=1.0.0,<2.0.0``.

- PyPI release: https://pypi.org/project/polars/#history
- Change Log: https://github.com/pola-rs/polars/releases
    - 1.0.0: https://github.com/pola-rs/polars/releases/tag/py-1.0.0
