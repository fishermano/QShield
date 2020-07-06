import pylab
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.pyplot import MultipleLocator
import numpy as np
import math

title_font = {'family' : 'Times New Roman',
'weight' : 'bold',
'size' : 8,
}

legend_font = {'family' : 'Times New Roman',
'weight' : 'bold',
'size' : 6,
}

label_font = {'family' : 'Times New Roman',
'weight' : 'bold',
'size' : 7.5,
}

def to_ms(x):
    y = float(x) * 1000
    return y

def to_log(x):
	y = math.log(x, 10)
	return y

def load_data(f_n):
    file = open(f_n, 'r')
    return file.readline()

opaque_big_q1 = to_ms(load_data('./exp_res/opaque/res/big/q1_mean.txt'))
opaque_big_q2 = to_ms(load_data('./exp_res/opaque/res/big/q2_mean.txt'))
opaque_big_q3 = to_ms(load_data('./exp_res/opaque/res/big/q3_mean.txt'))
opaque_big = [opaque_big_q1, opaque_big_q2, opaque_big_q3]
opaque_big_log = list(map(to_log, opaque_big))
opaque_medium_q1 = to_ms(load_data('./exp_res/opaque/res/medium/q1_mean.txt'))
opaque_medium_q2 = to_ms(load_data('./exp_res/opaque/res/medium/q2_mean.txt'))
opaque_medium_q3 = to_ms(load_data('./exp_res/opaque/res/medium/q3_mean.txt'))
opaque_medium = [opaque_medium_q1, opaque_medium_q2, opaque_medium_q3]
opaque_medium_log = list(map(to_log, opaque_medium))
opaque_tiny_q1 = to_ms(load_data('./exp_res/opaque/res/tiny/q1_mean.txt'))
opaque_tiny_q2 = to_ms(load_data('./exp_res/opaque/res/tiny/q2_mean.txt'))
opaque_tiny_q3 = to_ms(load_data('./exp_res/opaque/res/tiny/q3_mean.txt'))
opaque_tiny = [opaque_tiny_q1, opaque_tiny_q2, opaque_tiny_q3]
opaque_tiny_log = list(map(to_log, opaque_tiny))

qshield_big_q1 = to_ms(load_data('./exp_res/qshield/res/big/q1_mean.txt'))
qshield_big_q2 = to_ms(load_data('./exp_res/qshield/res/big/q2_mean.txt'))
qshield_big_q3 = to_ms(load_data('./exp_res/qshield/res/big/q3_mean.txt'))
qshield_big = [qshield_big_q1, qshield_big_q2, qshield_big_q3]
qshield_big_log = list(map(to_log, qshield_big))
qshield_medium_q1 = to_ms(load_data('./exp_res/qshield/res/medium/q1_mean.txt'))
qshield_medium_q2 = to_ms(load_data('./exp_res/qshield/res/medium/q2_mean.txt'))
qshield_medium_q3 = to_ms(load_data('./exp_res/qshield/res/medium/q3_mean.txt'))
qshield_medium = [qshield_medium_q1, qshield_medium_q2, qshield_medium_q3]
qshield_medium_log = list(map(to_log, qshield_medium))
qshield_tiny_q1 = to_ms(load_data('./exp_res/qshield/res/tiny/q1_mean.txt'))
qshield_tiny_q2 = to_ms(load_data('./exp_res/qshield/res/tiny/q2_mean.txt'))
qshield_tiny_q3 = to_ms(load_data('./exp_res/qshield/res/tiny/q3_mean.txt'))
qshield_tiny = [qshield_tiny_q1, qshield_tiny_q2, qshield_tiny_q3]
qshield_tiny_log = list(map(to_log, qshield_tiny))

