import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#学習モデル
df = pd.read_csv('sample.csv')
mean = df.mean()
xa = df['x']
yb = df['y']
df_c = df - df.mean()
xa = df_c['x']
yb = df_c['y']
xx = xa * xa
xy = xa * yb

def predict(x):
    #予測
    a = xy.sum()/xx.sum()
    xm = mean['x']
    ym = mean['y']
    # 中心化
    xc = x - xm
    y_hat = a*xc+ym
    #出力
    return y_hat

print('部屋の広さを入力してください')
room = input('>>')
room = int(room)
print(predict(room))
