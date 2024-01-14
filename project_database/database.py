import mysql.connector

connect = mysql.connector.connect(
    host ="localhost",
    username ="root",
    password ="",
)

cursor = connect.cursor()

def check_database():
    cursor.execute("SHOW DATABASES LIKE '5220411221'")
    result = cursor.fetchone()
    if result is None:
        return False
    else:
        connect.database = "5220411221"
        return True
        
def start_database():
    if check_database() is False:
        print("Database belum ada, apakah anda ingin membuat database baru?")
        def konf_input():
            user_input = input("(YA / TIDAK) ==> ")
            if user_input == "YA":
                # Create Database
                cursor.execute("CREATE DATABASE `5220411221`")
                connect.database = "5220411221"

                # Create Table
                cursor.execute("CREATE TABLE sosial_users (id INT AUTO_INCREMENT PRIMARY KEY, object VARCHAR(255))")
                cursor.execute("CREATE TABLE sosial_masyarakat_users (FOREIGN KEY (id) REFERENCES sosial_users(id), %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255), "
                               "%s VARCHAR(255))")
                cursor.execute("CREATE TABLE sosial_kampus_users (FOREIGN KEY (id) REFERENCES sosial_users(id), name VARCHAR(255), address VARCHAR(255))")
                cursor.execute("CREATE TABLE sosial_kelas_users (FOREIGN KEY (id) REFERENCES sosial_users(id), name VARCHAR(255), address VARCHAR(255))")
                connect.database = "5220411221"
                print("Database telah berhasil dibuat")
                return True
            elif user_input == "TIDAK":
                print("Tutup...")
                return False
            else:
                return konf_input()
        return konf_input()
    else:
        print("Tutup...")
        return False

start_database()

# cursor = connect.cursor()

