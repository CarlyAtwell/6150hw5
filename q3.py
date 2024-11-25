import numpy as np
import scipy

psize = 1e6

prob1 = 0.35
probneg = 0.4
prob0 = 0.25

pop_a = np.ones(int(psize*0.35), dtype = np.int8)
pop_b = np.full(int(psize*0.4), -1, dtype = np.int8)
pop_c = np.zeros(int(psize*0.25), dtype = np.int8)

population = np.concatenate([pop_a, pop_b, pop_c])
#print("santiy check: 1000000 = "+str(len(population)))

#sample_size = 10
#sample_size = 120
sample_size = 500

ismajority = np.zeros(200)
for i in range(200):
    sample = np.random.choice(population, sample_size, replace=False)
    if(int(scipy.stats.mode(sample)[0]) == -1):
        # -1 is majority
        ismajority[i] = 1

prob_majority = np.mean(ismajority)
print(prob_majority)