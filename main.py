import sqlite3

# データベースとの接続を確立, Connectionオブジェクトを返す
con = sqlite3.connect("tutorial.db")

# データベースカーソルを作成
cur = con.cursor()

# CREATE TABLE文を実行
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

# resにSELECT文の結果を代入
res = cur.execute("SELECT name FROM sqlite_master") # sqlite_master: sqliteによって自動的に作成、管理される.データベース内の構造が管理されている

# 結果の行を取得
print(res.fetchone())

# 結果がない場合、Noneを返す
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)

# 接続を閉じる
con.close()