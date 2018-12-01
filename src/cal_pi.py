# %%
import numpy as np


def cal_pi(max_rand=10000, trial=1000):
    """calculate PI using probability

    Args:

        max_rand (long): max random number. In theory, the bigger the better estimation
        trial(int): number of times to repeat

    Returns:
        pi (double): estimated PI value
    """
    result = np.empty(trial)
    for i in range(1000):
        r1 = np.random.randint(1, high=max_rand, size=trial)
        r2 = np.random.randint(1, high=max_rand, size=trial)
        coprime = np.gcd(r1, r2)
        coprime_count = np.isin(coprime, 1)
        result[i] = np.sqrt(6/(sum(coprime_count)/trial))

    return np.mean(result)
