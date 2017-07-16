## Gale-Shapley Stable Marriage algorithm

In the problem of stable marriages a stable matching between men and women is the aim, given the preferences of every man and woman. This project implements the Gale-Shapley algorithm.

The preferences are given via JSON format files. The files are in the following form:
```
{
  "men_rankings": {
    "abe": ["cat", "bea", "ada"],
    "bob": ["ada", "cat", "bea"],
    "cal": ["ada", "bea", "cat"]
  },

  "women_rankings": {
    "ada": ["abe", "cal", "bob"],
    "bea": ["bob", "abe", "cal"],
    "cat": ["cal", "abe", "bob"]
  }
}
```
