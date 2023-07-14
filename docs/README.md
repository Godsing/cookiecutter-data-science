## 生成本项目文档

安装所需的包：

```
pip install -r requirements.txt
```

进入 docs 文件夹：

```
cd docs
```

使用[mkdocs](http://www.mkdocs.org/)结构来更新文档。本地测试：

```
mkdocs serve
```

一旦文档看起来不错，就可以使用以下命令发布到`gh-pages`分支：

```
mkdocs gh-deploy --clean
```

**注意**：切勿手动编辑生成的站点，因为使用`gh-deploy`会“吹走”`gh-pages`分支，并且您将丢失所做的编辑。