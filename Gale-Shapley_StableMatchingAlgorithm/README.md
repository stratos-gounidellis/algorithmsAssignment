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
The algorithm runs with the following ways:

  - `python3 stable_marriage.py -m <input_filename>`, which prints the optimal solution for men. The program creates as output a JSON file with following form `{ "man": "woman", "another_man": "another_woman", ...}`.
  * `python3 stable_marriage.py -m <input_filename> -o <output_filename>`, which prints the optimal solution for men. The solution is saved in the `output_filename`.
  * `python3 stable_marriage.py -w <input_filename>`, which prints the optimal solution for women. The program creates as output a JSON file with following form `{ "woman": "man", "another_woman": "another_man", ...}`.
  * `python3 stable_marriage.py -w <input_filename> -o <output_filename>`, which prints the optimal solution for women. The solution is saved in the `output_filename`.
