---
author : "Wang Chaohua"
title : "Mathematical Analysis | 13 Fourier Series"
date : "2021-04-13T10:52:59+02:00"

tags : [
    "markdown",
]
categories : [
    "analysis"
]
series : ["math analysis"]
aliases : ["migrate-from-jekyl"]
math : true
---






## 1. Fourier Series

Definition 1 (**Trigonometric polynomial**)
: A `Trigonometric polynomial` is a finite sum of the form
$$ 
 f(x) = a_0 + \sum_{n=1}^N (a_n \cos nx  + b_n \sin nx),
$$
where $a_i,b_i$ are complex numbers. 

It can be written in the form 
$$ 
\begin{equation}
f(x) = \sum_{n=-N}^N c_n e^{inx},
\end{equation}
$$
which is more convenient for most purposes. It is clear that every Trigonometric polynomial has period $2\pi$. Notice that 
$$ 
 \frac{1}{2\pi}\int_{-\pi}^\pi e^{inx} dx =  1_{n=0},
$$
so we have 
$$ 
\begin{equation}
c_m =   \frac{1}{2\pi}\int_{-\pi}^\pi f(x)e^{-imx} dx
\end{equation}
$$
for $|m|\leq N$. 

Definition 2 (**Fourier series**)
: In agreement with (1), we define a `trigonometric series` to be a series of the form 
$$ 
\begin{equation}
   \sum_{n=-\infty}^\infty c_n e^{inx}.
\end{equation}
$$

If $f$ is integrable, the numbers $c_m$ defined by (2) for all integers $m$ are called the `Fourier coefficients` of $f$, and the series (3) formed with these coefficients is called a `Fourier series` of $f$.


A natural question is whether the Fourier series of $f$ converges to $f$.

Definition 3 (**Orthogonal system of functions**)
: Let $\{\phi_n\}$ be a sequence of complex functions on $[a,b]$, s.t. 
$$ 
 \int_a^b \phi_n(x) \bar{\phi}_m(x) dx = 0,\; (n\neq m) .
$$
Then $\{\phi_n\}$ is said to be an `orthogonal system of functions` on $[a,b]$. In particular, if 
$$ 
   \int_a^b |\phi_n(x)|^2  dx = 1
$$
for all $n$, then  $\{\phi_n\}$ is said to be `orthonormal`.

Let $\\{\phi_n\\}$ be orthonormal on $[a,b]$. If $c_n = \int_a^b f(x) \bar{\phi}_n(x) dx$ for all $n$, we call $c_n$ the n-th Fourier coefficient of 
$f$ relative to $\\{\phi_n\\}$. Write $f(x) \sim \sum\_{n=1}^\infty c_n \phi_n(x)$ and call this series the Fourier series of $f$ relative to $\\{\phi_n\\}$.


Theorem 4
: Let $\{\phi_n\}$ be orthonormal on $[a,b]$. Let 
$$ 
 s_n(x) = \sum_{m=1}^n c_m \phi_m(x)
$$
be the n-th partial sum of the Fourier series of $f$, and define 
$$ 
    t_n (x) = \sum_{m=1}^n \gamma_m \phi_m(x) .
$$
Then 
$$ 
 \int_a^b |f - s_n|^2 dx \leq   \int_a^b |f - t_n|^2 dx,
$$
and the equality holds iff $c_m = \gamma_m$, $m=1,...,n$. 

proof
: Omit scripts $a,b,n$, we write $\int,\sum$. Then 
$$ 
 \int f \bar{t}_n = \int f \sum \bar{\gamma}_m \bar{\phi}_m = \sum \bar{\gamma}_m c_m
$$
by the definition of $c_m$. And 
$$ 
 \int |t_n|^2 = \sum |\gamma_m|^2
$$
since $\{\phi_n\}$ is orthonormal, and so 


$$
\begin{align*}
   \int |f-t_n|^2 &= \int |f|^2 - \int f \bar{t}_n - \int \bar{f}t_n + \int |t_n|^2 \cr
        &= \int |f|^2 - \sum \bar{\gamma}_m c_m - \sum {\gamma}_m  \bar{c}_m + \sum |\gamma_m|^2 \cr
        &=\int |f|^2 + \sum |\gamma_m - c_m|^2 - \sum |c_m|^2.
\end{align*}
$$
which is minimized by $\gamma_m = c_m$.

$\Box$

This theorem says that among all functions $t_n$, $s_n$ gives the best mean-square approximation to $f$.

Theorem 5
: Let $\{\phi_n\}$ be orthonormal on $[a,b]$. If $f(x)\sim \sum_{n=1}^\infty c_n \phi_n(x)$, then 
$$ 
   \sum_{n=1}^\infty |c_n|^2 \leq \int_a^b |f(x)|^2 dx.
$$
In particular, $\lim_{n\to\infty} c_n = 0$.

proof
: Given $n$, we have 
$$ 
 \int |s_n|^2 =    \sum_{m=1}^n |c_m|^2 \leq \int |f|^2.
$$
We draw the conclusion by letting $n\to\infty$.
$\Box$


## 2. Convergence
From now on we shall deal only with the trigonometric system. We shall consider functions $f$ that have period $2\pi$ and that are Riemann-integrable on $[-\pi,\pi]$. We define the N-th partial sum of the Fourier series of $f$ by 
$$ 
 S_N(x) = S_N(f;x) = \sum_{n=-N}^N c_n e^{inx}.
$$

Definition 6 (**Dirichlet kernel**)
: The `Dirichlet kernel` is defined by 
$$ 
\begin{equation}
 D_N(x) :=   \sum_{n=-N}^N  e^{inx} = \frac{\sin(N+1/2)x}{\sin(x/2)}.
