import random
import pandas as pd
from scipy.stats import ks_2samp

# create a hypothetical P&L set of 250 days
dataset_size = 250
hypo = []
for i in range(dataset_size):
    hypo_obs = random.randrange(-2500000, 2500000)
    hypo.append(hypo_obs)

#calculate risk theoretical P&L value bases on hypo
rtpl = []
for i in range(len(hypo)):
    rtpl_obs = random.uniform(0.7,1.3) * hypo[i]
    rtpl.append(rtpl_obs)

#create Pandas dataframe
df = pd.DataFrame(list(zip(hypo, rtpl)), columns=['HYPO', 'RTPL'])

#calculate Spearman's correlation
sm_corr = df.corr(method='spearman')
print(f"Spearman's correlation equals {sm_corr}")

#calculate Kolmogorov-Smirnov test value
kolm_smir = ks_2samp(hypo, rtpl)
print(kolm_smir)


