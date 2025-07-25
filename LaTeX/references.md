---
title: 参考文献
---

## BibTeX 和 BibLaTeX

现在不少的教程都是写如何使用 BibTeX 来管理参考文献，但实际上 BibTeX 已经有些过时了，BibLaTeX 是更加现代的方案（当然，这并不意味着 BibTeX 就完全没用了）。BibLaTeX 是对 BibTeX 的改进，提供了更强大的功能和更灵活的配置选项，一般用 `biber` 作为后端处理器进行渲染。

## GB/T 7714-2015

GB/T 7714-2015 是中文文献引用的国家标准。一般用上交制作的 `gb7714-2015` 样式，提供 BibTeX 和 BibLaTeX 两种实现方式，按需选用即可：

- [BibTeX 实现](https://mirrors.sjtug.sjtu.edu.cn/ctan/biblio/bibtex/contrib/gbt7714/gbt7714.pdf)

- [BibLaTeX 实现](https://mirrors.sjtug.sjtu.edu.cn/ctan/macros/latex/contrib/biblatex-contrib/biblatex-gb7714-2015/biblatex-gb7714-2015.pdf)

```latex
\usepackage[backend=biber,style=gb7714-2015]{biblatex}
```
