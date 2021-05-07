# coding: utf-8

import pandas as pd # データの読み書きに使う
from pathlib import Path # ファイル操作に使う
from sklearn.neighbors import KNeighborsClassifier # K-neighbors 法の分類器を作るのに使う

'''
メイン関数の処理
- iris.csv の sepal_length 列, petal_length に注目して k-neighbors 法による分類を行う

想定するディレクトリ構成
hoge/
├ k_neighbors.py
└ source/
  └ iris.csv

参考URL
- https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

'''

# 目的のファイルへのパスを作る
def get_source_file_path():
    file_dir_path = Path(__file__).parent 
    source_dir_path = file_dir_path / 'source' 
    source_file_path = source_dir_path / 'iris.csv' 
    return source_file_path

# メイン関数
def main():
    # パスを得る
    source_file_path = get_source_file_path() 

    # ファイルを読み込む
    df = pd.read_csv(source_file_path, encoding='utf-8', header=0, index_col=None) 

    # データを抽出する
    label = ['sepal_length','petal_length']
    X = df[label]
    y = df['species']

    # 抽出したデータを訓練データとテストデータに分割する
    X_train = X[:-1]
    y_train = y[:-1]
    X_test = X[-2:-1]
    y_test = y[-2:-1]

    # 分類器を呼び出す
    neigh = KNeighborsClassifier(n_neighbors=5)

    # 分類器に訓練データを食わせて学習完了
    neigh.fit(X_train,y_train)

    # テストデータを表示
    print('X_test:')
    print(X_test)
    print('y_test:')
    print(y_test)

    # テストデータの推定結果を表示
    print("predict:", neigh.predict(X_test))

# デバッグ
def test():
    source_file_path = get_source_file_path() 
    df = pd.read_csv(source_file_path, encoding='utf-8', header=0, index_col=None) 
    print(df)
    
if __name__ == "__main__":
    main()
