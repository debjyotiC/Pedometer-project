# accelerometer auto calibration tool

import pandas as pd
import serial
import time
import numpy as np

acc_data = []

ser = serial.Serial('COM7', 9600)  # open serial port
for pos in range(6):        # loop for 6 accelerometer position
    time.sleep(5)
    print 'Data for position ' + str(pos) + ' collected'
    for i in range(10):     # loop to collect 10 acc. data sample
        dataRead = ser.readline()
        acc_data.append(dataRead.split('\t'))
        x_axis = np.array(acc_data[0][0]).astype(np.float)
        y_axis = np.array(acc_data[0][1]).astype(np.float)
        z_axis = np.array(acc_data[0][2]).astype(np.float)
    x_data = x_axis.mean()  # calculate mean of acc. data
    y_data = y_axis.mean()
    z_data = z_axis.mean()
    # flush data to a CSV file
    data = {'x_axis': [x_data], 'y_axis': [y_data], 'z_axis': [z_data]}
    df = pd.DataFrame(data, index=range(pos+1)).to_csv('data.csv')

df_acc_data = pd.read_csv('data.csv')

a_x_0 = df_acc_data['x_axis'].mean()
k_ax = (df_acc_data['x_axis'][0]-df_acc_data['x_axis'][1])/2
s_ax_1 = (df_acc_data['x_axis'][2]-df_acc_data['x_axis'][3])/2
s_ax_2 = (df_acc_data['x_axis'][4]-df_acc_data['x_axis'][5])/2

a_y_0 = df_acc_data['y_axis'].mean()
s_ay_1 = (df_acc_data['y_axis'][0]-df_acc_data['y_axis'][1])/2
k_ay = (df_acc_data['y_axis'][2]-df_acc_data['y_axis'][3])/2
s_ay_2 = (df_acc_data['y_axis'][4]-df_acc_data['y_axis'][5])/2

a_z_0 = df_acc_data['z_axis'].mean()
s_az_1 = (df_acc_data['z_axis'][1]-df_acc_data['z_axis'][2])/2
s_az_2 = (df_acc_data['z_axis'][2]-df_acc_data['z_axis'][3])/2
k_az = (df_acc_data['z_axis'][4]-df_acc_data['z_axis'][5])/2


installation_matrix = [[k_ax, s_ax_1, s_ax_2],
                       [s_ay_1, k_ay, s_ax_2],
                       [s_az_1, s_az_2, k_az]]

bias_matrix = [a_x_0, a_y_0, a_z_0]

print installation_matrix, bias_matrix
