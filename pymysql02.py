import pymysql
db = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='school',charset='utf8')
cur = db.cursor()
sql = 'select name from student'
cur.close()
db.close()