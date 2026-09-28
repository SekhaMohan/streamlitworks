
import mysql.connector

class BookListCreateRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="root",host="localhost",database="library_db"
        )
        print(self.connection)
        self.cursor=self.connection.cursor()
        print("successfully connected")
    def list(self):
        #read all the records  from table
        query="select * from book"
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            # for row in records:
            #     print(row)
            #print(records)
            return records
        else:
            print("no records found")
    def create(self,title,author,price,pages,language):
        query="insert into book(title,author,price,pages,language) values(%s,%s,%s,%s,%s)"
        data=(title,author,price,pages,language)
        self.cursor.execute(query,data)
        self.connection.commit()
        print("data inserted successfully")
    def retrieve(self,id):
        query="select * from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            #print(record)
            return record
        else:
            print("no records found")
    def update(self,title,author,price,pages,language,id):
        query="update book set title=%s,author=%s,price=%s,pages=%s,language=%s where id=%s"
        data = (title,author,price,pages,language,id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            #print("data is updated")
            return True
        else:
            #print("id not found")
            return False
    def delete(self,id):
        query="delete from book where id=%s"
        data=(id,)
        self.cursor.execute(query,data)
        self.connection.commit()
        if self.cursor.rowcount>0:
            #print("data is deleted")
            return True
        else:
            #print("data not found")
            return False
book_instance=BookListCreateRetrieveUpdateDelete()
#book_instance.list()
#book_instance.create("STU","sam",400,500,"english")
#book_instance.retrieve(2)
book_instance.update("XYZ","mekha",200,150,"malayalam",1)
#book_instance.delete(3)