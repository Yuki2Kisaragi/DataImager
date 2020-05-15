# -*-coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import cv2
import numpy
import argparse
import sys

# ToDO:コマンドライン引数でモード選択、
# ToDo：訓練データor検証データ
# ToDo：ラベル名選択
# ToDo：記録時間設定
# ToDo：イメージサイズ指定
# ToDo:データセットの一覧ファイル(csv or txt)を作成する
#


parser = argparse.ArgumentParser()

# 引数作成
parser.add_argument("list", help="make csv or txt file as datasets list", action="store_true")
parser.add_argument("cap", help="capture dataset", action="store_true")
parser.add_argument("size", type=tuple, help="data size")

args = parser.parse_args()

if args.list:
    print("make dataset file")
elif args.cap:
    print("Capture dataset")
else:
    pass
