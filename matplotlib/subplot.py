import numpy as np
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LW = 1.5
eLW = 0.8
nb = 450
num_players = 2

def plot(ax, data_dir, title, annotations):

    def process(arr):
        ln = len(arr)
        x, y, stderr = [], [], []
        for i in range(0, ln-10, 10):
            x.append(i+5)
            y.append(np.mean(arr[i:i+10]))
            stderr.append(np.std(arr[i:i+10]))

        return x, y, stderr


    ax.set_title(title)
    ax.set_ylabel('Original reward received in a single game')
    ax.set_xlabel('Episode')

    line = []
    if os.path.exists(os.path.join(data_dir, 'ori_history.npz')):
        ori_history = np.load(os.path.join(data_dir, 'ori_history.npz'))['arr_0']
        for i in range(num_players):
            x, y, stderr = process(ori_history[i][:nb])
            line.append(ax.errorbar(x, y, yerr=stderr, marker='.', lw=LW, elinewidth=eLW, errorevery=3, capsize=2, markersize=5))

    ax.legend(line, annotations)



tot = len(sys.argv) - 1
f, ax = plt.subplots(1, 2, sharey=True)
plot(ax[0], sys.argv[1], 'Original', ['player_0', 'player_1'])
plot(ax[1], sys.argv[2], 'Step Function', ['player_0', 'player_1'])
plt.tight_layout()
plt.savefig('result.png')
