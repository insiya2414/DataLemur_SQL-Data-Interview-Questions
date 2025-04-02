# Probability of Being a "Lazy" Rater

We use **Bayes' Theorem**, which states:

$$
P(A | B) = \frac{P(B | A) P(A)}{P(B)}
$$

where:
- \( A \) is the event that a user is "lazy."
- \( B \) is the event that the user gives **3 thumbs up in a row**.

## Step 1: Define Given Probabilities
- **80% of users are normal**: \( P(N) = 0.8 \).
- **20% of users are lazy**: \( P(L) = 0.2 \).
- **Normal users rate thumbs up 60% of the time**.
- **Lazy users rate thumbs up 100% of the time**.

## Step 2: Compute Likelihoods
- If a normal user rates a movie, the probability of them giving **3 thumbs up in a row** is:

  $$
  P(B | N) = (0.6)^3 = 0.216
  $$

- If a lazy user rates a movie, they **always** give thumbs up:

  $$
  P(B | L) = 1
  $$

## Step 3: Compute \( P(B) \), the Total Probability of 3 Thumbs Up
Using the Law of Total Probability:

$$
P(B) = P(B | N) P(N) + P(B | L) P(L)
$$

$$
P(B) = (0.216 \times 0.8) + (1 \times 0.2)
$$

$$
P(B) = 0.1728 + 0.2 = 0.3728
$$

## Step 4: Apply Bayes' Theorem

$$
P(L | B) = \frac{P(B | L) P(L)}{P(B)}
$$

$$
P(L | B) = \frac{(1 \times 0.2)}{0.3728}
$$

$$
P(L | B) \approx \frac{0.2}{0.3728} \approx 0.5367
$$

## Conclusion
The probability that a user is **lazy**, given that they rated **3 movies in a row** with a thumbs up, is **53.67%**.
