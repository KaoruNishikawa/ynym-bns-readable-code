# 実行方法: $python print_better.py
"""
出力例:
1: 上手 じょうず
2: 一時 いちじ
3: 市場 しじょう
"""


import argparse


def print_dict(file, user, idx, start_idx=0):
    with open(file, "r", encoding="utf-8") as f:
        print(f"ユーザー名: {user}")
        print_all = idx is None
        for i, row in enumerate(f): # 行ごとにファイルを読み込む
            row_num = start_idx + i + 1 # i = 0, 1, 2 ...より現在の行には i + 1 が必要
            if (not print_all) and (row_num != int(idx)):
                continue
            print(f'{row_num}: {row}', end="") # 行数: 内容 で出力
    return i


def main(args):
    if len(args.file) == len(args.user):
        next_idx = 0
        for file, user in zip(args.file, args.user):
            last_idx = print_dict(file, user, args.id, next_idx)
            next_idx += last_idx + 1  # インデックスが重複しないように次の開始行を更新
            print("")  # 空行を出力
    else:
        print(f"ファイル名とユーザー名の数が一致しません：{args.file=} {args.user=}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser() # descriptionは必要に応じて書くこと

    parser.add_argument("id", help="行数の指定", nargs="?")
    parser.add_argument(
        "--file",
        "-f",
        help="ファイル名の指定",
        default=[],
        action="append",
    )
    parser.add_argument(
        "--user", "-u", help="ユーザー名の指定", default=[], action="append"
    )

    args = parser.parse_args()
    main(args)