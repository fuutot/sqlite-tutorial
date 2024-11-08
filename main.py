import sqlite3

# データベースとの接続を確立, Connectionオブジェクトを返す
con = sqlite3.connect("tutorial.db")

# データベースカーソルを作成
cur = con.cursor()

# movieが存在する場合、削除
cur.execute("DROP TABLE IF EXISTS movie")

# CREATE TABLE文を実行
cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

# resにSELECT文の結果を代入
res = cur.execute("SELECT name FROM sqlite_master") # sqlite_master: sqliteによって自動的に作成、管理される.データベース内の構造が管理されている

# 結果の行を取得
print(res.fetchone()) # tuple型

# 結果がない場合、Noneを返す
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
print(res.fetchone() is None)

# データを挿入、トランザクションが開かれる
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
# トランザクションをコミットする
con.commit()

res = cur.execute("SELECT * FROM movie")

print(res.fetchall()) # list[tuple]型

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
# プレイスホルダーを利用したバインディング SQLインジェクションに対応するため、以下のように行う
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()

# for文で反復処理
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row) # tuple型

# 接続を閉じる
con.close()


# 新しく接続を確立
new_con = sqlite3.connect("tutorial.db")
# データベースカーソルを作成
new_cur = new_con.cursor()
# スコアでソート
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
# 一番大きいものを取得
title, year = res.fetchone()

print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
new_con.close()