# Conditional Probability

## Discrete Form

A discrete random variable $X$ is conditioned on an event $A$ ($P(A) > 0$), then we may define the **conditional PMF** of $X$ as follows:

$$p_{X | A} (x) = P( X = x | A)=\frac{P(\{X = x\} \cap A)}{P(A)}.$$

Apparently, $p_{X | A} \ge 0$. And,

$$\displaystyle\sum_{i = 1}^{N} p_{X | A}(x_i) = \displaystyle\sum_{i = 1}^{N} \frac{P(\{X = x_i\} \cap A)}{P(A)}.$$

Since $\{X = x_i\} (i = 1, 2, 3, \cdots, N)$ is a partition of $\Omega$, so,

$$\displaystyle\sum_{i = 1}^N P(X = x_i \cap A) = P(A).$$

Thus,

$$\displaystyle\sum_{i = 1}^{N} p_{X | A}(x_i) = 1,$$

and $p_{X|A}(x)$ is a legitimate PMF.

### PMF conditioned on another discrete *r.v.*

Now we consider the special case $A = \{Y = y\}$, here $Y$ is another discrete random variable. We get

$$p_{X|Y}(x|y) = \frac{P(X = x, Y = y)}{P(Y = y)} = \frac{p_{X, Y}(x, y)}{p_Y(y)}.$$

It is easy to get

$$p_{X, Y}(x, y) = p_Y(y)p_{X|Y}(x|y) = p_X(x)p_{Y|X}(y|x).$$

Now let us delve into $p_{X|A}(x)$ by using total probability theorem.
Given $B_i (i = 1, 2, \cdots, N)$ as a partition of $A$, then,

$$A = \displaystyle\bigcup_{i = 1}^{N} (A \cap B_i);$$

using Morgan's theorem, we get

$$\{X = x\} \cap A = \displaystyle\bigcup_{i = 1}^{N} \{X = x\} \cap (A \cap B_i).$$

<!-- $$P(A) = \displaystyle\sum_{i = 1}^{N} P(A \cap B_i).$$ -->

Finally, we get

$$
\begin{split}
p_{X|A}(x) &= \frac{P(\{X = x\} \cap A)}{P(A)} \\
&= \frac{\displaystyle\sum_{i = 1}^{N} P(\{X = x\} \cap (A \cap B_i))} {P(A)} \\
&= \frac{\displaystyle\sum_{i = 1}^N P(\{X = x\} | (A \cap B_i)) P(A \cap B_i)}{P(A)} \\
&= \displaystyle\sum_{i = 1}^N P(B_i|A) P(\{X = x\}|A \cap B_i) \\
&= \displaystyle\sum_{i = 1}^N P(B_i|A) p_{X|(A \cap B_i)}(x).
\end{split}
$$

As a special case, we let $A = \Omega$, in which $B$ will be a partition of $\Omega$, then

$$p_X(x) = \displaystyle\sum_{i = 1}^N P(B_i)p_{X|Bi}(x).$$

## Continuous Form

A continuous random variable $X$ is conditioned on an event $A$ ($P(A) > 0$), then the possibility that $X \in B$ is

$$P(\{X \in B\} | A) = \frac{P(\{X \in B\} \cap A)}{P(A)}.$$

We define **conditional PDF** of $X$ as $f_{X|A}(x)$.

Then we get

$$P(\{X \in B\} | A) = \frac{\int_B f_{X|A}(x)dx}{P(A)}.$$

So, $\forall B \sub \Omega$, the following equation holds:

$$\int_B f_{X|A}(x)dx = P(\{X \in B\} \cap A).$$

Let $B = (x, x + \delta)(\delta > 0)$,

$$\lim_{\delta \rightarrow 0^+} \int_x^{x + \delta}f_{X|A}(x)dx = \lim_{\delta \rightarrow 0^+} f_{X|A}(x) \delta = \lim_{\delta \rightarrow 0^+} P(\{x \le X \le x + \delta\} | A);$$

Then we get

$$
\begin{split}
f_{X|A}(x)
&= \lim_{\delta \rightarrow 0^+} \frac{P(\{x \le X \le x + \delta\} | A)}{\delta}\\
&= \lim_{\delta \rightarrow 0^+} \frac{P(\{x \le X \le x + \delta\} \cap A)}{\delta P(A)}.\\
\end{split}
$$

Since $P(A) \gt 0, \delta \gt 0$ and ${P(\{x \le X \le x + \delta\} \cap A)}$ is a valid probability, we know that $f_{X|A}(x) \ge 0.$

Let $B = (-\infin, +\infin)$, we see that

$$\int_{-\infin}^{+\infin} f_{X|A}(x) dx = \frac{P(\{X \in (-\infin, +\infin)\} \cap A)}{P(A)} = \frac{P(\Omega \cap A)}{P(A)} = 1,$$ and thus $f_{X|A}(x)$ is legitimate.

### PDF conditioned on another continuous *r.v.*

Consider the case $A = \{Y = y\}$, different from what we see in the corresponding PMF case, the tricky thing is that $P(Y = y) = 0$ for continuous $Y$. Here, instead of directly considering $P(Y = y)$, we turn to $P(y \le Y \le y + \epsilon) (\epsilon > 0).$

$$
\begin{split}
&\;P(\{x \le X \le x + \delta\}|\{y \le Y \le y + \epsilon\})\\
&= \frac{P(\{x \le X \le x + \delta\} \cap \{y \le Y \le y + \epsilon\})}{P(y\le Y \le y + \epsilon)}.\\
\end{split}
$$

Now, we let $\epsilon \rightarrow 0^+$:

$$
\begin{split}
P(\{x \le X \le x + \delta\} | \{Y = y\}) &= \lim_{\epsilon \rightarrow 0^+} \frac{\int_x^{x + \delta} f_{X, Y}(x, y) \epsilon}{f_{Y}(y) \epsilon}\\
&= \frac{\int_x^{x + \delta} f_{X, Y}(x, y)}{f_Y(y)}.
\end{split}
$$

Note that we've already known that $X$'s PDF conditioned on $A$:

$$f_{X|A}(x) = \lim_{\delta \rightarrow 0^+} \frac{P(\{x \le X \le x + \delta\} | A)}{\delta}.$$

We write $X$'s PDF conditioned on $Y$ as

$$f_{X|Y}(x|y) = \lim_{\delta \rightarrow 0^+} \frac{\int_x^{x + \delta} f_{X, Y}(x, y)}{\delta f_Y(y)} = \frac{f_{X, Y}(x, y)}{f_Y(y)}.$$