import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# Data
models = ['CARe', 'IC']
categories = ['Head', 'Middle', 'Tail']
care_scores = [63.33, 38.62, 25.09]
ic_scores = [69.53, 60.52, 45.79]
scores = np.array([care_scores, ic_scores])

# Create bar chart
bar_width = 0.25
r1 = np.arange(len(care_scores))
r2 = [x + bar_width for x in r1]
differences = [ic - care for ic, care in zip(ic_scores, care_scores)]

# plot the chart
fig, ax = plt.subplots(figsize=(7, 5))

# Plotting the bars again
bars1 = ax.bar(r1, care_scores, bar_width, label='CARe')
bars2 = ax.bar(r2, ic_scores, bar_width, label='IC')

# Adjusting x-tick labels to be centered between bars
ax.set_xticks([r + bar_width / 2 for r in range(len(care_scores))])

# Adding differences with "{" sign on the chart
for i, (r1_coord, r2_coord, diff) in enumerate(zip(r1, r2, differences)):
    x = (r1_coord + r2_coord) / 2
    y = sum([care_scores[i] * 2, ic_scores[i]]) / 3
    text = f'{diff:.2f}'
    if i == 0:
        xytext = (x-0.25, y+2.1)
    else:
        xytext = (x-0.4, y+4)
    ax.annotate("diff: \n" + text, xy =(x, y),
                color='red',
                xytext = xytext, 
                arrowprops = dict(color ='black', 
                                  width=1, 
                                  headlength=5, 
                                  headwidth=5, 
                                  shrink=True))

# Labeling
ax.set_xlabel('Segments')
ax.set_ylabel('mAP Score')
ax.set_title('Comparison of mAP scores for CARe and IC models')
ax.set_xticklabels(categories)
ax.legend()

# Display the updated plot
plt.tight_layout()
plt.savefig('LongTailResultComparison.pgf')
# plt.savefig('LongTailResultComparison.png', dpi=900)
# plt.show()