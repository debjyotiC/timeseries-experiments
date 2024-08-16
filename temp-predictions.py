import os
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

zip_path = tf.keras.utils.get_file(
    origin='https://storage.googleapis.com/tensorflow/tf-keras-datasets/jena_climate_2009_2016.csv.zip',
    fname='jena_climate_2009_2016.csv.zip',
    extract=True)
csv_path, _ = os.path.splitext(zip_path)

df = pd.read_csv(csv_path)
df = df[5::6]
df.index = pd.to_datetime(df['Date Time'], format='%d.%m.%Y %H:%M:%S')
temp = df['T (degC)']


def df_to_xy(data_frame, window_size=5):
    df_np = data_frame.to_numpy()
    x, y = [], []
    for i in range(len(df_np) - window_size):
        data = [[a] for a in df_np[i:i + window_size]]
        label = df_np[i + window_size]
        x.append(data)
        y.append(label)

    return np.array(x), np.array(y)


WINDOW_SIZE = 5
x1, y1 = df_to_xy(temp, WINDOW_SIZE)
print(x1.shape)
print(y1.shape)
