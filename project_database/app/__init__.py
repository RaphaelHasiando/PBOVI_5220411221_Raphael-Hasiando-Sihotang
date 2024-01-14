import mysql.connector
import os

error_database = False
try:
    connect = mysql.connector.connect(
        host ="localhost",
        username ="root",
        password ="",
    )
    cursor = connect.cursor()
except:
    error_database = True
    print("Belum terkoneksi ke MySQL Database, Mohon dihidupkan terlebih dahulu")



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
                a_sosial = ("alamat", "nama", "tempat_lahir", "tanggal_lahir")
                sosial_masyarakat = ("NIK", "kelurahan", "kecamatan", "sosialisasi_poin")
                sosial_kampus = ("nama_kampus", "jurusan", "fakultas", "npm")
                sosial_kelas = ("kelas", "nama_matkul")
                sql = "CREATE TABLE sosial_users (id INT AUTO_INCREMENT PRIMARY KEY, %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255))"
                cursor.execute(sql % a_sosial)
                sql = "CREATE TABLE sosial_masyarakat_users (id INT, FOREIGN KEY (id) REFERENCES sosial_users(id), %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255), %s INT(255), PRIMARY KEY(NIK))"
                cursor.execute(sql % sosial_masyarakat)
                sql = "CREATE TABLE sosial_kampus_users (id INT, FOREIGN KEY (id) REFERENCES sosial_users(id), %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255), %s VARCHAR(255), PRIMARY KEY(npm))"
                cursor.execute(sql % sosial_kampus)
                sql = "CREATE TABLE sosial_kelas_users (id INT, FOREIGN KEY (id) REFERENCES sosial_kampus_users(id), %s VARCHAR(255), %s VARCHAR(255))"
                cursor.execute(sql % sosial_kelas)
                print("Database telah berhasil dibuat")
                return True
            elif user_input == "TIDAK":
                print("Tutup...")
                os.system("exit")
                return
            else:
                return konf_input()
        return konf_input()
    else:
        print("Terhubung ke Database 5220411221...")
        return False

if error_database is False:
    start_database()

