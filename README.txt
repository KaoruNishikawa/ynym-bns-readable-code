---使用方法---
1. リポジトリのクローンを行う
$ git clone https://github.com/ynym-bns/ynym-bns-readable-code

2. プログラムを実行する
python main.py

2.1 一部の単語のみ出力する
# 単語ID=1の単語のみ出力
python main.py 1
※ 存在しない単語IDを指定した場合は、何も出力されない

2.2 ユーザー名を紐づける (-u オプション)
# ユーザー名=太郎さんとする
python main.py -u 太郎

2.3 データファイルを指定して読み込む (-f オプション)
# ファイル名=dictionary-data.txtとする
python main.py -f dictionary-data.txt -u 太郎
※ ファイル名には必ずユーザー名を紐づける必要がある

2.4 複数のデータファイルを読み込む (-u オプションと -f オプションを繰り返し使う)
# 太郎さんの辞書 taro.txt と次郎さんの辞書 jiro.txt を読み込む
python main.py -f taro.txt -u 太郎 -f jiro.txt -u 次郎
※ -f taro.txt -u 太郎 -u 次郎 -f jiro.txt のような順番でも読み込める。
　ただし -f taro.txt -u 次郎 -u 太郎 -f jiro.txt のように、ファイルとユーザーの順番を入れ替えて指定
　すると、辞書とユーザー名の紐づけが不正確になる。

---データファイル(dictionary-data.txt)について---
・保存されている単語は 上手、一時、市場
・それぞれの単語について、単語そのものと読み仮名が保存されている。
　これらの情報は半角スペースで区切られている。
