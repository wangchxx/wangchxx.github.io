+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 8 Indefinite Integrals"
date = "2021-04-08T10:52:59+02:00"

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


## 1. Definitions 

Definition 1 (**Primary function**)
: Let $f$ and $F$ be functions defined on $I$. If $F'(x) = f(x)$ for every $x\in I$, we say that $F$ is the `primary function` of $f$ on $I$.

Theorem 2 (**Existence**)
: If $f$ is continuous on $I$, then $f$ possesses a primary function $F$ on $I$.

Definition 3 (**Indefinite integral**)
: The set of all primary functions of $f$ on $I$ is called the `indefinite integral` of $f$ on $I$, denoted by $\int f(x) dx= F(x) + C$.

## 2. Change of Variable and Integration by Parts

Theorem 4 (**Change of variable**)
: Let $f(x)$ defined on $I$, $\phi(t)$ differentiable on $J$ and $\phi(J)\subset I$.

1. If the indefinite integral $\int f(x) dx = F(x) + C$ exists, then the indefinite integral $\int f(\phi(t))\phi'(t) dt$ exists too, and $\int f(\phi(t))\phi'(t) dt = F(\phi(t))+C$
2. If the function $x = \phi(t)$ has inverse function $t=\phi^{-1}(x)$,and $\int f(x) dx = F(x) + C$ exists, then then the indefinite integral $\int f(\phi(t))\phi'(t) dt = G(t) + C$ exists too, and $\int f(x) dx =G(\phi^{-1}(x)) + C$.

Theorem 5 (**Integration by Parts**)
: If $u(x)$ and $v(x)$ are differentiable, and $\int v(x)u'(x) dx$ exists, then $\int v'(x) u(x) dx$ exists too, and $\int v'(x) u(x) dx = v(x)u(x) - \int v(x) u'(x) dx$.

proof
: $[u(x)v(x)]' = u'(x)v(x) + v'(x)u(x)$.

$\Box$
