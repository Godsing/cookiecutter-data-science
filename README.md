# Cookiecutter 数据科学项目模板

一个逻辑清晰、标准化但依然灵活的项目结构，用于数据科学研发。
_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

> Fork from: [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science)
> 本仓库在原始仓库的基础上做了一些修改，以适应自己的工作习惯。如果您觉得还不错，欢迎使用！

## 用法

### 使用该模板的要求

 - Python 2.7 or 3.5+
 - [Cookiecutter Python 包](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: 可以使用 pip by 或 conda 安装（具体取决于您管理 Python 包的方式）：

    ```bash
    pip install cookiecutter
    ```

    或者

    ```bash
    conda config --add channels conda-forge
    conda install cookiecutter
    ```

### 使用该模板创建新项目

```bash
cookiecutter -c wgx https://github.com/Godsing/cookiecutter-data-science
```

> 此项目模板**即将**转到 v2 版本，届时将需要使用命令 `ccds ...` 而不是 `cookiecutter ...`。
> 不过 cookiecutter 命令和此版本的模板仍然可用，但需要显式使用 `-c wgx` 来选择它。

以上命令创建得到的新项目，目录结构如下：

```
├── README.md          <- 项目开发者使用的顶级 README 文件
├── data
│   ├── raw            <- 原始、不可变的数据转储
│   ├── processed      <- 最终用于建模的规范化数据集
│   ├── interim        <- 经过转换的中间数据
│   └── external       <- 第三方数据源
│
├── notebooks          <- Jupyter 笔记本。命名约定为数字(用于排序)+描述，例如:
│                         `1.0-initial-data-exploration.ipynb`
│
├── src                <- 用于此项目的源代码
│   ├── __init__.py    <- 使 src 目录成为一个 Python 模块
│   │
│   ├── data           <- 下载或处理数据的脚本
│   │
│   ├── modeling       <- 模型结构(核心代码，训练、评估、推理时均需用到)
│   │   ├── modeling.py
│   │   └── config.json
│   │
│   ├── train          <- 训练模型的脚本，加载训练集并生成模型权重、记录训练过程
│   │
│   ├── eval           <- 评估模型的脚本，加载验证集并生成评估报告
│   │
│   └── infer          <- 推理(预测)脚本，可提供 RESTful API 或 CLI 或 Web UI
│
├── weights            <- 训练得到的模型权重，及其相关的必要配置信息
│
├── reports            <- 评估结果等结论性的内容，以图、表等形式呈现
│
├── logs               <- 推理接口的日志文件
│
├── tmp                <- 临时文件(例如：训练时的 TF events 文件、评估时的中间文件)
│
├── requirements.txt   <- 环境要求文件。可通过 `pipreqs . --encoding=utf8 --force`
│                         或 `pip freeze > requirements.txt` 生成
│
├── setup.py           <- 使项目可通过 `pip install -e .` 安装，以便 `import src`.
├── Makefile           <- 包含诸如 `make data` 或 `make train` 等命令的 Makefile
└── LICENSE
```

## 参与贡献

非常欢迎贡献你的代码，以继续优化该模板！

如果不知道如何操作，请参考[这里](https://github.com/Godsing/cookiecutter-data-science/blob/wgx/docs/docs/index.md#参与贡献)。

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行测试

```bash
py.test tests
```
