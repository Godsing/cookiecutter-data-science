# 千篇一律的数据科学

*一个逻辑合理、标准化但灵活的项目结构，用于进行和共享数据科学工作。*

## 为什么使用这个项目结构？

> 我们并不是在谈论废除缩进美学或迂腐的格式标准——最终，数据科学代码质量关乎正确性和可重复性。

当我们考虑数据分析时，我们通常只考虑生成的报告、见解或可视化结果。虽然这些最终产品通常是主要事件，但人们很容易将注意力集中在使产品*看起来漂亮*而忽略*生成它们的代码的质量*。由于这些最终产品是以编程方式创建的，因此**代码质量仍然很重要**！我们并不是在谈论废除缩进美学或迂腐的格式标准——最终，数据科学代码质量关乎正确性和可重复性。

众所周知，好的分析往往是非常漫无目的和偶然探索的结果。尝试性实验和可能行不通的快速测试方法都是获得好东西的过程的一部分，并且没有灵丹妙药可以将数据探索变成简单的线性过程。

话虽这么说，一旦开始，它就不是一个需要仔细思考代码结构或项目布局的过程，因此最好从一个干净的逻辑结构开始，并始终坚持下去。我们认为使用像这样的相当标准化的设置是一个相当大的胜利。原因如下：

### 其他人会感谢你的

> 在创建一个新的 Rails 项目之前，没有人会坐下来思考他们想要将自己的观点放在哪里；他们只是`rails new`像其他人一样跑去获得一个标准的项目框架。

定义明确的标准项目结构意味着新手无需深入研究大量文档即可开始理解分析。这也意味着他们不一定要阅读 100% 的代码才能知道在哪里寻找非常具体的东西。

组织良好的代码往往是自记录的，因为组织本身为您的代码提供了上下文，而无需太多开销。人们会因此感谢你，因为他们可以：

- 在此分析方面与您更轻松地协作
- 从您对流程和领域的分析中了解
- 对分析得出的结论充满信心

在任何主要的 Web 开发框架（如 Django 或 Ruby on Rails）中都可以找到一个很好的例子。在创建一个新的 Rails 项目之前，没有人会坐下来思考他们想要将自己的观点放在哪里；他们只是`rails new`像其他人一样跑去获得一个标准的项目框架。因为默认的项目结构*在大多数项目中都是**合乎逻辑*且合理标准的，所以对于从未见过特定项目的人来说，更容易弄清楚他们在哪里可以找到各种活动部件。

另一个很好的例子是类 Unix 系统的[文件系统层次结构标准。](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)该`/etc`目录和文件夹一样都有一个非常具体的目的，`/tmp`每个人（或多或少）都同意遵守该社会契约。这意味着 Red Hat 用户和 Ubuntu 用户都大致知道在哪里查找某些类型的文件，即使在使用彼此的系统或任何其他符合标准的系统时也是如此！

理想情况下，当同事打开你的数据科学项目时应该是这样的。

### 你会感谢你的

是否曾经尝试过重现几个月前甚至几年前所做的分析？您可能已经编写了代码，但现在不可能判断是否应该使用`make_figures.py.old`, `make_figures_working.py`或`new_make_figures01.py`来完成工作。以下是我们学会带着存在主义恐惧感提出的一些问题：

- 我们是否应该在开始之前将 X 列加入到数据中，还是来自其中一台笔记本？
- 想一想，在运行绘图代码之前我们必须先运行哪个笔记本：是“处理数据”还是“清理数据”？
- 地理图的 shapefile 从哪里下载？
- 等等(无穷无尽...)。

