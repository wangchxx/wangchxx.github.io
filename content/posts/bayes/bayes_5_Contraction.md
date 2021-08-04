+++
author = "Wang Chaohua"
title = "Bayesian Statistics| Posterior Consistency and Contraction"
date = "2021-07-20T10:52:59+02:00"

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
<!-- # Bayesian Statistics| Posterior Consistency and Contraction -->

这一章在理论上讨论non-parametric Bayes 是否真的wrok. 换句话讲，就是posterior是否真的收敛到所谓的 "true" parameter $\theta_0$. Contraction 是比 Consistency 更丰富的一种概念，它还涉及到收敛的速率。

Dirichlet process priors and Gaussian process priors 都是常见的 non-parametric Bayes 方法，还有它们的五花八门的变种，如果 case by case 地讨论他们的收敛问题，就太过于麻烦，因此本章讨论一些general thoery， 对于具体地模型，只需要具体地运用这些理论即可。


## 1. Consistency 

Definition (Posterior consistency)
: ![consistency_def](/img_bayes_Rates/Consistency_1.PNG)


Theorem (Doob's consistency)
: ![consistency_thm](/img_bayes_Rates/Consistency_2.PNG)


Doob's consistency 看起来非常漂亮，对于模型几乎没有任何假设，给定一个prior $\Pi$, its posterior is almost always consistent. 但问题在于我们不清楚这个让结论不成立的 $\Pi-$null set 在哪里。有可能这个 null set 非常大。

所以我们应该对于 prior 给出一定的限制，确保我们的目标 $\theta$ 不在 null set 里。下面给出一种叫做 Kullback-Leibler property 的限制。

Definition (KL property)
: ![kl_p_def](/img_bayes_Rates/Consistency_3.PNG)

这个性质确保 prior assigns positive probability to any KL neighbourhood of the density $p_0:=p_{\theta_0}$ determined by parameter $\theta_0$. 有了这个性质，我们就可以确保 posterior is consistent at $\theta_0$. 下面不加证明地给出一个定理，以后有时间可以拿一章单独讲讲证明，

Theorem (Schwartz's)
: ![consistency_schwartz](/img_bayes_Rates/Consistency_4.PNG)

这个定理有两个条件，第一个是KL property， 第二个是 tests. $P_0^n\theta_n$ 可以理解为假设检验里的 type I error, and $P_\theta^n (1-\theta_n)$ can be viewed as the type II error. 这个假设其实很强，有了这样的 tests，我们即使不用 Bayes，用其他任何统计方法都可以把 $\theta$ 找出来。

下面我们对这个条件进行放松，我们不需要对于每个 complement $\mathcal{U}^\complement$ 都存在 tests, 我们可以允许在一个非常小的集合（with small prior probability）上 tests 不存在。


Theorem (Schwartz's extension)
: ![consistency_schwartz](/img_bayes_Rates/Consistency_5.PNG)

Sketch of proof
: 我们需要证明 for any neighbourhood $\mathcal{U}$ of $p_0$, we have $\Pi_n(\mathcal{U}^\complement|X^{(n)})\to 0$ a.s.. 

  step 1: show that $\Pi_n(\mathcal{U}^\complement\cap \mathcal{P}|X^{(n)})\to 0$ a.s. 

  step 2: show that $\Pi_n( \mathcal{P}^\complement|X^{(n)})\to 0$ a.s. 


## 2. Tests

前面已经提到,对于 posterior consistency, 我们需要两个条件： KL property and tests。 第一个非常容易验证，the existence of tests 却没有这么直观. 因此我们用这一节讨论一下 the existence of tests.


Theorem (Convexity and tests)
: ![tests_convex_H](/img_bayes_Rates/Consistency_6.PNG)

这个定理说明，当 the set of alternative hypotheses $\mathcal{Q}$ is convex and separated from the "true" parameter $P$ (in terms of Hellinger distance), desired tests exist.

上面这个定理将 alternatives 限制在了 convex sets， 但在实际中，convexity 并不一定能满足， 所以我们将这个条件进行放松，思路是，即使 $\mathcal{Q}$ 并不是convex的，但如果它能被多个 convex 的集合给覆盖了, 我们仍然能找到合适的 tests. 这种思路叫做 conving number 也叫 entropy.

Theorem (Entropy)
: ![tests_entropy](/img_bayes_Rates/Consistency_7.PNG)



到目前为止，结合 Schwartz's extension and the existence of entropy under entropy, we can give a more general consistency results.

Theorem (Posterior consistency under entropy)
: ![consistency_entropy](/img_bayes_Rates/Consistency_8.PNG)


这是一个非常general 的理论，它允许我们将所有的 posterior consistency 问题转化为 covering number 的问题。

## 3. Posterior Contraction

Contraction 是比consistency 更精确的概念，它对 $\epsilon$ 的大小进行了量化，衡量了 posterior 收敛的速度。

Definition (Posterior contraction)
: ![contraction_def](/img_bayes_Rates/Contraction_1.PNG)


Theorrem (Posterior contraction)
: ![contraction_thm](/img_bayes_Rates/Contraction_2.PNG)

Sketch of proof
: 通过 条件 （5.7）我们限制了 covering number, 所以由 proposition 5.15 我们可以找到 合适 tests, 然后通过 bounded type I and type II errors 来限制 posterior.



Ok, 到目前为止我们得到了非常强大的理论，无论对于 consistency 还是 contraction, 我们都将他们转化为了 covering number or entropy 的问题。 对于一个具体的 non-parametric Bayes 问题，我们需要的仅仅是研究相应的 covering number. 

之后，会在新的一章中讨论一些具体的例子， 本章就到此为止了。


## References

- [1] Van der Vaart, A. W. (2000). Asymptotic statistics.
- [2] Ghosal, S., & Van der Vaart, A. (2017). Fundamentals of nonparametric Bayesian inference