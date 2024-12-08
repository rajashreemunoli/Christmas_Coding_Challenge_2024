#This program calculates the probability of Heads for given number of simulations of 100 coinflips

import numpy as np
np.random.seed(seed=42)
rng=np.random.default_rng()
number_of_flips=100
number_of_simulations=1000
heads_probabilities_array=[]

def simulate_flips(nflips,nsimulations):
    for _ in range(nsimulations):
        flips=rng.binomial(1, 0.5, nflips)
        heads_probabilities_per_event=np.sum(flips)/nflips
        heads_probabilities_array.append(heads_probabilities_per_event)
    return heads_probabilities_array

head_probability=np.mean(simulate_flips(number_of_flips,number_of_simulations))*100

print(f"Probabiliy of Heads for {number_of_simulations} simulations of {number_of_flips} coin flips is :\n {head_probability:.1f}%")