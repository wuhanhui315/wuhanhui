"""
模拟注册程序
"""
import pymysql
db=pymysql.connect(host="127.0.0.1",port=3306,user="root",password="root",database="stu",charset="utf8")
cur=db.cursor()
def register():
    name = input("用户名:")
    password=input("密码:")
    sql="select * from user where name='%s';"%name
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return False
    try:
        sql="insert into user (name,password) values(%s,%s);"
        cur.execute(sql,[name,password])
        db.commit()
    except Exception as e:
        cur.rollback()
        print(e)
def login():
    name = input("用户名:")
    password = input("密码:")
    sql = "select * from user where name='%s' and password='%s';" % (name,password)
    cur.execute(sql)
    result = cur.fetchone()
    if result:
        return True
while True:
    print("==============")
    print("1.注册  2.登录")
    print("==============")
    cmd = input("请输入命令:")
    if cmd == "1":
        if register():
            print("注册成功")
        else:
            print("注册失败")
    elif cmd=="2":
        if login():
            print("登录成功")
            break
        else:
            print("登录失败")

    else:
        print("输入有误，请重新输入")
        continue
