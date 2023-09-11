from pysql import DBHelper

# From {file_name} import {functions}

# From {otherfolder.filename} import {functions}


def main():
    db = DBHelper()
    print("************** WELCOME TO PYSQL *****************")
    while True:
        
        print("PRESS 1 TO INSERT USER")
        print("PRESS 2 TO DELETE USER")
        print("PRESS 3 TO UPDATE USER")
        print("PRESS 4 TO SHOW ALL USER")
        print("PRESS 5 TO EXIT PROGRAM")
        print("\n")
        try:
            choice = int(input())
            print("\n")
            match choice:
                case 1:
                    uid = input("Enter user id ")
                    username = input("Enter username ")
                    ipaddress = input("Enter Ipadddress format xxx.xxx.xxx.xx ")
                    rwt = input("RWT?")
                    db.insert_user(uid, username, ipaddress, rwt)
                case 2:
                    uid = input("Enter user id of which you want to delete ")
                    db.delete_user(uid)
                case 3:
                    uid = input("Enter user id ")
                    newName = input("Enter username ")
                    newrwt = input("RWT?")
                    db.update_user(uid, newName, newrwt)
                case 4:
                    db.fetch_all()
                case 5:
                    break
                case default:
                    print("Insert a number") 
        except Exception as e:
            print(e)
            print("Please enter in a real number")



if __name__ == "__main__":
    main()


