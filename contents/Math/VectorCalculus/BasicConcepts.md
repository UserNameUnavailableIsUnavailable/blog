# Basic Concepts

## Function

A function consists of three parts: domain, codomain, and a rule that maps any element from domain to exactly one element in codomain. For $f: \mathbb{R}^m \mapsto \mathbb{R}^n$, the domain is $\mathbb{R}^m$, the codomain is $\mathbb{R}^n$, and the rule is $f$.

### Domain

Set of inputs accepted by the function. We use $\mathrm{dom}\;f$ to denote the domain of a function. A function may come with a **natrual domain**.

### Range vs. Image

Both terms can be used to describe the set of all outputs that the function can produce. But Image can also be used in an element-wise manner, e.g., if $f(a) = b$, one can say that $b$ is the image of $a$ by rule $f$. The range (or image) of a function $f:\boldsymbol{X}\mapsto\boldsymbol{Y}$ can be denoted by $f(\boldsymbol{X}) = \{f(x)\;|\;x \in \boldsymbol{X}\}$.

### Codomain

The set of elements that the function may produce and must be at least as big as the range. Unlike domain, there is no such thing as "natrual codomain", so codomain is always choosed manually.

### Special cases

- **Onto**: A function $f:\boldsymbol{X}\mapsto\boldsymbol{Y}$ is onto (or **surjective**) if $\forall\; y \in \boldsymbol{Y}$ there $\exists\; x \in \boldsymbol{X}$ such that $f(x)=y$.
- **One-to-one**: A function $f:\boldsymbol{X}\mapsto\boldsymbol{Y}$ is one-to-one (or **injective**) if $\forall\; y \in \boldsymbol{Y}$ there is at most one $x \in \boldsymbol{X}$ such that $f(x) = y$.
- **Invertible**: A function is invertible (or **bijective**) if it is both onto and one-to-one. For an invertible mapping $f:\boldsymbol{X}\mapsto\boldsymbol{Y}$, we say its inverse image is $f^{-1}:\boldsymbol{Y}\mapsto\boldsymbol{X}$.


## Vectors, matrices, and derivatives

### Points and vectors

Points (e.g., $\boldsymbol{a}$) cannot be added, but vectors (e.g., $\boldsymbol{\vec{b}}$) can. The substraction of two points constructs a vector.

### Subspace of $\mathbb{R}^n$

A subspace (or **vector subspace**) of $\mathbb{R}^n$ is a subset of $\mathbb{R}^n$ such that it is closed under addition and multiplication by scalars.

### Vector field

A vector field is a function that take a point in $\mathbb{R}^n$ as input and outputs a vector in $\mathbb{R}^n$ **emanating from that point**.