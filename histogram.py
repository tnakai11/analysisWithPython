# coding: utf-8

import pandas as pd # データの読み書きに使う
from matplotlib import pyplot as plt # グラフの描画に使う
from pathlib import Path # ファイル操作に使う

'''
メイン関数の処理
- iris.csv の sepal_length 列についてヒストグラムを描く

想定するディレクトリ構成
hoge/
├ histogram.py
└ source/
  └ iris.csv

参考URL
- https://pythondatascience.plavox.info/matplotlib/%E3%83%92%E3%82%B9%E3%83%88%E3%82%B0%E3%83%A9%E3%83%A0
- https://qiita.com/supersaiakujin/items/be4a78809e7278c065e6

'''

# 目的のファイルへのパスを作る
def get_source_file_path():
    file_dir_path = Path(__file__).parent 
    source_dir_path = file_dir_path / 'source' 
    source_file_path = source_dir_path / 'iris.csv' 
    return source_file_path

# 与えられた1次元データを使ってヒストグラムを描く
def draw_histogram(data):
    # キャンバスを得る
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    # ヒストグラムを描く
    ax.hist(data,bins=10,rwidth=0.9)

    # 見た目を整える
    ax.set_xlim([0,10]) # x軸の範囲を指定
    ax.set_ylim([0,30]) # y軸の範囲を指定
    ax.set_title('Sepal Length') # 図のタイトルを設定
    ax.set_xlabel('x') # x 軸のラベルを設定
    ax.set_ylabel('freq') # y 軸のラベルを設定

    # 描いたグラフを表示する
    plt.show()

# メイン関数
def main():
    # パスを得る
    source_file_path = get_source_file_path() 

    # ファイルを読み込む
    df = pd.read_csv(source_file_path, encoding='utf-8', header=0, index_col=None) 

    # データを抽出する
    label = 'sepal_length'
    data_sepal_length = df[label]

    # ヒストグラムを描く
    draw_histogram(data_sepal_length)

# デバッグ
def test():
    source_file_path = get_source_file_path() 
    df = pd.read_csv(source_file_path, encoding='utf-8', header=0, index_col=None) 
    print(df)
    
if __name__ == "__main__":
    main()
