import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
# c.execute('''CREATE TABLE stocks
#              (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Never do this -- insecure!
# symbol = 'RHAT'
# c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)
# print('symbol=RHAT',c.fetchone())

# Do this instead
# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
# print('RHAT',c.fetchone())

# Larger example that inserts many records at a time
# purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
#              ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
#              ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
#             ]
# c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


# for row in c.execute('SELECT * FROM stocks limit 2 offset 2'):
#   print('all:',row)

# c.execute(
#   '''
#     CREATE TABLE stu(id int, name text, classid int)
#   '''
# )
# stus = [
#   (1,'A',1),
#   (2,'B',1),
#   (3,'C',2),
#   (4,'D',2),
#   (5,'E',2)
# ]
# c.executemany('INSERT INTO stu VALUES (?,?,?)', stus)

# for row in c.execute('SELECT *,(select max(id) from stu where classid = s1.classid) as maxid FROM stu as s1 order by classid desc'):
#   print('stu',row)

# c.execute(
#   '''
#     CREATE TABLE order1(num int, city int, price int, time text)
#   '''
# )
# orders = [
#   (1,10,100,'2019/3/14 15:33'),
#   (2,12,124,'2019/3/16 15:33'),
#   (3,10,110,'2019/3/15 15:33'),
#   (4,14,31,'2019/3/20 15:33')
# ]
# c.executemany('INSERT INTO order1 VALUES (?,?,?,?)', orders)

c.execute(
  '''
    CREATE TABLE IF NOT EXISTS city(num int,name text)
  '''
)
# citys = [
#   (10,'北京'),
#   (12,'武汉'),
#   (14,'成都')
# ]
# c.executemany('insert into city values (?,?)',citys)

for row in c.execute('select * from city'):
  print('city', row)
for row in c.execute('select * from order1'):
  print('order', row)
for row in c.execute('select city.name,order1.time,count(order1.num),min(price) from order1 join city on order1.city = city.num group by order1.time,city.num'):
  print('order_and_city', row)

# Save (commit) the changes
conn.commit()
conn.close()