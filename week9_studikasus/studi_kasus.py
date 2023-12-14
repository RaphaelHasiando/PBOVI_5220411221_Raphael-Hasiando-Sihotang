#       Tugas Kelompok | Studi Kasus Minggu 9
#       Kelompok:
#       1.      Raphael Hasiando Sihotang   (5220411221)
#       2.      Jofran Albhinata            (5220411214)
#       3.      NONE                        
#================================================================


#       Import
import time

#       Kode Program


class KendaraanDarat:
    def __init__(self, TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang):
        self.tahun = TahunKeluaran
        self.nama = Nama
        self.warna = Warna
        self.kecepatan = Kecepatan
        self.bhn_bakar = BahanBakar
        self.jml_roda = JumlahRoda
        self.kap_penumpang = KapasitasPenumpang
    

class Kereta(KendaraanDarat):
    def __init__(self, TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, JenisGerbong, JumlahKursi, JenisLayananKereta, Rute):
        super().__init__(TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang=JumlahKursi)
        self.jenis_gerbong = JenisGerbong
        #   Jenis-jenis Gerbong : Gerbong Datar, Gerbong Terbuka, Gerbong Tertutup, Gerbong Ketel, Kereta Bagasi, dan Gerbong bongkar.
        self.jml_kursi = JumlahKursi
        self.jenis_layanan = JenisLayananKereta
        #   Jenis-jenis Layanan : Kereta Api Jarak-Jauh, Kereta Api Lokal, Kereta Rel Listrik (KRL), LRT, MRT Jakarta, Kereta Api Bandara, dan Kereta Cepat Jakarta-Bandung (KCJB)
        self.rute = [Rute]

    def tambahRute(self, dari, ke):
        value_list = [dari, ke]
        if value_list in self.rute:
            print("Rute yang anda ingin tambahkan sudah ada")
            return
        self.rute.append(value_list)
        print("Metode Tambah Rute")

    # OVERLOADING
    def kurangiRute(self, dari_rute = None, ke_rute = None):
        if dari_rute is None and ke_rute is None:
            self.rute.pop()
            return
        __list_dari = []
        __list_ke = []
        # Keberangkatan | Dari
        x = 0
        if dari_rute is not None:
            for i in self.rute:
                if dari_rute in i[0]:
                    __list_dari.append(x)
                x += 1
        # Kedatangan | Ke
        y = 0
        if ke_rute is not None:
            for i in self.rute:
                if ke_rute in i[1]:
                    __list_ke.append(y)
                y += 1
        
        __hasil_pencarian = []
        if len(__list_dari) == 0 and len(__list_ke) == 0:
                print("Tidak ditemukan")
                return
        if dari_rute is None and ke_rute is not None:
            __hasil_pencarian = __list_ke
        elif dari_rute is not None and ke_rute is None:
            __hasil_pencarian = __list_dari
        else:
            for j in __list_dari:
                for k in __list_ke:
                    if self.rute[j] == self.rute[k]:
                        __hasil_pencarian.append(j)


        if len(__hasil_pencarian) == 1:
            print(f"Apakah anda ingin menghapus rute {self.rute[__hasil_pencarian[0]]}")
            def fungsi_input2():
                value_input = int(input("1. IYA | 0. TIDAK"))
                if value_input == 1:
                    self.rute.pop(value_input)
                    print("Rute berhasil dihapus")
                elif value_input == 0:
                    print("Membatalkan...")
                    return
                else:
                    print("Mohon diulangi...")
                    fungsi_input2()
            fungsi_input2()
        elif len(__hasil_pencarian) > 1:
            print(f"Beberapa rute ditemukan bedasarkan pencarian anda:")
            x = 0
            for m in __hasil_pencarian:
                x += 1
                print(f"{x}. {self.rute[m]}")
            print("Pilih nomor untuk menghapus salah satu rute diatas")
            def fungsi_input():
                value_input = int(input("==> "))
                if value_input > 0 and value_input <= len(__hasil_pencarian):
                    self.rute.pop(value_input)
                else:
                    print("Mohon diulangi...")
                    fungsi_input()
            fungsi_input()
            print("Rute Berhasil dihapus.")
    

