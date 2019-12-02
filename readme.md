## 介绍

使用的是[pelican](https://github.com/getpelican/pelican)搭建的网站

使用的themes是[pelican-bootstrap3](https://github.com/xunta-today/pelican-themes/tree/master/pelican-bootstrap3),有修改过

使用了[tipue_search](https://github.com/xunta-today/pelican-plugins/tree/master/tipue_search)插件, 有修改过

关于网站其他介绍看[程序员找对象聚合平台-xunta.today](https://igaojin.me/2019/11/30/%E7%A8%8B%E5%BA%8F%E5%91%98%E6%89%BE%E5%AF%B9%E8%B1%A1%E8%81%9A%E5%90%88%E5%B9%B3%E5%8F%B0-xunta-today/)

## 如何在本地部署本网站

- `pip install -r requirements.txt`
- `git clone git@github.com:xunta-today/website.git`
- `git clone git@github.com:xunta-today/pelican-themes.git`
- `git clone git@github.com:xunta-today/pelican-plugins.git`

把https://github.com/xunta-today/website/blob/5a4f87892d59a6cfe8a952819f29634e3a43b907/pelicanconf.py#L41 的**PLUGIN_PATHS** 改成你本地pelican-plugins的路径

执行`pelican-themes -vi /Users/gaojin/Documents/GitHub/pelican-themes/pelican-bootstrap3 ` （其中路径改成你本地pelican-themes的）

这样本地就配置好了

## 本地build

`invoke rebuild`

## 本地预览

`invoke serve`

## 更新网站 

`ghp-import output -b gh-pages -p -f -c xunta.today`