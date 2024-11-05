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

# 実行、結果を出力
print(cur.execute(sql).fetchall())

con.close()