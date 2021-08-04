+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 11 Sequences and Series of Functions"
date = "2021-04-11T10:52:59+02:00"

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


We have studied how to define a number by convergent sequences or series. In this chapter we discuss how to define a function by a sequence or series of functions, and study the properties of this function.

## 1. Uniform Convergence

Definition 1 (**Pointwise convergence**)
: Suppose $\{f_n\}$ be a sequence of functions defined on a set $E$, and suppose that the sequence of numbers $\{f_n(x)\}$ converges for every $x\in E$. We can define a function $f$ by 
$$ 
 f(x) = \lim_{n\to\infty} f_n(x).  \tag{1}
$$
We say that $\{f_n\}$ `converges pointwise` to $f$ on $E$. Similarly, if $\sum f_n (x)$ converges for every $x\in E$, we can define $f$ by 
$$ 
 f(x) = \sum_{n=1}^\infty f_n(x).  \tag{2}
$$

Definition 2 (**Uniform convergence**)
: We say that a sequence of functions $\{f_n\}$ `converges uniformly` to a function $f$ on $E$ if for every $\epsilon>0$ there exists an integer $N$ s.t. $n\geq N$ implies 
$$ 
 |f_n(x) - f(x)|<\epsilon \tag{3}
$$
for all $x\in E$.

It is clear that every uniformly convergent sequence is pointwise convergent.

Theorem 3 (**Cauchy criterion**)
: The sequence of functions $\{f_n\}$ defined on $E$ converges uniformly on $E$ iff for every $\epsilon>0$ there exists an integer $N$ s.t. $m,n\geq N$ implies 
$$ 
 |f_n(x) - f_m(x)|<\epsilon, \tag{4}
$$
for all $x\in E$.

proof
: '$\Rightarrow$' is trivial. We show '$\Leftarrow$' only. Suppose the Cauchy condition holds, we have that $\{f_n(x)\}$ converges for every $x\in E$ to a limit function $f$. We shall prove the convergence is uniform.
Let $\epsilon>0$ be given, we choose $N$ s.t. (4) holds. Fix $n$ and let $m\to\infty$, we have 
$$ 
 |f_n(x) - f(x)|<\epsilon
$$
for every $n\geq N$ and every $x\in E$.
$\Box$

Theorem 4
: The sequence of functions $\{f_n\}$ defined on $E$ converges uniformly to $f$ on $E$ iff
$$ 
 \lim_{n\to\infty}\sup_{x\in E} |f_n(x) - f(x)| = 0.
$$

proof
:  We show '$\Leftarrow$' only. For any $\epsilon>0$, choose $N$ s.t. $n\geq N$ implies 
$$ 
 \sup_{x\in E}|f_n(x) - f(x)|  < \epsilon.
$$
It follows that for every $x\in D$, $|f_n(x) - f(x)|\leq \sup_{x\in E}|f_n(x) - f(x)|  < \epsilon$.
$\Box$

Theorem 5
: Suppose $\{f_n\}$ is a sequence of functions defined on $E$, and suppose for every $x\in E$ and $n=1,2,...$
$$ 
 |f_n(x)|\leq M_n.
$$
Then  $\sum f_n$ converges uniformly on $E$ if $\sum M_n$ converges.

proof
: $|\sum_{k=n}^m f_k(x)|\leq \sum_{k=n}^m M_k < \epsilon$.
$\Box$

## 2. Continuity
Theorem 6
: Suppose $f_n\to f$ uniformly on a set $E$. Let $x_0$ a limit point of $E$, and suppose that, for $n=1,2,...$
$$ 
 \lim_{x\to x_0}f_n(x) = a_n.
$$
Then $\{a_n\}$ converges, and 
$$ 
 \lim_{x\to x_0} f(x) = \lim_{n\to\infty} a_n.
$$
In other words, $\lim_{x\to x_0}\lim_{n\to\infty} f_n(x) = \lim_{n\to\infty}\lim_{x\to x_0} f_n(x)$.

proof
: By the uniform convergence of $\{f_n\}$, for every $\epsilon>0$, there is $N$ s.t. for any $m,n\geq N$ and any $x\in E$, 
$$ 
 |f_n(x) - f_m(x)|<\epsilon.
