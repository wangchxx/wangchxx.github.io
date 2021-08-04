+++
author = "Wang Chaohua"
title = "Bayesian Statistics| Pirors and Posteriors"
date = "2021-07-17T10:52:59+02:00"

tags = [
    "markdown",
]
categories = [
    "stat",
    "ml"
]
series = ["bayesian statistics"]
aliases = ["migrate-from-jekyl"]
math = true
draft = true
+++
```
这个系列主要内容是介绍贝叶斯理论，是我之前上课笔记的简单整理。整个体系是建立在测度论基础上的，所以默认读者已经熟悉 measure-theoretical probability 的基本内容了， 如果没有这方面基础，建议任意找本教材查阅。
```

这是第一章，我们的主要任务是定义先验概率(piror)和后验概率(posterior). 在非贝叶斯统计里，我们认为一个统计模型是一个概率分布的集合 $\{ P_\theta: \theta\in \Theta \}$. 然而，贝叶斯统计给与了参数$\theta$一个先验分布，denoted by $\Pi$, 这样分布$P_\theta$就成了 data $X$ given $\vartheta = \theta$ 的条件概率, 从而 $(X,\vartheta)$拥有联合概率
$$ 
   \Pr(X\in A,\vartheta\in B) = \int_B P_\theta(A) d\Pi(\theta) .
$$ (1)
观测到数据之后，我们可以对 prior 进行更新，这被称为posterior, given by 
$$ 
 \Pi(B|x) = \Pr(\vartheta\in B| X =x).
$$


## 1. Definitions
$\mathfrak{X},\mathscr{X}$

