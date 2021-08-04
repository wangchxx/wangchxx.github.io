+++
author = "Wang Chaohua"
title = "Bayesian Statistics| Gaussian Process Priors (1)"
date = "2021-07-21T10:52:59+02:00"

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
<!-- # Bayesian Statistics| Gaussian Process Priors (1) -->

在前面章节中已经介绍过 Dirichlet process prior, 其主要用作 measure space 的先验。 这章要介绍的 Gaussian process (GP) 可用作 function space 的先验。举个例子，假如我们有样本 $(X_i,Y_i),i\leq n.$ 我们要研究 $X_i$ 和 $Y_i$ 之间的关系。 一个常见的模型是
$$Y = \beta X  + \epsilon.$$

我们要做的是估计参数 $\beta$. 这是一个有限维的模型，我们其实可以更广义地写成,
$$Y_i = f(X_i) + \epsilon_i,$$

where $f$ is function. 我们要做的就是估计这个函数 $f$, 这是一个无限维的模型。Gaussian process regression 是给与函数 $f$一个先验分布 $\Pi$, 而这个先验就是用的Gaussian process.


## 1. Gaussian Process

GP 的一个简单定义是通过其 finite-dimensional distributions (FDDs) 实现的。

Definition (Gaussian process)
: ![GP_def_1](/img_bayes_GP/GP_1.PNG)

the map $t\mapsto W_t(\omega)$ is called the sample path of of $W$. Sample paths are functions from $T$ to $\mathbb{R}$, so the process can be viewed as a map $W:\Omega \to \mathbb{B}$, where $\mathbb{B}$ is a function space, e.g. the space of continuous functions on $T$.

这个定义的问题是，FDDs 并不能完全决定sample paths的性质。一个解决办法是找到 a version $\tilde{W}$  of $W$ s.t. the sample paths $\tilde{W}$ possess the desired properties. For instance, if we need a space of continuous functions on $T$, we may apply the following theorem  
![GP_continuous](/img_bayes_GP/GP_2.PNG)


GP 的另一个定义。Let $\mathbb{B}^*$ denote the dual space of a Banach space $\mathbb{B}$.

Definition (Gaussian random element)
: ![GP_def_2](/img_bayes_GP/GP_3.PNG)

这两个定义有什么关系呢？由第二个定义我们总是能构成一个 Gaussian stochastic process by $(b^\*(W):b^\*\in T)$, for any subset $T\subset \mathbb{B}^*$. 另外，if the sample paths $t\mapsto W_t$ of the stochastic process $W = (W_t:t\in T)$ belong to a Banach process $\mathbb{B}$ of functions $z:T\to \mathbb{R}$, then under some conditions the process will be a Gaussian random element. 


## 2. Reproducing Kernel Hilbert Space

每个 GP都天然地自带一个 Hilbert space, determined by its covariance function. For a GP $W = (W_t: t\in T)$, let $\overline{lin}(W)$ be the closure of the set of all linear combinations $\sum_i \alpha_i W_{t_i}$ in the $L^2$-space of square-integrable variables. Then the space $\overline{lin}(W)$ is a Hilbert space, with inner product $< f,g> = E f\bar{g}$,called the first order chaos of $W$.

Definition (RKHS, 1)
: ![RKHS_1](/img_bayes_GP/GP_4.PNG)

可以验证 $\mathbb{H}$ 的确是一个Hilbert space.

Lemma (Properties of RKHS)
: ![RKHS_1_pty](/img_bayes_GP/GP_5.PNG)

A Gaussian random element in a separable Banach space also comes with a RKHS. First we define the map $S:\mathbb{B}^*\to \mathbb{B}$ by

$$Sb^* = E[b^*(W)W],$$

where the right side is the Pettis integral.

Definition (RKHS, 2)
: ![RKHS_2](/img_bayes_GP/GP_6.PNG)

这两个定义之间的联系

$$r(s,t) = E W_s W_t = E[\pi_s(W) \pi_t(W)] = \langle S\pi_s, S\pi_t \rangle_{\mathbb H},$$
where $\pi_t: b\mapsto b(t)$ are elements in $\mathbb B^*$.

## 3. Small Ball Probability

As a Bayesian, we are always interested in the posterior consistency. Here we give some lemmas which are useful to study the posterior consistency of Gaussian process priors.

Lemma (Borell's)
: Let $\Phi$ be the CDF of the standard normal.
![Borell's](/img_bayes_GP/GP_7.PNG)

The additional small ball $\epsilon\mathbb B_1$ creates an $\epsilon$-cushion around $M\mathbb{B}_1$. This lemma suggests that if we want to use GP prior to estimate a function, we must ensure that the true function is contained in the closure of RKHS.


Lemma (Decentered)
: ![Decentered](/img_bayes_GP/GP_8.PNG)


Lemma (Small ball)
: ![small ball](/img_bayes_GP/GP_9.PNG)


## 4. Posterior Contraction

在讨论 posterior contraction of GP prior之前，我们需要先介绍一些infinite-dimensional Bayes 的一些理论，这将是很长的一部分内容，所以我将用专门的一章来介绍，之后，再回过头来讨论DP prior 的情况。


## References

- [1] van der Vaart, A. W., & van Zanten, J. H. (2008). Reproducing kernel Hilbert spaces of Gaussian priors.

- [2] Ghosal, S., & Van der Vaart, A. (2017). Fundamentals of nonparametric Bayesian inference.