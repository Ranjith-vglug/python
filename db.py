# import sql name
#con=sqn name .connect("file name")


def insert(name,age)
    qer="insert into file name (Name,age)values(?,?,?);"
    con.execute(qry,(name,age))
    con.commit()
    print("value inserted")






print ("""
1.insert
2.update
3.delete
4.select
       
""")

r=1
while r==1:
    c=int(input("select you choice :"))
    if(c==1):
        print("add new record")
        name=input("Enter the name:")
        age=input("Enter the age:")
        insert(name,age)
    elif(c==2):
