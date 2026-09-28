import mysql.connector

class Blood_donor():
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="root",host="localhost",database="blood_db"
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def post(self,name,blood_group,phone,city,last_don):
        query="insert into donor(name,blood_group,phone,city,last_don) values(%s,%s,%s,%s,%s)"
        data=(name,blood_group,phone,city,last_don)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted successfully")
    def get(self,id):
        #read all the records  from table
        query="select * from donor"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            return records
        else:
            print("no records found")
    def retrieve(self,id):
        query="select * from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            #print(record)
            return record
        else:
            print("no records found")
    def put(self,name,blood_group,phone,city,last_don,id):
        query="update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_don=%s where id=%s"
        data = (name,blood_group,phone,city,last_don,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            # print("data is updated")
            return True
        else:
            #print("id not found")
            return False
    def delete(self,id):
        query="delete from donor where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            print("data is deleted")
        else:
            print("data not found")
donor_instance=Blood_donor()
#book_instance.list()
#book_instance.create("STU","sam",400,500,"english")
#book_instance.retrieve(2)
#book_instance.update("XYZ","mekha",200,150,"malayalam",1)
#book_instance.delete(3)