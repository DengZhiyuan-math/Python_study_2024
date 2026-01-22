import sqlite3

# 1. 连接数据库（不存在会自动创建）
conn = sqlite3.connect(
    "/Users/zhdeng/Python_study_2024/test_SQL.db"
)


# 2. 创建游标（你和数据库对话的“嘴”）
cursor = conn.cursor()

# 3. 要插入的一批数据
Users = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
]

# 4. 批量插入
cursor.executemany(
    "INSERT INTO Users (name, email) VALUES (?, ?)",
    Users
)

# 5. 提交事务（非常重要）
conn.commit()

# 测试
cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()
print(rows)
# 6. 关闭连接
conn.close()