class Mobil(KendaraanDarat):
    def __init__(self, TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang, JenisMobil):
        super().__init__(TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang)
        self.jenis_mobil = JenisMobil
        self.kondisi_mobil = False
        self.aktivitas_perjalanan_mobil = []
    
    def startEngine(self):
        if self.kondisi_mobil is False:
            print("Menghidupkan mesinnya...")
            time.sleep(2)
            print("Hidup!!\n")
            self.kondisi_mobil = True
            self.aktivitas_perjalanan_mobil.append("START ENGINE")
        else:
            print("Mobil sudah hidup")
    
    def stopEngine(self):
        if self.kondisi_mobil is True:
            print("Mematikan Mesin...\n")
            self.kondisi_mobil = False
            self.aktivitas_perjalanan_mobil.append("STOP ENGINE")
        else:
            print("Mobil sudah mati")
    
    def Maju(self):
        if self.kondisi_mobil is False:
            print("Hidupkan mesinnya terlebih dahulu!")
            return
        time.sleep(0.5)
        print("Maju ke depan")
        self.aktivitas_perjalanan_mobil.append("MAJU")
    
    def Mundur(self):
        if self.kondisi_mobil is False:
            print("Hidupkan mesinnya terlebih dahulu")
            return
        print("Mundur ke belakang")
        self.aktivitas_perjalanan_mobil.append("MUNDUR")

    def Belok(self, arah):
        if self.kondisi_mobil is False:
            print("Hidupkan mesinnya terlebih dahulu")
            return
        time.sleep(0.5)
        if arah == "kiri":
            print("Belok ke kiri")
            self.aktivitas_perjalanan_mobil.append("BELOK KIRI")
        if arah == "kanan":
            print("Belok ke kanan")
            self.aktivitas_perjalanan_mobil.append("BELOK KANAN")


class MobilBalap(Mobil):
    def __init__(self, TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang, JenisMobil, FrontWing, RearWing):
        super().__init__(TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang, JenisMobil)
        self.front_wing = FrontWing
        self.rear_wing = RearWing
        #   Adding Spoiler or Wing makes your car slow, because it increase the weigth of your car. However, Spoilers and wings are designed to manipulate airflow, 
        #   primarily by generating downforce.
        #   Front Wing  :    Light Downforce Front Wing, Medium Downforce Front Wing, dan Heavy Downforce Front Wing
        #   Rear Wing   :   Light Downforce Rear Wing, Medium Downforce Rear Wing, dan Heavy Downforce Rear Wing 


    # OVERLOADING
    def race(self, jenis_race = "Drag Race"):
        
        if self.kondisi_mobil is False:
            print("Hidupkan mesinnya terlebih dahulu!")
            return
        # Jenis Race (Default: Drag Race)
        jenis = True
        if jenis_race == "Drag Race":
            print("Drag Race")
        elif jenis_race == "Circuit Race":
            print("Circuit Race")
            jenis = False
        else:
            print("Jenis Race tidak diketahui")
        
        print("Get ready, in...")
        for i in range(3):
            time.sleep(1)
            print(i + 1)
        print("Go!")

        def dragging():
            self.Maju()
            self.Maju()
        
        def circuit():
            self.Maju()
            self.Belok('kanan')
            self.Belok('kanan')
            self.Belok('kiri')
            self.Belok('kanan')
            self.Belok('kanan')
            self.Belok('kiri')
            self.Belok('kanan')
            self.Belok('kanan')
            self.Maju()
        
        if jenis is True:
            dragging()
        if jenis is False:
            circuit()
        print("Finish!")


class MobilCrossroad(Mobil):
    def __init__(self, TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang, JenisMobil, SunroofType, ShockBreaker):
        super().__init__(TahunKeluaran, Nama, Warna, Kecepatan, BahanBakar, JumlahRoda, KapasitasPenumpang, JenisMobil)
        self.tipe_sunroof = SunroofType
        self.shock_breaker = ShockBreaker
        self.kecepatan_asli = self.kecepatan
        if self.shock_breaker == "Light":
            self.kecepatan_asli = self.kecepatan_asli - 6/100 * self.kecepatan_asli
        elif self.shock_breaker == "Medium":
            self.kecepatan_asli = self.kecepatan_asli - 4/100 * self.kecepatan_asli
        elif self.shock_breaker == "Heavy":
            self.kecepatan_asli = self.kecepatan_asli - 2/100 * self.kecepatan_asli
        else:
            self.kecepatan_asli = self.kecepatan_asli - 10/100 * self.kecepatan_asli

        self.__kondisi_sunroof = False
        self.__manual_sunroof = ["Pop-up", "Soft-Top", "Spoiler"]

        # Tipe Sunroof : Pop-up (Manual), Soft-Top (Manual/Electric), Spoiler (Manual/Electric), Inbuilt, Tilt and Slide, Panoramic, Split-Type
    
    def sunroofTerbuka(self):
        if self.tipe_sunroof not in self.__manual_sunroof:
            if self.kondisi_mobil is False:
                print("Anda menggunakan tipe sunroof yang membutuhkan listrik untuk membukannya.")
                print("Hidupkan mesinnya terlebih dahulu! \n")
                return
        if self.__kondisi_sunroof is False:
            self.__kondisi_sunroof = True
            print("Membuka Sunroof...\n")
        else:
            print("Sunroof sudah terbuka\n")
    
    def sunroofTertutup(self):
        if self.tipe_sunroof not in self.__manual_sunroof:
            if self.kondisi_mobil is False:
                print("Anda menggunakan tipe sunroof yang membutuhkan listrik untuk menutupnya.")
                print("Hidupkan mesinnya terlebih dahulu! \n")
                return
        if self.__kondisi_sunroof is True:
            self.__kondisi_sunroof = False
            print("Menutup Sunroof...\n")
        else:
            print("Sunroof sudah tertutup\n")
    
    # OVERRIDING
    def stopEngine(self):
        if self.tipe_sunroof not in self.__manual_sunroof:
            if self.__kondisi_sunroof is True:
                print("WARNING! Sunroof anda masih dalam keadaan terbuka!")
        return super().stopEngine()
    


