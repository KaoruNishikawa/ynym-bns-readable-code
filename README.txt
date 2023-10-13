---使用方法---
1. リポジトリのクローンを行う
$ git clone https://github.com/ynym-bns/ynym-bns-readable-code

2. プログラムを実行する
python main.py

2.1 一部の単語のみ出力する
# 単語ID=1の単語のみ出力
python main.py 1
※ 存在しない単語IDを指定した場合は、何も出力されない

2.2 ユーザー名を紐づける
# ユーザー名=太郎さんとする
python main.py -u 太郎

---データファイル(dictionary-data.txt)について---
・保存されている単語は 上手、一時、市場
・それぞれの単語について、単語そのものと読み仮名が保存されている。
　これらの情報は半角スペースで区切られている。
