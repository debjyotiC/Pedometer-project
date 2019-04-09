import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import csv file
df = pd.read_csv('C:\Users\debjy\PycharmProjects\pedometer_project\datasets\data_3.csv')
x_axis = np.array(df['X'])
y_axis = np.array(df['Y'])
z_axis = np.array(df['Z'])
time_line = np.array(df['Milliseconds'])

peaks = []
thres = []
spikes = []
spike_counter = 0
acc_vector = np.sqrt(np.square(x_axis) + np.square(y_axis) + np.square(z_axis))
miliV = (acc_vector / 36.73)
threshold = miliV.sum()/len(miliV)

for itr_a in range(len(miliV)):
    thres.append(threshold)
    if float(miliV[itr_a]) > threshold:
        peaks.append(1)
    else:
        peaks.append(0)

zeros = np.zeros(len(peaks)-1)

for itr_b in range(len(peaks)-1):
    if peaks[itr_b] > peaks[itr_b+1]:
        spikes.append(1)
    else:
        spikes.append(0)


values = {'Time': time_line[:-1], 'Vector': miliV[:-1], 'Threshold': thres[:-1], 'Peaks': peaks[:-1], 'Spikes': spikes}
df_w = pd.DataFrame(values, columns=['Time', 'Vector', 'Threshold', 'Peaks', 'Spikes'])
df_w.to_csv("datasets/data_3_results.csv", index=None, header=True)

fig, axs = plt.subplots(3, 1)
axs[0].plot(time_line, miliV, color='Green')
axs[0].plot(time_line, np.array(thres), color='Red', linestyle=':')
axs[0].set_xlabel('time (millisecond)')
axs[0].set_ylabel('Acc. vector data (mV)')
axs[0].grid(True)

axs[1].plot(time_line, np.array(peaks), color='Red')
axs[1].set_xlabel('time (millisecond)')
axs[1].set_ylabel('Detected Peaks')
axs[1].grid(True)

axs[2].plot(time_line[:-1], np.array(spikes), color='Blue')
axs[2].set_xlabel('time (millisecond)')
axs[2].set_ylabel('Step spikes')
axs[2].grid(True)
# fig.tight_layout()
plt.show()
