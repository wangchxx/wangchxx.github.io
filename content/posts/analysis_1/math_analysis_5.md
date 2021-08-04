+++
author = "Wang Chaohua"
title = "Mathematical Analysis | 5 Derivatives and Differentiations"
date = "2021-04-05T10:52:59+02:00"

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


## 1. Derivatives

Definition 1 (Derivative at $x_0$)
: Given a function $f$ defined on an neighbourhood of $x_0$ $U(x_0,\delta)$, we say that $f$ is `differentiable` at $x_0$ if the following limit exists
$$ 
\lim_{x\to x_0}\frac{f(x)- f(x_0)}{x-x_0}, 
$$
denoted by $f'(x_0)$.

According to the definition, we can see that if $f$ has derivative at $x_0$, then it is continuous at $x_0$. But the converse is not true.

Definition 2 (One-sided derivatives)
: Given a function $f$ defined on $[x_0,x_0+\delta)$, then it has a right derivative at $x_0$, if the right limit exists
$$ 
\lim_{x\to x_0^+}\frac{f(x)- f(x_0)}{x-x_0}, 
$$
denoted by $f'_{+}(x_0)$.

Theorem 3
: $f'(x_0)$ exists iff both $f'\_{+}(x_0)$ and $f'\_{-}(x_0)$ exist.


Definition 4 (Local maximum)
: If there is a neighbourhood $U(x_0,\delta)$ where for any $x\in U(x_0,\delta)$ s.t. 
$$ 
 f(x_0)\geq f(x),
$$
we say that $f$ attains its local maximum at $x_0$.

Theorem 5 (Fermat's Theorem)
: If $f$ has a local extremum at $x_0$ and if it is differentiable at $x_0$, then $f'(x_0) = 0$.

## 2. Differentials

Definition 5 (Differential)
: We define an increment of $f$ by $\Delta y = f(x_0 + \Delta x) - f(x_0)$. If there exists a constant $A$ s.t. 
$$ 
 \Delta y = A\Delta x + o(\Delta x),
$$
we say $f$ has a differential at $x_0$, denoted by $d y|_{x_0} = A\Delta x$.

Theorem 6 
: $f$ has a differential at $x_0$ iff $f$ is differentiable at $x_0$ and $A = f'(x_0)$.

