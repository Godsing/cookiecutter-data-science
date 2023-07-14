def deprecation_warning():
    print("""

=============================================================================
*** 警告 ***

此项目模板即将转到 v2 版本，届时将需要使用命令 `ccds ...` 而不是 `cookiecutter ...`。
不过 cookiecutter 命令和此版本的模板仍然可用，但需要显式使用 `-c v1` 来选择它。

例如:
    cookiecutter -c v1 https://github.com/Godsing/cookiecutter-data-science
=============================================================================

    """)


deprecation_warning()
