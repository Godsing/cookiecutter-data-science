# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## 项目结构

```
├── README.md           <- 项目开发者使用的顶级 README 文件
├── data
│   ├── raw             <- 原始、不可变的数据转储
│   ├── processed       <- 最终用于建模的规范化数据集
│   ├── interim         <- 经过转换的中间数据
│   └── external        <- 第三方数据源
│
├── notebooks           <- Jupyter 笔记本。命名约定为数字(用于排序)+描述，例如:
│                          `1.0-initial-data-exploration.ipynb`
│
├── src                 <- 源代码。可打包的代码应放在 {{ cookiecutter.package_name }} 中，其余直接放在 src 下
|   └── {{ cookiecutter.package_name }}
│       │
│       ├── __init__.py <- 使 src 目录成为一个 Python 模块
│       │
│       ├── data        <- 下载或处理数据的脚本
│       │
│       ├── modeling    <- 模型结构(核心代码，训练、评估、推理时均需用到)
│       │   ├── modeling.py
│       │   └── config.json
│       │
│       ├── train       <- 训练模型的脚本，加载训练集并生成模型权重、记录训练过程
│       │
│       ├── eval        <- 评估模型的脚本，加载验证集并生成评估报告
│       │
│       └── infer       <- 推理(预测)脚本，可提供 RESTful API 或 CLI 或 Web UI
│
├── weights             <- 训练得到的模型权重，及其相关的必要配置信息
│
├── reports             <- 评估结果等结论性的内容，以图、表等形式呈现
│
├── logs                <- 推理接口的日志文件
│
├── tmp                 <- 临时文件(例如：训练时的 TF events 文件、评估时的中间文件)
│
├── requirements.txt    <- 环境要求文件。可通过 `pipreqs . --encoding=utf8 --force`
│                          或 `pip freeze > requirements.txt` 生成
│
├── setup.py            <- 使项目可通过 `pip install -e .` 安装，以便 `import src`.
├── Makefile            <- 包含诸如 `make data` 或 `make train` 等命令的 Makefile
└── LICENSE
```

> 本项目基于 [cookiecutter data science](https://github.com/Godsing/cookiecutter-data-science) 项目模板创建。