# ======================================== Objek Kendaraan Darat ========================================
objek1 = KendaraanDarat("2023", "Supra T23", "Kuning", 221, "Bensin", 4, 2)


# ======================================== Objek Kereta ========================================
print("\n==========================")
objek2 = Kereta("2008", "LRT", "Hijau", 189, "Biosolar", 8, "Gerbong Bongkar", 40, "LRT", ["Bogor", "Depok"])
#   Menampilkan rute saat ini
print(objek2.rute)
#   Menambahkan rute baru
objek2.tambahRute('Depok', 'Manggarai')
objek2.tambahRute('Manggarai', 'Gambir')
objek2.tambahRute('Gambir', 'Jakarta Kota')
#   Tidak akan ditambahkan ke rute, karena rute yang ditambahkan tersebut sudah ada di rute saat ini
objek2.tambahRute('Depok', 'Manggarai')
print(objek2.rute)
objek2.kurangiRute(None, "ar")
#   Fungsinya akan mencari kata yang mendekati kata yang tersedia di Rute.
objek2.kurangiRute('Depo', "Manggara")
print(objek2.rute)
print(objek2.jml_kursi)
print("==========================\n")


# ======================================== Objek Mobil ========================================
objek3 = Mobil("2022", "Mercedes Benz C300", "Hitam", 178, "Bensin", 4, 4, "Sedan")
print("\n==========================")
#   Mobil tidak akan bergerak karena mesinnya masih dalam keadaan mati
objek3.Maju()
#   Dihidupkan dengan memanggil method 'startEngine()'. Suatu variable bernama 'self.kondisi_mobil' akan bernilai True
objek3.startEngine()
#   Seluruh method yang dipanggil akan dicatat ke dalam variable list, yaitu 'self.aktivitas_mobil'
objek3.Maju()
objek3.Mundur()
objek3.Belok('kiri')
objek3.Belok('kanan')
#   Akan memberi peringatan kepada pengguna jika menghidupkan mobil ketika mesinnya masih hidup
objek3.startEngine()
#   pemanggilan method dibawah ini digunakan untuk mematikan mesin mobil, dimana suatu atribut (self.kondisi_mobil) akan bernilai False
objek3.stopEngine()
#   Akan memberi peringatan kepada pengguna jika mematikan mobil ketika mesinnya sudah mati
objek3.stopEngine()
print("==========================\n")


# ======================================== Objek Mobil Crossroad ========================================
objek4 = MobilCrossroad("1990", "Civic HM239", "Merah", 90, "Bensin", 4, 2, "Honda", "Pop-up", "Light")
print("\n==========================")
objek4.sunroofTerbuka()
objek4.startEngine()
objek4.sunroofTerbuka()
objek4.stopEngine()
objek4.sunroofTertutup()
objek4.sunroofTerbuka()
print(objek4.nama," : ",objek4.aktivitas_perjalanan_mobil)
print("==========================\n")

print("\n==========================")
objek5 = MobilCrossroad("1990", "SUV T50", "Merah", 178, "Bensin", 4, 2, "Honda", "Panoramic", "Medium")
objek5.sunroofTerbuka()
objek5.startEngine()
objek5.sunroofTerbuka()
objek5.stopEngine()
objek5.sunroofTertutup()
objek5.sunroofTerbuka()
print(objek1.nama," : ",objek5.aktivitas_perjalanan_mobil)
print("==========================\n")

# ======================================== Objek Mobil Balap ========================================
print("\n==========================")
objek6 = MobilBalap("1990", "F40", "Merah", 90, "Bensin", 4, 2, "Ferrari", "Medium Front Wing", "Medium Rear Wing")
objek6.startEngine()
objek6.race()
print(objek6.kecepatan)
objek6.race('Circuit Race')
print("\n==========================")
