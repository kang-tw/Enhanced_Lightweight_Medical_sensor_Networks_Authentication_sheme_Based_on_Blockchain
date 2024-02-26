import numpy as np
import matplotlib.pyplot as plt

# Data
schemes = ["Wu et al.", "Li et al.", "Fotouhi et al.", "Wang et al.", "Yu et al.", "Our Scheme"]
mp = np.array([800, 800, 720, 656, 576, 608])
gwn = np.array([1360, 1280, 1680, 1024, 1216, 1312])
s = np.array([320, 640, 480, 496, 576, 512])
total_costs = np.array([2480, 2720, 2880, 2176, 2368, 2432])


colors = ['#DDE6ED', '#9DB2BF', '#526D82', '#27374D']


# Number of schemes
n_schemes = len(schemes)

# Setting the positions for the bars
index = np.arange(n_schemes)
bar_width = 0.2

# Creating the bar plot
plt.figure(figsize=(12, 6))

plt.bar(index, mp, bar_width, alpha=0.7, label='MP',color=colors[0])
plt.bar(index + bar_width, gwn, bar_width, alpha=0.7, label='GWN',color=colors[1])
plt.bar(index + 2*bar_width, s, bar_width, alpha=0.7, label='S',color=colors[2])
plt.bar(index + 3*bar_width, total_costs, bar_width, alpha=0.7, label='Total Costs',color=colors[3])




plt.xlabel('Scheme',fontsize = 26)
plt.ylabel('Communication Costs (bits)',fontsize=26)
plt.xticks(index + 1.5*bar_width, schemes,fontsize=18)
plt.legend(loc='best',fontsize=16)
plt.grid(which='major', axis='y', linestyle='--')
plt.ylim(0,3000)
plt.tight_layout()
plt.show()