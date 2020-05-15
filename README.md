# DataImager


# DEMO


# Features
* PC内蔵カメラ 又は Webカメラでデータセット用のデータセットが作れる
* 複数の引数でラベリング済みデータセットを作成できる
* 

# Requirement
* Python        3.7.5
* numpy         1.18.4
* opencv-python 4.2.0.34

# Installation

```bash
sudo apt install python==3.7.5
pip install numpy==1.18.4
pip install opencv-python==4.2.0.34
```

# Usage
```bash
git clone https://github.com/hoge/~
```

1) For example 

If you want to make dataset for "Recognition Rock-paper-scissors" ,

at first making "Rock" test data ...
```bash
$ python dataimager.py datatype=train label="Rock" timer=30 size=(500,500) 
$ cd train
$ ls
rock0001.jpg
rock0002.jpg
rock0003.jpg
rock0004.jpg
 .
 .
 .
```

# Note

# Author

* Masahiro Shimono

# License
