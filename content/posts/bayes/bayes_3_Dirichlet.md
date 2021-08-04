+++
author = "Wang Chaohua"
title = "Bayesian Statistics| Dirichlet Process"
date = "2021-07-19T10:52:59+02:00"

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

+++
<!-- # Bayesian Statistics| Dirichlet Process -->

Dirichlet process Bayesian nonparametrics 中被广泛运用， 通常，它被当成一个默认的 prior on spaces of probability measures.

## 0. Parametric VS Non-parametric

Non-parametric 并不是指没有parameter, 而是指 the parameter space $\mathcal{\Theta}$ is infinite-dimensional. On the other hand， a statistical model is called parametric if its parameter space $\mathcal{\Theta}$ is finite-dimensional.



## 1. Definitions


![dirichlet_definition](/img_bayes_DP/dirichlet_1.PNG)

有了定义，但不代表这样一个东西真的就存在，所以还需要证明它的存在性。DP 可以看成是一个stochastic process, 式子(4.3) 可以是为其 finite-dimensional distributions, 根据 Kolmogorov's extension theorem, 我们可以证明其存在性。

如何理解 dirichlet process prior? 对于一个随机过程 $(X_t:t\in T)$, 我们有两种方式理解，
   1. For a fixed $t$, $X_t:\Omega\to\mathbb{R}$ is a random variable.
   2. For a fixed $\omega\in \Omega$, the mapping $t\mapsto X_t(\omega)$ is called a sample path of $(X_t:t\in T)$.

因此，随机过程 $(X_t:t\in T)$ 可以理解为其sample paths的集合，而这个随机过程也定义了这些sample paths的分布。 对于DP而言，它的一条sample path就是一个 probability measure, 因此DP为这些probability measures 提供了一个 prior $\Pi$.

## 2. Properties

首先介绍一种simulation的方法，叫做 stick-breaking.

![stick_breaking](/img_bayes_DP/dirichlet_2.PNG)

这说明我们可以通过base measure $\alpha$ and scaling parameter $M$ 来模拟DP。

sketch of proof
: step 1: show that $P = \sum_j W_j \delta_{\theta_J}$ is  a random measure. 略
  step 2: show that $P \sim DP(M\bar{\alpha})$. 

  For $j\geq 2$, define $W_{j-1}' = W_j/(1-Y_1), \theta'_j = \theta_{j+1}$, then 
  
  $$P= Y_1 \delta_{\theta_1} + (1-Y_1)\sum_{j\geq 1} W_j'\delta_{\theta'_j}$$.

  Notice that the random measure $P':= \sum_{j\geq 1} W_j'\delta_{\theta'_j}$ has the same structure as $P$, and hence has the same distribution. Thus we have the equation 
  $$P = Y\delta_{\theta} + (1-Y) P.$$
  剩下的工作就是解这个方程，可以证明 $P\sim DP(M\bar{\alpha}）$ 是它的唯一解。
  $\Box$


第二个非常重要的性质叫做tail-free, 它的概念比较复杂 (see Freedman, 1963). 简单来说，它表示了一种独立性。不加证明得给出一个结论：$DP(\alpha)$ is tail-free. 这个性质对于求解它得 posterior十分重要。同样不加证明的给出一个定理，

![tail_free](/img_bayes_DP/dirichlet_3.PNG)
where $N_\epsilon := \\# \\{i: X_i\in A_\epsilon\\}$, i.e. the number of observations falling in $A_\epsilon$.

这个tail-free 的性质非常方面，有了它，我们再求posterior的时候不用关心 $X_i$ 的具体数值，我们仅仅需要 $X_i$ 落在某一集合中的个数.

Theorem (Conjugacy of DP)
: The posterior of DP is again a DP.

![dirichlet_conjugacy](/img_bayes_DP/dirichlet_4.PNG)
where $MN$ indicates the multinomial distribution. And the Multinomial-Dirichlet distribution conjugacy is used in the proof.

这个定理告诉我们，我们仅仅需要我们更新observations 出现的点的概率. Let $\mathbb{P}_n$ denote the empirical distribution of observations, then the posterior of DP can be written as $DP(\alpha + n\mathbb{P}_n)$.


## 3. Consistency
当我们用DP来估计某一probability measure时，我们还关心它的收敛问题，这几乎是所有learning algorithm的核心。 下面我们将证明 the DP prior does work.

Theorem (Consistency of DP)
: Suppose that observations $X_i\sim P_0$ independently.
![dirichlet_consistency](/img_bayes_DP/dirichlet_5.PNG)

sketch of proof
: ![dirichlet_consistency_prof](/img_bayes_DP/dirichlet_6.PNG)

DP的介绍就到此为止了，如果有空可能会再补充点 DP mixture的内容。 从直观上来看，DP 是离散的，所以并不能直接用于估计连续函数。因此下一章介绍可以用于估计连续函数的 Gaussian process.

## References

- [1] Ghosal, S. (2010). The Dirichlet process, related priors and posterior asymptotics
- [2] Ghosal, S., & Van der Vaart, A. (2017). Fundamentals of nonparametric Bayesian inference



