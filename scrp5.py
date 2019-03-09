"""x = 8
name = 'Nagendra'

value = [1,2,3,4,5,6]
print (type(value))

val2 =(1,2,5,3,6,4)

print (type(val2))
if ('s' in name):
    print (True)
else:
     print ('Flase')
print ("values:%d " %x +"User name : %s " %name)

a = (" Hello, World! ")
print (type(a[0]))
print(a.strip())
a = "Hello, World!"
print(a.replace("H", "J"))
data = input("Enter the data: ")

print ("Length of data: %d" %(len(data)))"""
value = [1,2,3,4,5,6]
value2 = (1,2,3,4,5,6)
value3 = {1,2,3,4,5,6}

value3.add(10)
value3.add(2)
value3.update([11,12])
value3.discard(11)
value3.remove(10)

val4 = tuple(value3)
val5 = list(value3)

#print (value2.index(3))

def deploy():
     """print(value)
     value.append(val)
     print(value)
     value.insert(1,10)
     print(value)
     value.remove(10)
     value.pop()
     print (value)
     #del value
     #value.clear()

     value.reverse()
     print(value)
     print (value3)
     print (val4)
     print (val5)
     data = {
         "brand": "Ford",
         "model": "Mustang",
         "year": 1964
     }
     print(data)
     print(data.get('year'))
     print(data.items())
     print(data.keys())
     print(data.values())
     chk ={}
     chk['name']  =('Nagendra')
     chk['id']    ='205048'
     chk['email'] ='N.NagendraAndra@spi-global.com'
     chk['Role']  ='ReleaseEngineer'
     print ('My name is        : ' + chk.get('name'))
     print ('My Employee id is : '+chk.get('id'))
     print ('My Email    id is : '+chk.get('email'))
     print ('My Positios    is : '+chk.get('Role'))
     quote = 'Think Positive'
     for i in range(21):
         print(quote)
     #for i in data:
     #   print (i)
     name = input("Enter the name: ")
     if name =='Nagendra':
        print (True)
     else:
        print (False)
     a = 30
     b = 20
     if a >b: print("a is greater than b")
     i = 0
     i = 1
     while i < 6:
         print(i)
         if i == 3:
             break
         i += 1


deploy()

def my_function():
  print("Hello from a function")

my_function()
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def first(value ='10'):
    print (value)

first(20)
first()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(x):
  return 5 * x
  x = lambda a: a + 10
  print(x(5))
print (my_function(10))

from urllib.request import urlopen
from bs4 import BeautifulSoup

link = urlopen('https://realpython.com/')

soup = BeautifulSoup(link,'lxml')

print (soup)

quote = " no jealous "

for i in range(21):
    print (quote)"""
"""import pymysql

class MyClass:
 def __init__(self,name):
     self.x = name
text = MyClass('Nagendra ' +'andra' )
#print ("My name is ",text.x)

class emp:
    def __init__(self,name,id,email):
        self.name  = name
        self.id    = id
        self.email = email
    def date(text):
        print ("My name is: "+ text.name)
        print ("My oid  is: "+ text.id)
        print ("My oid  is: "+ text.email)
pd = emp('Nagendra','205048','N.NagendraAndra@spi-global.com')
#pd.date()

class database:
    def __init__(self, hostname, username, password, databasename):
        self.hostname   = hostname
        self.username   = username
        self.password   = password
        self.databasename = databasename

    def check(verify):
        conn = pymysql.connect(verify.hostname,verify.username,verify.password,verify.databasename )
        cursor = conn.cursor()

        #print (cursor.execute("create database ci"))
        databases = (cursor.execute("select databases()"))

        for i in cursor.fetchall():
            print (i)
        print (cursor.execute("show tables"))
        tables = cursor.fetchall()
        for i in tables:
            print(i)
        #cursor.execute("show database")
        #cursor.execute("use ci")
        #sql = "create table nag(id INT )"
        #(cursor.execute('describe automation '))
        #print (cursor.fetchall())
        #sql = "insert into automation(email) values('N.NagendraAndra')"
        #cursor.execute(sql)
        #conn.commit()
        cursor.execute('select * from automation')

        for i in cursor.fetchall():
            # print (i[0])
            if i[0] == 205048:
                print(i[0])
            # if i[0]== '205048':
            #     print (i[0])



        #cursor.execute("CREATE TABLE  automation(id int,name varchar(20), email varchar(20))")

        #cursor.commit()

        #cursor.execute("select database()")
        #db_name = cursor.fetchone()[0]
        #print (db_name)
        #cursor.execute("show tables")
        #get the database list and names
        cursor.execute("show databases")
        for r in cursor.fetchall():
            if str(r) is 'ci':
                print ("database name")
            else:
                print ("not match")




db = database('54.173.201.15','nagendra','Nagendra@1818','ci')
db.check()
#username:nagendra
#password:Nagendra@1818
# create user 'nagendra'@'%' identified by "password";
# GRANT ALL PRIVILEGES ON * . * TO 'username'@'%'; FLUSH PRIVILEGES;(% --> all host machines)
"""

def aws(val):
    print ("values is: "+ val)