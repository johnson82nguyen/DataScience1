import mysql.connector as connector




class DBHelper:
    def __init__(self):

        self.con = connector.connect(host='localhost', 
                        port='3306',
                        user='root',
                        password='',
                        database='pythontest')
        print("Initialized")
    
#Creates user_table
    def create_user_table(self):
        query = 'create table if not exists user(userId int primary key, userName varchar(200), ipaddress varchar(200), rwt varchar(200))'
        cur = self.con.cursor()
        cur.execute(query)



#inserts users into user table. Each user needs unique Id
    def insert_user(self, userId, userName, ipaddress, rwt):
        query = "insert into user(userId, userName, ipaddress, rwt) values('{}','{}','{}', '{}')".format(userId, userName, ipaddress, rwt)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to database")


#update user based on userId
    def update_user(self, userId, newName, newRWT):
        query="update user set userName='{}',rwt='{}' where userId={}".format(newName,newRWT,userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        

#Fetches all data from user table
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("id:", row[0])
            print("name:", row[1])
            print("ipaddress:", row[2])
            print("rwt:", row[3])
            print(" ")
    

#Deletes users based on userId
    def delete_user(self, userId):
        query = "delete from user where userId={}".format(userId)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(" " + str(userId) + " Has been deleted.")








# Main coding

helper = DBHelper()

# helper.delete_user(28)
helper.update_user(27, 'asianchad', 'f')
helper.fetch_all()


# helper.insert_user('25', 'Brewce_Wayne', '111.162.103.11', 'T')
# helper.insert_user('26', 'Scibbity', '111.162.103.11', 'T')
# helper.insert_user('27', 'Asian_Chad', '111.162.103.11', 'T')
# helper.insert_user('28', 'Confide', '111.162.103.11', 'T')
# helper.insert_user('29', 'Linx', '111.162.103.11', 'T')
# helper.insert_user('30', 'Breeshki', '111.162.103.11', 'T')