这些类型的问题是令人痛苦的，并且是项目杂乱无章的症状。良好的项目结构鼓励更容易返回旧工作的实践，例如关注点分离、将分析抽象为 DAG[以及](https://en.wikipedia.org/wiki/Directed_acyclic_graph)版本控制等工程最佳实践。

### 这里没有任何约束力

> “愚蠢的一致性是头脑狭隘的怪物”——拉尔夫·沃尔多·爱默生（和[PEP 8！](https://www.python.org/dev/peps/pep-0008/#a-foolish-consistency-is-the-hobgoblin-of-little-minds)）

不同意几个默认文件夹名称？正在从事一个有点不标准且不完全适合当前结构的项目？更喜欢使用与（少数）默认包之一不同的包？

**大胆试试吧！** 这是一种轻量级结构，旨在成为许多项目的良好*起点。* 或者，正如 PEP 8 所说：

> 项目内的一致性更为重要。一个模块或功能内的一致性是最重要的。...然而，知道何时要不一致——有时风格指南的建议并不适用。如有疑问，请运用您的最佳判断。查看其他示例并决定哪个看起来最好。请随时询问！

## 入门

考虑到这一点，我们为 Python 项目创建了一个数据科学 cookiecutter 模板。您的分析不必使用 Python，但模板确实提供了一些您想要删除的 Python 样板文件（`src`例如在文件夹中，以及 中的 Sphinx 文档框架`docs`）。

### 要求

- Python 2.7 或 3.5
- [cookiecutter Python 包](http://cookiecutter.readthedocs.org/en/latest/installation.html)>= 1.4.0：`pip install cookiecutter`

### 开始一个新项目

启动新项目就像在命令行运行此命令一样简单。无需先创建目录，cookiecutter 会为您完成。

```bash
cookiecutter https://github.com/Godsing/cookiecutter-data-science
```

## 目录结构

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

## 意见

项目结构中隐含了一些观点，这些观点源自我们在数据科学项目合作时对哪些有效、哪些无效的经验。有些观点是关于工作流程的，有些观点是关于让生活更轻松的工具的。以下是该项目所基于的一些信念 - 如果您有任何想法，请[贡献或分享](https://github.com/Godsing/cookiecutter-data-science#contributing)。

### 数据是不可变的

切勿编辑原始数据，尤其不要手动编辑，尤其不要在 Excel 中编辑。不要覆盖您的原始数据。不要保存原始数据的多个版本。将数据（及其格式）视为不可变。您编写的代码应该通过管道式的处理，将原始数据流转至最终数据。您不必每次想要创建新图形时都运行所有步骤（请参阅[Analysis is a DAG](https://github.com/Godsing/cookiecutter-data-science#analysis-is-a-dag)），但任何人都应该能够仅使用`src`中的代码和`data/raw`中的数据来复现最终结果。

此外，如果数据是不可变的，则它不需要像代码那样进行源代码控制。因此，***默认情况下，数据文件夹包含在`.gitignore`文件中。*** 如果您有少量很少更改的数据，您可能希望将这些数据包含在存储库中。Github 目前会在文件超过 50MB 时发出警告，并拒绝超过 100MB 的文件。用于存储/同步大数据的其他一些选项包括（例如）：带有同步工具的[AWS S3](https://aws.amazon.com/s3/)、[Git Large File Storage](https://git-lfs.github.com/)、[Git Annex](https://git-annex.branchable.com/)和[dat](http://dat-data.com/)。

> 本项目不含 AWS S3 上传下载工具，如果需要，可参考[原始项目](https://github.com/drivendata/cookiecutter-data-science/blob/master/docs/docs/index.md#:~:text=Currently%20by%20default)。

### 笔记本用于探索和交流

[Jupyter Notebook](http://jupyter.org/)、[Beaker Notebook](http://beakernotebook.com/)、[Zeppelin](http://zeppelin-project.org/)和其他文学编程工具等 Notebook 软件包对于探索性数据分析非常有效。然而，这些工具对于重现分析的效果可能较差。我们在工作中使用笔记本的时候，经常会对`notebooks`文件夹进行细分。例如，`notebooks/exploratory`包含初步探索，而`notebooks/reports`更精致的工作可以作为 html 导出到`reports`目录。

由于笔记本对于源代码控制来说是具有挑战性的对象（例如，人类通常无法读取差异`json`，并且合并几乎不可能），因此我们建议不要在 Jupyter 笔记本上直接与其他人协作。为了有效地使用笔记本，我们建议采取两个步骤：

1. 遵循显示所有者和分析完成顺序的命名约定。我们使用格式`<step>-<ghuser>-<description>.ipynb`（例如，`0.3-bull-visualize-distributions.ipynb`）。
2. 重构好的部分。不要编写代码在多个笔记本中执行相同的任务。如果是数据预处理任务，则将其放入管道中`src/data/make_dataset.py`并从中加载数据`data/interim`。如果它是有用的实用程序代码，请将其重构为`src`.

现在默认情况下我们将项目转换为 Python 包（请参阅`setup.py`文件）。您可以导入代码并在具有如下单元格的笔记本中使用它：

```python
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```

### 分析是有向无环图（[DAG](https://en.wikipedia.org/wiki/Directed_acyclic_graph)）

通常，在分析（指数据处理）中，您需要长时间运行的步骤来预处理数据或训练模型。如果这些步骤已经运行（并且您已将输出存储在目录等位置`data/interim`），您不想每次都等待重新运行它们。我们更喜欢[`make`](https://www.gnu.org/software/make/)管理相互依赖的步骤，尤其是长时间运行的步骤。Make 是基于 Unix 的平台上的常用工具（并且[可用于 Windows](https://github.com/Godsing/cookiecutter-data-science/blob/wgx/docs/docs)）。遵循[`make`文档](https://www.gnu.org/software/make/)、[Makefile 约定](https://www.gnu.org/prep/standards/html_node/Makefile-Conventions.html#Makefile-Conventions)和[可移植性指南](http://www.gnu.org/savannah-checkouts/gnu/autoconf/manual/autoconf-2.69/html_node/Portable-Make.html#Portable-Make)将有助于确保您的 Makefile 跨系统有效工作。下面[是](https://web.archive.org/web/20150206054212/http://www.bioinformaticszen.com/post/decomplected-workflows-makefiles/)[一些](http://zmjones.com/make/) 入门[示例](http://blog.kaggle.com/2012/10/15/make-for-data-scientists/)。人们使用许多数据`make`作为他们选择的工具，包括[Mike Bostock](https://bost.ocks.org/mike/make/)。

还有其他用 Python 而不是 DSL 编写的 DAG 管理工具（例如[Paver](http://paver.github.io/paver/#)、[Luigi](http://luigi.readthedocs.org/en/stable/index.html)、[Airflow](https://airflow.apache.org/index.html)、[Snakemake](https://snakemake.readthedocs.io/en/stable/)、[Ruffus](http://www.ruffus.org.uk/)或[Joblib](https://pythonhosted.org/joblib/memory.html)）。如果它们更适合您的分析，请随意使用它们。

### 从环境开始构建

重现分析的第一步始终是重现运行分析的计算环境。您需要相同的工具、相同的库和相同的版本，以使所有内容都能很好地协同工作。

一种有效的方法是使用[virtualenv](https://virtualenv.pypa.io/en/latest/)（我们建议使用[virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/)来管理 virtualenv）。通过在存储库中列出您的所有需求（我们包含一个`requirements.txt`文件），您可以轻松跟踪重新创建分析所需的包。这是一个很好的工作流程：

1. `mkvirtualenv`创建新项目时运行
2. `pip install`您的分析所需的软件包
3. 运行`pip freeze > requirements.txt`以固定用于重新创建分析的确切包版本
4. 如果您发现需要安装另一个软件包，请`pip freeze > requirements.txt`再次运行并将更改提交到版本控制。

如果您对重新创建环境有更复杂的要求，请考虑基于虚拟机的方法，例如[Docker](https://www.docker.com/)或[Vagrant](https://www.vagrantup.com/)。这两个工具都使用基于文本的格式（分别是 Dockerfile 和 Vagrantfile），您可以轻松添加到源代码管理中，以描述如何根据您的需求创建虚拟机。

### 将秘密和配置置于版本控制之外

您*确实*不想在 Github 上泄露您的 AWS 密钥或 Postgres 用户名和密码。说得够多了——关于这一点，请参阅[十二要素应用程序](http://12factor.net/config)原则。这是执行此操作的一种方法：

#### 将您的秘密和配置变量存储在特殊文件中

`.env`在项目根文件夹中创建一个文件。感谢`.gitignore`，这个文件永远不应该被提交到版本控制存储库中。这是一个例子：

```nohighlight
# example .env file
DATABASE_URL=postgres://username:password@localhost:5432/dbname
AWS_ACCESS_KEY=myaccesskey
AWS_SECRET_ACCESS_KEY=mysecretkey
OTHER_VARIABLE=something
```



#### 使用包自动加载这些变量。

如果您查看 中的存根脚本，它使用一个名为[python-dotenv](https://github.com/theskumar/python-dotenv)`src/data/make_dataset.py`的包将该文件中的所有条目加载为环境变量，以便可以使用. 以下是改编自文档的示例片段：`os.environ.get``python-dotenv`

```
# src/data/dotenv_example.py
import os
from dotenv import load_dotenv, find_dotenv

# find .env automagically by walking up directories until it's found
dotenv_path = find_dotenv()

# load up the entries as environment variables
load_dotenv(dotenv_path)

database_url = os.environ.get("DATABASE_URL")
other_variable = os.environ.get("OTHER_VARIABLE")
```



#### AWS CLI 配置

使用 Amazon S3 存储数据时，管理 AWS 访问的一个简单方法是将访问密钥设置为环境变量。但是，在单台计算机上管理多组密钥（例如，在处理多个项目时），最好使用[凭证文件](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html)，通常位于`~/.aws/credentials`. 典型的文件可能如下所示：

```
[default]
aws_access_key_id=myaccesskey
aws_secret_access_key=mysecretkey

[another_project]
aws_access_key_id=myprojectaccesskey
aws_secret_access_key=myprojectsecretkey
```



您可以在初始化项目时添加配置文件名称；假设未设置适用的环境变量，则默认情况下将使用配置文件凭据。

### 更改默认文件夹结构时要保守

为了使这种结构广泛适用于许多不同类型的项目，我们认为最好的方法是自由地更改*你的*项目周围的文件夹，但在更改*所有*项目的默认结构时尽量保守。

我们专门针对建议添加、删除、重命名或移动文件夹的问题创建了文件夹布局标签。更一般地说，我们还为在实施之前应进行仔细讨论和广泛支持的问题创建了需求讨论标签。

## 贡献

Cookiecutter 数据科学项目固执己见，但不怕犯错。最佳实践不断变化，工具不断发展，经验教训不断汲取。**该项目的目标是让分析的启动、构建和共享变得更加容易。** 鼓励[拉取请求](https://github.com/drivendata/cookiecutter-data-science/pulls)和[提交问题。](https://github.com/drivendata/cookiecutter-data-science/issues)我们很想听听什么对您有用，什么不适合您。

如果您使用 Cookiecutter 数据科学项目，请链接回此页面或[给我们留言](https://twitter.com/drivendataorg)并[让我们知道](mailto:info@drivendata.org)！

## 相关项目和参考文献的链接

R 研究社区更多地讨论了项目结构和可重复性。如果您使用 R 工作，这里有一些项目和博客文章可能会对您有所帮助。

- [项目模板](http://projecttemplate.net/index.html)- R 数据分析模板
- Nice R Code 上的“[设计项目”](http://nicercode.github.io/blog/2013-04-05-projects/)
- Carlboettiger.info 上的“[我的研究流程](http://www.carlboettiger.info/2012/05/06/research-workflow.html)”
- PLOS 计算生物学中的“[组织计算生物学项目的快速指南”](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)

最后，非常感谢[Cookiecutter](https://cookiecutter.readthedocs.org/en/latest/)项目 ( [github](https://github.com/audreyr/cookiecutter) )，它帮助我们花更少的时间思考和编写样板文件，而将更多的时间花在完成工作上。