import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt(
    'C:\Users\debjy\PycharmProjects\pedometer_project\HMP_Dataset\Climb_stairs\Accelerometer-2011-03-24-10-24-39-climb_stairs-f1.txt')
x_data = data[:, 0]
y_data = data[:, 1]
z_data = data[:, 2]

noisy_x = -14.709 + (x_data / 63) * (2 * 14.709)
noisy_y = -14.709 + (y_data / 63) * (2 * 14.709)
noisy_z = -14.709 + (z_data / 63) * (2 * 14.709)

sampleNumb = len(x_data)
time = range(sampleNumb)


def find_peak(t, sig):
    peaks = []
    max_peak = -np.Inf
    n = len(sig)
    for i in range(0, n):
        if sig[i] > max_peak:
            max_peak = sig[i]
            position = t[i]
    peaks.append((position, max_peak))
    return np.array(peaks)


max_peaksX = find_peak(time, noisy_x)
max_peaksY = find_peak(time, noisy_y)
max_peaksZ = find_peak(time, noisy_z)

f, acc_data = plt.subplots(3, sharex=True)
f.suptitle('Accelerometer data')
acc_data[0].plot(time, noisy_x)
acc_data[0].scatter(max_peaksX[:, 0], max_peaksX[:, 1], color='red')
acc_data[1].plot(time, noisy_y)
acc_data[1].scatter(max_peaksY[:, 0], max_peaksY[:, 1], color='red')
acc_data[2].plot(time, noisy_z)
acc_data[2].scatter(max_peaksZ[:, 0], max_peaksZ[:, 1], color='red')
plt.show()