$$
Now let $x\to x_0$, we obtain $|a_n - a_m|\leq \epsilon$. So $\{a_n\}$ converges, say to $A$.
Next, $|f(x) - A|\leq |f(x) - f_n(x)| + |f_n(x) - a_n| + |a_n - A|$. We first choose $n$ s.t 
$$ 
 |f(x) - f_n(x)|<\epsilon/3, \quad \forall x\in E \quad (\text{uniform convergence}),
$$
and s.t. 
$$ 
 |a_n - A| < \epsilon/3 , \quad (\text{convergent}).
$$
Then, for this $n$, we choose a neighbourhood $V$ of $x_0$ where
$$ 
 |f_n(x) - a_n| <\epsilon/3.
$$
Overall, for $x \in E\cap V, x\neq x_0$, we have $|f(x) - A|<\epsilon.$
$\Box$

Theorem 7 (Continuity)
: If $\{f_n\}$ is a sequence of continuous functions on $E$, and if $f_n\to f$ uniformly on $E$, then $f$ is continuous on $E$.

proof
: For $x\in E$, we have $\lim_{x\to x_0} f_n(x) = f_n(x_0)$. By the Theorem 6, we know that $\lim_{x\to x_0} f(x) = \lim_{n\to\infty}f_n(x_0) = f(x_0)$.
$\Box$

Theorem 8
: Suppose $K$ is compact, and 
    1. $\{f_n\}$ is a sequence of continuous functions on $K$,
    2. $\{f_n\}$ converges pointwise to a continuous function $f$ on $K$,
    3. $f_n(x)\geq f_{n+1}(x)$ for all $x\in E, n = 1,2,...$. 
    
    Then $f_n \to f$ uniformly on $K$.

proof
: Let $g_n = f_n -f $, then $g_n$ is continuous, $g_n \to 0$ pointwise, and $g_n\geq g_{n+1}$. It suffices to show that $g_n \to 0$ uniformly on $K$.
Given $\epsilon>0$, let $K_n=\{x\in K: g_n(x)\geq \epsilon\}$. Since $g_n$ is continuous, $K_n$ is closed and hence compact. Since $g_n\geq g_{n+1}$, $K_n\supset K_{n+1}$. For any $x\in K$, since $g_n(x)\to 0$, we see that $x\notin K_n$ for some $n$, hence $x\notin \cap K_n$. 
In other words, $\cap K_n=\emptyset$, and hence $K_N = \emptyset$ for some $N$. It follows that $0\geq g_n(x) <\epsilon $ for all $x\in K$ and for all $n\geq N$.

## 3. Integration

Theorem 9 (**Integration**)
: Let $\alpha$ be a monotonically increasing on $[a,b]$. Suppose $f_n \in \mathcal{R}(\alpha)$ on $[a,b]$ for $n=1,2,...,$ and suppose $f_n\to f$ uniformly on $[a,b]$. Then $f\in \mathcal{R}(\alpha)$ and 
$$ 
 \int_a^b f d\alpha = \lim_{n\to\infty}\int_a^b f_n d\alpha .
$$

proof
: Put $\epsilon_n = \sup_x |f_n(x) - f(x)|$. Then, 
$$ 
 f_n - \epsilon_n \leq f \leq f_n + \epsilon,
$$
so that 
$$ 
 \int_a^b (f_n - \epsilon_n) d\alpha \leq \sup_T L(T,f,\alpha)\leq \inf_T U(T,f,\alpha) \leq \int_a^b (f_n + \epsilon_n) d\alpha.  \tag{5}
$$
Hence $\inf_T U(T,f,\alpha) - \sup_T L(T,f,\alpha)\leq 2\epsilon_n[\alpha(b) - \alpha(a)]\to 0$ by uniform convergence. Thus $f\in \mathcal{R}(\alpha)$ and (5) yields
$$ 
 \left| \int_a^b fd \alpha  - \int_a^b f_n d\alpha \right|  \;\leq \epsilon_n[\alpha(b) - \alpha(a)]\to 0
$$
$\Box$

## 4. Differentiation