cryptdb_big_q1 = to_ms(load_data('./exp_res/cryptdb/res/big/q1_mean.txt'))
cryptdb_big_q2 = to_ms(load_data('./exp_res/cryptdb/res/big/q2_mean.txt'))
cryptdb_big_q3 = to_ms(load_data('./exp_res/cryptdb/res/big/q3_mean.txt'))
cryptdb_big = [cryptdb_big_q1, cryptdb_big_q2, cryptdb_big_q3]
cryptdb_big_log = list(map(to_log, cryptdb_big))
cryptdb_medium_q1 = to_ms(load_data('./exp_res/cryptdb/res/medium/q1_mean.txt'))
cryptdb_medium_q2 = to_ms(load_data('./exp_res/cryptdb/res/medium/q2_mean.txt'))
cryptdb_medium_q3 = to_ms(load_data('./exp_res/cryptdb/res/medium/q3_mean.txt'))
cryptdb_medium = [cryptdb_medium_q1, cryptdb_medium_q2, cryptdb_medium_q3]
cryptdb_medium_log = list(map(to_log, cryptdb_medium))
cryptdb_tiny_q1 = to_ms(load_data('./exp_res/cryptdb/res/tiny/q1_mean.txt'))
cryptdb_tiny_q2 = to_ms(load_data('./exp_res/cryptdb/res/tiny/q2_mean.txt'))
cryptdb_tiny_q3 = to_ms(load_data('./exp_res/cryptdb/res/tiny/q3_mean.txt'))
cryptdb_tiny = [cryptdb_tiny_q1, cryptdb_tiny_q2, cryptdb_tiny_q3]
cryptdb_tiny_log = list(map(to_log, cryptdb_tiny))

fig = plt.figure(figsize=(8, 2))
gs = gridspec.GridSpec(nrows=1, ncols=3)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[0,1])
ax3 = fig.add_subplot(gs[0,2])

bar_width=0.2
x_l=['Q1', 'Q2', 'Q3']
x=np.arange(len(x_l))

ax1.set_title(r'Tiny Dataset', title_font)
ax1.grid(linestyle='-.', axis='y', zorder=1)
ax1.bar(x, opaque_tiny_log, width=bar_width, label='Opaque', color='seagreen', edgecolor='white', linewidth=0.5, zorder=2)
ax1.bar(x + bar_width, qshield_tiny_log, width=bar_width, label='QShield', color='goldenrod', edgecolor='white', linewidth=0.5, zorder=2)
ax1.bar(x + 2*bar_width, cryptdb_tiny_log, width=bar_width, label='CryptDB', color='slategrey', edgecolor='white', linewidth=0.5, zorder=2)
ax1.set_xticks(x+bar_width)
ax1.set_xticklabels(x_l)
ax1.set(ylim=[0,5])
ax1.xaxis.set_minor_locator(MultipleLocator(bar_width))
ax1.tick_params(labelsize=7.5)
labels = ax1.get_xticklabels() + ax1.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
ax1.legend(frameon=True, prop=legend_font)
ax1.set_ylabel('Logarithmic Time (ms)', label_font)

ax2.set_title(r'Medium Dataset', title_font)
ax2.grid(linestyle='-.', axis='y', zorder=1)
ax2.bar(x, opaque_medium_log, width=bar_width, label='Opaque', color='seagreen', edgecolor='white', linewidth=0.5, zorder=2)
ax2.bar(x + bar_width, qshield_medium_log, width=bar_width, label='QShield', color='goldenrod', edgecolor='white', linewidth=0.5, zorder=2)
ax2.bar(x + 2*bar_width, cryptdb_medium_log, width=bar_width, label='CryptDB', color='slategrey', edgecolor='white', linewidth=0.5, zorder=2)
ax2.set_xticks(x+bar_width)
ax2.set_xticklabels(x_l)
ax2.set(ylim=[0,5])
ax2.xaxis.set_minor_locator(MultipleLocator(bar_width))
ax2.tick_params(labelsize=7.5)
labels = ax2.get_xticklabels() + ax2.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
ax2.legend(frameon=True, prop=legend_font)
ax2.set_xlabel('Benchmark Query Type', label_font)

ax3.set_title(r'Big Dataset', title_font)
ax3.grid(linestyle='-.', axis='y', zorder=1)
ax3.bar(x, opaque_big_log, width=bar_width, label='Opaque', color='seagreen', edgecolor='white', linewidth=0.5, zorder=2)
ax3.bar(x + bar_width, qshield_big_log, width=bar_width, label='QShield', color='goldenrod', edgecolor='white', linewidth=0.5, zorder=2)
ax3.bar(x + 2*bar_width, cryptdb_big_log, width=bar_width, label='CryptDB', color='slategrey', edgecolor='white', linewidth=0.5, zorder=2)
ax3.set_xticks(x+bar_width)
ax3.set_xticklabels(x_l)
ax3.set(ylim=[0,5])
ax3.xaxis.set_minor_locator(MultipleLocator(bar_width))
ax3.tick_params(labelsize=7.5)
labels = ax3.get_xticklabels() + ax3.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]
ax3.legend(frameon=True, prop=legend_font)

plt.tight_layout()
plt.show()