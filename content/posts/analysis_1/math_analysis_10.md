+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 10 Numerical Series"
date = "2021-04-10T10:52:59+02:00"

tags = [
    "markdown",
]
categories = [
    "analysis"
]
series = ["math analysis"]
aliases = ["migrate-from-jekyl"]
math = true

+++


## 1. Convergence

Definition 1 (Series)
: Given a sequence $\{a_n\}$, we define a sequence $\{s_n\}$ by 
$$ 
 s_n = \sum_{i=1}^n a_i.
$$
We call $\sum_{i=1}^\infty a_i$ an `infinite series` or just a `series`. The numbers $s_n$ are called the `partial sums` of the series.

Definition 2 (Convergence of series)
: If the sequence $\{s_n\}$ converges to $s$, we say that the series converges, and write $\sum_{n=1}^\infty a_n = s$. If $\{s_n\}$ diverges, the series is said to be diverge.


Theorem 3 (Cauchy criterion)
: $\sum a_n$ converges iff for any $\epsilon>0$, there exists an integer $N$ s.t.
$$ 
 |\sum_{k=n}^m a_k|< \epsilon
$$
if $m\geq n\geq N$.

In other words, if $\sum a_n$ converges, then $\lim_{n\to\infty} a_n = 0$.


Theorem 4
: A series of nonnegative terms converges iff its partial sums form a bounded sequence.


Theorem 5
:   1. If $|a_n|\leq c_n$ for $n\geq N$, and if $\sum c_n$ converges, then $\sum a_n$ converges.
    2. If $a_n\geq d_n\geq 0$ for $n\geq N$, and if $\sum d_n$ diverges, then $\sum a_n$ diverges.

proof
: Given $\epsilon>0$, there exists $N$ s.t. $m\geq n\geq N$ implies 
$$ 
 \sum_{k=n}^m c_k <\epsilon,
$$
by Cauchy criterion. Hence 
$$ 
 |\sum_{k=n}^m a_k|\leq \sum_{k=n}^m |a_k|\leq \sum_{k=n}^m c_k <\epsilon.
$$
$\Box$

## 2. The Root and Ratio Tests

Theorem 6 (Root test)
: Given $\sum a_n$, put $\alpha = \lim\sup_{n\to\infty} \sqrt[n]{|a_n|}$. Then 
1. if $\alpha<1$, $\sum a_n$ converges;
2. if $\alpha>1$, $\sum a_n$ diverges;
3. if $\alpha =1$, the test gives no information.

proof
: If $\alpha<1$, we can choose $\alpha<\beta<1$, and an integer $N$ s.t. 
$$ 
 \sqrt[n]{|a_n|}<\beta
$$
for $n\geq N$. It follows that $|a_n|^n<\beta^n$. Since $\sum \beta^n$ converges, by `Theorem 5 (i)`, $\sum a_n$ converges.
If $\alpha >1$, then there is a sequence $\{n_k\}$ s.t. $\sqrt[n_k]{|a_{n_K}|}\to \alpha$. Hence $a_n \to 0$  does not hold.
$\Box$

Theorem 7 (Ratio test)
: The series $\sum a_n$, 
    1. converges if $\lim\sup_{n\to\infty}|a_{n+1}/a_n|<1$,
    2. diverges if  $|a_{n+1}/a_n|\geq 1$ for all $n\geq N$.

proof
: Under condition (a), we can find $\beta<1$ and integer $N$ s.t. 
$$ 
 \left| \frac{a_{n+1}}{a_n} \right|<\beta
$$
for $n\geq N$. It follows that $|a_n|< |a_N|\beta^{n-N}$. Then (a) follows from the fact that $\sum \beta^n$ converges.
If $|a_{n+1}|\geq |a_n|$ for $n\geq N$, it is easily seen that $a_n\to 0$ does not hold.
$\Box$

Notice that the ratio test is easier to apply than the root test, since it easier to compute ratios than roots. However, the root test has wider scope. More precisely, whenever the ratio test shows convergence, the root test does too; whenever the root test is inconclusive, the ratio test is too.


## 3. Absolute Convergence
The series $\sum a_n$ is said to be `absolutely convergent` if the series $\sum |a_n|$ converges.

Theorem 8  
: if $\sum a_n$ converges absolutely, then $\sum a_n$ converges.

proof
: $|\sum_{k=n}^m a_k|\leq \sum_{k=n}^m |a_k|$.
$\Box$
