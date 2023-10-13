# 実行方法: $python print_better.py
"""
出力例:
1: 上手
2: 一時
3: 市場
"""


import argparse


def main(args):
    with open("dictionary-data.txt", "r", encoding="utf-8") as f:
        print_all = args.id is None
        for i, row in enumerate(f): # 行ごとにファイルを読み込む
            row_num = i + 1 # i = 0, 1, 2 ...より現在の行には i + 1 が必要
            if (not print_all) and (row_num != int(args.id)):
                continue
            print(f'{row_num}: {row}', end="") # 行数: 内容 で出力

if __name__ == "__main__":
    parser = argparse.ArgumentParser() # descriptionは必要に応じて書くこと

    parser.add_argument("id", help="行数の指定", nargs="?")

    args = parser.parse_args()
    main(args)