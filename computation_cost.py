import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# 각 Scheme의 이름과 비용 데이터
schemes = ["Wu et al.", "Li et al.", "Fotouhi et al.", "Wang et al.", "Yu et al.", "Our Scheme"]
mp_costs = [99, 1887 + 72, 108, 54, 81, 102]
gwn_costs = [153, 72+628, 198, 36, 81, 110]
s_costs = [54, 36+1256, 63, 27, 63, 82]
total_costs = [306, 3948,369,117,225,294]

mp_costs = [x / 1000 for x in mp_costs]
gwn_costs = [x / 1000 for x in gwn_costs]
s_costs = [x / 1000 for x in s_costs]
total_costs = [x / 1000 for x in total_costs]


# X 좌표
x = np.arange(len(schemes))

colors = ['#DDE6ED', '#9DB2BF', '#526D82', '#27374D']


# MP, GWN, S, Total cost를 따로 표현하는 그래프
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [2, 3]})



bar_width = 0.2

ax2.bar(x - 1.5 * bar_width, mp_costs, width=bar_width, label="MP", alpha=0.7,color=colors[0])
ax2.bar(x - 0.5 * bar_width, gwn_costs, width=bar_width, label="GWN", alpha=0.7,color=colors[1])
ax2.bar(x + 0.5 * bar_width, s_costs, width=bar_width, label="S", alpha=0.7,color=colors[2])
ax2.bar(x + 1.5 * bar_width, total_costs, width=bar_width, label="Total", alpha=0.7,color=colors[3])






# Total cost만 따로 표현하는 그래프

ax1.bar(x - 1.5 * bar_width, mp_costs, width=bar_width, label="MP", alpha=0.7,color=colors[0])
ax1.bar(x - 0.5 * bar_width, gwn_costs, width=bar_width, label="GWN", alpha=0.7,color=colors[1])
ax1.bar(x + 0.5 * bar_width, s_costs, width=bar_width, label="S", alpha=0.7,color=colors[2])
ax1.bar(x + 1.5 * bar_width, total_costs, width=bar_width, label="Total", alpha=0.7,color=colors[3])

# X 축 레이블 설정
ax1.set_xticks([])
ax2.set_xticks(x)
ax2.set_xticklabels(schemes,fontsize =14)

# 아래 그래프의 위쪽 그리드 지우기
ax2.spines['top'].set_visible(False)

# 위쪽 그래프의 아래쪽 그리드 지우기
ax1.spines['bottom'].set_visible(False)
ax1.xaxis.tick_top()
ax1.tick_params(labeltop=False)



ax1.set_yticks(np.arange(1.5, 4.51, 1))
ax2.set_yticks(np.arange(0, 0.49, 0.1))

ax1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.3f'))

ax1.set_ylim(1.2, 5)
ax2.set_ylim(0, 0.5)
ax2.set_xlabel("Schemes",fontsize = 22)
handles, labels = ax1.get_legend_handles_labels()
ax1.legend(handles[0:4], labels[0:4], loc='best',prop={'size':16})

ax1.yaxis.grid(True, linestyle='--', alpha=1)
ax2.yaxis.grid(True, linestyle='--', alpha=1)


plt.tight_layout()
plt.show()