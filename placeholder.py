import sqlite3

con = sqlite3.connect("tutorial.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS user")
cur.execute("CREATE TABLE user(userid, username, password)")
data = [
    (1, "one", "samplepassword1"),
    (2, "two", "samplepassword2"),
    (3, "theree", "samplepassword3"),
]
cur.executemany("INSERT INTO user VALUES(?, ?, ?)", data)
con.commit()

# フォーマット文を使ってpythonの値をSQLに組み込む
username_input = "' OR '1'='1"
sql = f"SELECT * FROM user WHERE username = '{username_input}';"
print(sql)
print("format文 version")
# 実行、結果を出力
print(cur.execute(sql).fetchall())

con.close()

# クエリ文字列中でプレイスホルダーを利用(名前付き)
new_con = sqlite3.connect("tutorial.db")
new_cur = new_con.cursor()

username_input = "' OR '1'='1"
data = {"username": username_input}
print("placeholder version")
# 実行、結果を出力
print(new_cur.execute("SELECT * FROM user WHERE username = :username;", data).fetchall())

con.close()
