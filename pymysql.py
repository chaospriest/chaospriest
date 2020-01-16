import pymysql
# host = 127.0.0.1
# port = 3306
# user = 'root'
# password = '123456'
# database = 'stu'
db = pymysql.connect(host=127.0.0.1,port=3306,user='root',password='123456',database='stu',charset='utf8')
cur = db.cursor()
st = input('请输入学生姓名：')
sql = 'select name,age,sex,score from 一班 where name = %s;'%st
cur.execute(sql)
# for i in cur:
#     print(i)
print(cur.fetchall())
cur.close()
db.close()