\end{equation}
$$
The second equality follows from the fact
$$ 
   (e^{ix} - 1) D_N(x) = e^{i(N+1)x} - e^{-iNx},
$$
and multiply $e^{-ix/2}$ on both sides.

Now we can rewrite $S_N(f;x)$ as 
$$ 
 \begin{align*}
    S_N(f;x) &= \sum_{n=-N}^N \frac{1}{2\pi} \int f(t)e^{-int} dt\; e^{inx} \cr
        &= \frac{1}{2\pi}  \int f(t) \sum_{n=-N}^N   e^{in(x-t)} dt \cr
        &= \frac{1}{2\pi}  \int f(t) D_N(x-t) dt \cr
        &= \frac{1}{2\pi}  \int f(x-t) D_N(t) dt.
 \end{align*} 
$$

Theorem 7 (**Convergence**)
: If, for some $x$, there are constants $\delta>0$ and $M<\infty$ s.t. 
$$ 
 |f(x+t) - f(x)|\leq M|t|
$$
for all $|t|<\delta$, then 
$$ 
 S_N(f;x)\to f(x) \text{ as } N\to\infty.
$$

proof
: Define 
$$ 
 g(t) = \frac{f(x-t) - f(x)}{\sin(t/2)}
$$
for $0<|t|\leq \pi$, and let $g(0) = 0$. We have 

$$ 
 \begin{align*}
    S_N(f;x) - f(x) &= \frac{1}{2\pi}  \int (f(x-t) - f(x)) D_N(t) \;dt \cr
        &=\frac{1}{2\pi}  \int g(t) \sin(N+1/2)t \;dt \cr
        &=\frac{1}{2\pi}  \int g(t) \cos(t/2)\sin(Nt) \;dt + \frac{1}{2\pi}  \int g(t) \sin(t/2)\cos(Nt) \;dt
 \end{align*}
$$
By assumption, $g(t) \cos(t/2),g(t) \sin(t/2)$ are bounded. By Theorem 13.5, the last two integrals tend to 0 as $N\to\infty$.
$\Box$

Theorem 8
: If $f$ is continuous (with period $2\pi$), then given $\epsilon>0$ there exists a trigonometric polynomial $P$ s.t. 
$$ 
 |P(x) - f(x)|< \epsilon,\;\forall x.
$$

proof
: $f$ can be regarded as a function on the unit circle $T$, by means of mapping $x\mapsto e^{ix}$. Notice that the trigonometric polynomials form a self-adjoint algebra $\mathcal{A}$, which seperates points on $T$, and vanishes at no point of $T$. For $T$ a unit circle. Since $T$ is compact, we have that $\mathcal{A}$ is dense in $C(T)$.


Theorem 9 (**Parseval's theorem**)
: Suppose $f$ and $g$ are Riemann-integrable functions with period $2\pi$, and 
$$ 
 f(x)\sim \sum_{-\infty}^\infty c_n e^{inx},\quad g(x)  \sim \sum_{-\infty}^\infty \gamma_n e^{inx}.
$$
Then 
$$ 
 \begin{align}
 \lim_{N\to\infty} \frac{1}{2}\int_{-\pi}^\pi |f(x) - S_N(f;x)|^2 dx &= 0 ,\cr
 \frac{1}{2}\int_{-\pi}^\pi f(x)\bar{g}(x) dx &= \sum_{-\infty}^\infty c_n \bar{\gamma}_n, \cr
 \frac{1}{2}\int_{-\pi}^\pi |f(x)|^2 dx &= \sum_{-\infty}^\infty |c_n|^2.\cr
 \end{align}
$$

proof
: Define the norm
$$
 ||h||_2 = \left( \frac{1}{2\pi}\int\_{-\pi}^\pi |h(x)|^2 dx \right)^{1/2}.
$$
We can choose a continuous $2\pi$-periodic function $h$ s.t. 
$$
 || f-h||_2 < \epsilon.
$$
By Theorem 13.8, there is a trigonometric polynomial $P$ s.t. $|P(x) - h(x)|<\epsilon$ for all $x$. Hence $||P - h ||_2<\epsilon$. Suppose that $P$ has degree $N_0$, Theorem 13.4 shows that 
$$
 ||h - S_N(h) ||_2\leq ||h - P ||  <\epsilon
$$
for all $N\geq N_0$. With $h-f$ in place of $f$, 
$$ 
 ||s_N(h) - s_N(f) ||_2 = || s_N(h-f)||_2\leq || h-f||_2<\epsilon.
$$
By the triangle inequality,
$$ 
 ||f-s_N(f) ||_2< 3\epsilon,\; (N\geq N_0).
$$






## Complements

Definition (**Self-adjoint**)
: An algebra $\mathcal{A}$ of complex functions is said to be `self-adjoint` if $f\in\mathcal{A}\Rightarrow \bar{f}\in\mathcal{A}$.

Definition (**Seperate points on E**)
: Let $\mathcal{A}$ be a family of functions on a set $E$. Then $\mathcal{A}$ is said to `seperate ponits` on $E$ if to every pair of distinct points $x_1,x_2\in E$, there corresponds a function $f\in\mathcal{A}$ s.t. $f(x_1)\neq f(x_2)$.

Definition (**Vanish at no point**)
: If to each $x\in E$ there corresponds a function $g\in\mathcal{A}$ s.t. $g(x)\neq0$, we say that $\mathcal{A}$ `vanish at no point` of $E$.

Theorem
: Suppose $\mathcal{A}$ is self-adjoint algebra of complex continuous  functions on a compact set $K$, $\mathcal{A}$ separates points on $K$, vanishes at no point of $K$. Then the uniform closure $\mathcal{B}$ of $\mathcal{A}$ consists of all complex continuous functions on $K$. In other words, $\mathcal{A}$ is dense $C(K)$.
