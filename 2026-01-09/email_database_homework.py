import sqlite3

# 1. 建立数据库连接（注意 .sqlite 后缀）
connection = sqlite3.connect('email_database.sqlite')
cursor = connection.cursor()

# 2. 重建表，保证每次运行是干净的
cursor.execute('DROP TABLE IF EXISTS Counts')
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# 3. 读取文件并统计
with open('mbox.txt', 'r', encoding='utf-8') as email_file:
    print("email_file type is: ", type(email_file))
    for line in email_file:
        if not line.startswith('From: '):
            continue

        email = line.split()[1]
        org = email.split('@')[1]

        cursor.execute(
            'SELECT count FROM Counts WHERE org = ?',
            (org,)
        )
        row = cursor.fetchone()
        if row is None:
            cursor.execute(
                'INSERT INTO Counts (org, count) VALUES (?, 1)',
                (org,)
            )
        else:
            cursor.execute(
                'UPDATE Counts SET count = count + 1 WHERE org = ?',
                (org,)
            )

# 4. 只 commit 一次（性能关键点）
connection.commit()


cursor.execute(
    'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 1'
)


connection.close()