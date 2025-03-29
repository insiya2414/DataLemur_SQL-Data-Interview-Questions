# Expected Value of Min(X, Y)

We have two independent random numbers, **X** and **Y**, both from **Uniform(0,1)**.  
We want to find the expected value of **min(X, Y)**.

## Step 1: Think About the Probability

For any number $z$, the minimum of $X$ and $Y$ is **less than or equal to $z$** if at least one of them is less than $z$

Since $X$ and $Y$ are independent, the probability that both are **greater than $z$** is:

$$
P(X > z) \times P(Y > z) = (1 - z) \times (1 - z) = (1 - z)^2
$$

So, the probability that at least one is **less than or equal to $z$** is:

$$
P(\min(X, Y) \leq z) = 1 - (1 - z)^2
$$

## Step 2: Find the Expected Value

The expected value formula is:

$$
E[\min(X, Y)] = \int_0^1 z f_Z(z) dz
$$

We first find the probability density function (PDF):

$$
f_Z(z) = \frac{d}{dz} (1 - (1 - z)^2) = 2(1 - z)
$$

Now, we calculate:

$$
E[Z] = \int_0^1 z \cdot 2(1 - z) dz
$$

Expanding:

$$
= 2 \int_0^1 (z - z^2) dz
$$

Solving each integral:

$$
= 2 \left[ \frac{z^2}{2} - \frac{z^3}{3} \right]_0^1
$$

$$
= 2 \left( \frac{1}{2} - \frac{1}{3} \right)
$$

$$
= 2 \times \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
$$

## Final Answer:

$$
E[\min(X, Y)] = \frac{1}{3}
$$

So, the expected minimum of two random numbers between **0 and 1** is **1/3**! 🎉
