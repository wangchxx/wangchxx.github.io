+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 12 Power Series"
date = "2021-04-12T10:52:59+02:00"

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


In this Chapter we shall the power series formed by the sequence of power functions $\{c_n (x-x_0)^n\}$, i.e. of the form 
$$ 
 \sum_{n=0}^\infty c_n (x-x_0)^n. \tag{1}
$$
W.l.o.g. we shall focus on the case where $x_0 = 0$, i.e. 
$$ 
   \sum_{n=0}^\infty c_n x^n. \tag{2}
$$

## 1. Power Series

First, we study the convergence of series (2).

Lemma 1
: Suppose the series (2) converges for $|x|< R$, then it is absolutely convergent on every  $[-R+\epsilon, R-\epsilon]$.

proof
: Let $a_n = |c_n x^n|$, which goes to zero and is bounded. We have $\lim\sup_{n\to\infty}\sqrt[n]{a_n} = 0 <1$. By root test we complete the proof.
$\Box$

Theorem 2      
: Suppose the series (2) converges for $|x|< R$, and define 
$$ 
 f(x) =   \sum_{n=0}^\infty c_n x^n, \quad (|x|< R). \tag{3}
$$
Then (2) converges uniformly on every $[-R+\epsilon, R-\epsilon]$. The function $f$ is continuous and differentiable in $(-R,R)$, and 
$$ 
 f'(x) = \sum_{n=1}^\infty n c_n x^{n-1}  , \quad (|x|< R). \tag{4}
$$

proof
: For $|x|< R-\epsilon$, we have 
$$ 
 |c_n x^n|\leq |c_n (R-\epsilon)^n|
$$
and since $\sum c_n (R-\epsilon)^n$ converges absolutely by Lemma 1, the series (2) converges uniformly on $[-R+\epsilon, R-\epsilon]$.
Next, we have $\lim\sup_{n\to\infty} \sqrt[n]{n|c_n|} = \lim\sup_{n\to\infty} \sqrt[n]{|c_n|}$ since $\sqrt[n]{n} = 1$, which implies that $f$ and $f'$ have the same interval of convergence. As (4) is also a power series, it converges uniformly in $[-R+\epsilon, R-\epsilon]$. We can apply Theorem 11.10 (Differentiation) and obtain the assertion (4).
Continuity of $f$ follows from the existence of $f'$.
$\Box$

Theorem 3
: Suppose $\sum c_n$ converges, Put 
$$ 
 f(x) =   \sum_{n=0}^\infty c_n x^n, \quad (|x|< 1).
$$
Then 
$$ 
 \lim_{x\to 1_-} f(x) = \sum_{n=0}^\infty c_n.
$$

proof
: Let $f_n(x) = \sum_{j=0}^n c_j x^j$. $f_n \to f$ at $x=1$, so $f_n\to f$ uniformly on $[0,1]$. Since $f_n$ are continuous, then $f$ is continuous on $[0,1]$ (left continuous at $x = 1$).
$\Box$
<!-- Let $s_n = \sum_{j=0}^n c_j$. Then 
$$ 
   \sum_{n=0}^m c_n x^n = \sum_{n=0}^m (s_n - s_{n-1}) x^n = (1-x)\sum_{n=0}^m s_n x^n + s_m x^m.
$$
For $|x|<1$, we let $m\to\infty$ and obtain
$$ 
 f(x) = (1-x)  \sum_{n=0}^\infty s_n x^n.
$$
suppose $\lim_{n\to\infty} s_n= s$. Let $\epsilon>0$ and choose $N$ so that $n>N$ implies
$$ 
 |s_n - s|<\epsilon/2.  
$$
Since $(1-x)  \sum_{n=0}^\infty  x^n = 1 , |x|<1$, we obtain
$$ 
 |f(x) - s| = |(1-x)  \sum_{n=0}^\infty (s_n -s) x^n|\leq |1-x|  
$$ -->


## 2. Power Series Expansion
If (1) converges for $|x-x_0|< R$, and a function $f$ can be represented as $f(x) = \sum_{n=0}^\infty c_n (x-x_0)^n$, then we say $f$ is `expanded in a power series`  about the point $x=x_0$.

Theorem 4 (**Taylor expansion**)
: Suppose $f(x) = \sum_{n=0}^\infty c_n x^n$, the series converging in $|x|< R$. If $a\in(-R,R)$, then $f$ can be expanded in a power series about the point $x = a$, which converges in $|x-a|< R - |a|$, i.e. 
$$ 
 f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x-a)^n.
$$

proof
: Notice that $f^{(k)}(x) = \sum_{n=k}^\infty n (n-1)\cdots (n-k+1) c_n x^{n-k}$. And 
$$
\begin{align*}
f(x) &= \sum_{n=0}^\infty c_n (x-a+a )^n \cr
         &= \sum_{n=0}^\infty c_n \sum_{m=0}^n \binom{n}{m} a^{n-m} (x-a )^m \cr
         &= \sum_{m=0}^\infty \sum_{n=m}^\infty \binom{n}{m} c_n a^{n-m} (x-a )^m
\end{align*}
$$

We can exchange the order of summation because  the series is convergent.
$\Box$

Theorem 5
: Suppose the series $\sum a_n x^n$ and $\sum b_n x^n$ converge in the segment $S = (-R,R)$. Let $E$ be the set of all $x\in S$ where 
$$ 
 \sum_{n=0}^\infty a_n x^n = \sum_{n=0}^\infty b_n x^n . \tag{5}
$$
If $E$ has a limit point in $S$, then $a_n = b_n$ for $n=0,1,2,...$. Hence the equation (5) holds for all $x\in S$.

proof
: Let $c_n = a_n - b_n$ and $f(x) = \sum_{n=0}^\infty c_n x^n $, then $f(x) = 0$ on $E$. 
Let $A$ be the set of limit points of $E$ in $S$, and $B = S\setminus A$. It is clear that $B$ is open. Suppose we can prove that $A$ is open, because $S = A\cup B$ and $S$ is connected `(check definiiton)`, then it follows that $B$ is empty, thus $A = S$. Since $f$ is continuous in $S$, $A\subset E$. Thus $E=S$, and $c_n = 0$ for $n=0,1,...$.

    Now we prove that $A$ is open. If $x_0\in A$, then we can expand $f$ at $x=x_0$ by 
    $$ 
     f(x) = \sum_{n=0}^\infty d_n (x - x_0)^n,\quad |x - x_0|< R- |x_0|.
    $$
    By Theorem 12.4, $d_n = 0$ for all $n$. So that $f(x)=0$  for all $x:|x-x_0|< R- |x_0|$, i.e. in a neighbourhood of $x_0$. This shows that $A$ is open.
$\Box$