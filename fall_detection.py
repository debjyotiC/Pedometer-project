import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

# Import csv file
df = pd.read_csv('datasets/acc_fall.csv')
x_axis = np.array(df['X'])
y_axis = np.array(df['Y'])
z_axis = np.array(df['Z'])
time_line = np.array(df['Milliseconds'])

acc_vector = np.sqrt(np.square(x_axis) + np.square(y_axis) + np.square(z_axis))
theta = np.arctan(np.sqrt(np.square(y_axis)+np.square(z_axis))/x_axis)*(180/math.pi)
a_gsvm = (theta/90)*acc_vector
fall_mag = acc_vector-a_gsvm
threshold = fall_mag.sum()/len(fall_mag)
print threshold
values = {'Time': time_line, 'Vector': acc_vector, 'A_GSVM': a_gsvm, 'Fall mag':fall_mag, 'Theta': theta}
df_w = pd.DataFrame(values, columns=['Time', 'Vector', 'A_GSVM', 'Fall mag','Theta'])
df_w.to_csv("datasets/results_fall.csv", index=None, header=True)


fig, axs = plt.subplots(3, 1)
axs[0].plot(time_line, acc_vector, color='Green')
axs[0].plot(time_line, a_gsvm, color='Red')
axs[0].set_xlabel('time (millisecond)')
axs[0].set_ylabel('Acc. vector data (mV)')
axs[0].grid(True)

axs[1].plot(time_line, fall_mag, color='Red')
axs[1].plot(time_line, np.full(len(time_line),100), color='black', linestyle=':')
axs[1].set_xlabel('time (millisecond)')
axs[1].set_ylabel('Acc. vector data (mV)')
axs[1].grid(True)

axs[2].plot(time_line, theta, color='Red')
axs[2].set_xlabel('time (millisecond)')
axs[2].set_ylabel('Degree')
axs[2].grid(True)



# fig.tight_layout()
plt.show()