Theorem 10 (**Differentiation**)
: Suppose $\{f_n\}$ is a sequence of functions, differentiable on $[a,b]$ and $\{f_n(x_0)\}$ converges for some point $x_0\in[a,b]$. If $\{f_n'\}$ converges uniformly on $[a,b]$, then $\{f_n\}$ converges uniformly on $[a,b]$ to a function $f$, and 
$$ 
 f'(x) = \lim_{n\to\infty}f_n'(x) ,\quad \forall x\in[a,b].
$$

proof
: Let $\epsilon>0$ be given. By the convergence, we choose $N$ s.t. $m,n\geq N$ implies 
$$ 
 |f_n(x_0) - f_m(x_0)|<\epsilon/2,
$$
and 
$$ 
 |f_n'(x) - f_m'(x)|< \frac{\epsilon}{2(b-a)}, \quad x\in[a,b]  . \tag{6}
$$
Apply the mean value theorem to the function $f_n - f_m$, (6) yields that 
$$ 
 |f_n(x) - f_m(x) - f_n(t) + f_m(t)|\leq \frac{|x-t|\epsilon}{2(b-a)}  < \epsilon/2. \tag{7}
$$
Then by triangle inequality, we have 
$$ 
 |f_n(x) - f_m(x)|\leq   |f_n(x) - f_m(x) - f_n(x_0) + f_m(x_0)| + |f_n(x_0) - f_m(x_0)|<\epsilon.
$$
Thus we obtain the uniform convergence, and we write $f_n\to f$ uniformly.
Next, fix a point $x\in [a,b]$ and define 
$$ 
 \phi_n(t) = \frac{f_n(t) - f_n(x)}{t -x}, \quad   \phi(t) = \frac{f(t) - f(x)}{t -x}.
$$
Then $\lim_{t\to x} \phi_n(t) = f_n'(x)$ by differentiability. We shall show that $\{\phi_n\}$ converges uniformly. The first inequality in (7) gives
$$ 
 |\phi_n(t) - \phi_m(t)|\leq \frac{\epsilon}{2(b-a)}, \quad (n,m\geq N,t\in[a,b]\setminus\{x\}).
$$
So the uniform convergence of $\{\phi_n\}$ is obtained for $t\neq x$. Since $\{f_n\}$ converges to $f$, we conclude that 
$$ 
 \lim_{t\to\infty}\phi_n(t) = \phi(t)
$$
By Theorem 6, we have 
$$ 
 \lim_{t\to x} \phi(t) = \lim_{n\to\infty}f_n'(x).
$$




## Complements

Definition (**Open cover**)
: By an `open cover` of  a set $E$ in a metric space $X$, we mean a collection $\{G_\alpha\}$ of open subsets (*contain interior points only*) of $x$ s.t. $E\subset \cup_\alpha G_\alpha$.

Definition (**Compact**)
: A subset $K$ of a metric space $X$ is said to be `compact` relative to $X$ if every open cover of $K$ contains a finite subcover.

Theorem 
: Suppose $K\subset Y\subset X$. Then $K$ is compact relative to $X$ iff $K$ is compact relative to $Y$.

Theorem
: Compact subsets of metric spaces are closed (*contains all limit points*).

proof
: We shall prove that the complement of $K$ is an open subset of $X$. Suppose $p\in X, p\notin K$. If $q\in K$, let $V_q$ and $W_q$ be neighbourhoods of $p$ and $q$, relatively, of radius less than $\frac{1}{2}d(p,q)$. Since $K$ is compact, we can find finitely many $q_1,...,q_n \in K$ s.t. 
$$ 
 K \subset \cup_{j=1}^n W_{q_j}:= W.
$$
If $V = \cap_{i=1}^n V_{q_i}$, then $V$ is a neighbourhood of $p$ and $V\cap W =\emptyset$. Hence $V\subset K^\complement$, so $p$ is an interior point of $K^\complement$.
$\Box$

Theorem 
: Closed subsets of compact sets are compact.


Corollary
: If $F$ is closed and $K$ is compact, then $F\cap K$ is compact.

Theorem
: If $\{K_\alpha\}$ is a collection of compact subsets of a metric space $X$ s.t. the intersection of every finite subcollection of $\{K_\alpha\}$ is nonempty, then $\cap K_\alpha$ is nonempty.

Corollary
: If $\{K_n\}$ is a collection of nonempty compact sets s.t. $K_n\supset K_{n+1}$, then $\cap K_n$ is not empty.



