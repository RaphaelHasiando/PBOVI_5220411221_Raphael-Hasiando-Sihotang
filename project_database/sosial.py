#   Nama    :   Raphael Hasiando Sihotang
#   NPM     :   5220411221
#   Kelas   :   VI
#   Tema    :   Sosial

from app import cursor

class KegiatanSosial:
    def __init__(self, nama, alamat, tempatLahir, tanggalLahir):
        self.nama = nama
        self.alamat = alamat
        self.tempatLahir = tempatLahir
        self.tanggalLahir = tanggalLahir

class SosialMasyarakat(KegiatanSosial):
    def __init__(self, nama, alamat, tempatLahir, tanggalLahir, NIK, kelurahan, kecamatan, sosialisasi):
        super().__init__(nama, alamat, tempatLahir, tanggalLahir)
        self.NIK = NIK
        self.kelurahan = kelurahan
        self.kecamatan = kecamatan
        # Akses Modifier
        self.__sosialisasi = sosialisasi      
    
    def gotong_royong(self):
        print("Melakukan Gotong Royong \n")
        self.__sosialisasi += 1
    
    def kegiatan_ronda(self):
        print("Melakukan kegiatan Ronda malam \n")
        self.__sosialisasi += 1
    
    def menjenguk_tetangga(self):
        print("Menjenguk tetangga \n")
        self.__sosialisasi += 1
    
    def __tampilkan_sosialisasi(self):
        if self.__sosialisasi <= 3:
            print(f"Poin Sosialisasi anda masih kurang, Lakukanlah kegiatan lain supaya poin anda bertambah. \n")
        if self.__sosialisasi > 3 and self.__sosialisasi <= 6:
            print(f"Poin Sosialisasi anda mencapai {self.__sosialisasi}, Tetaplah terus mengikuti kegiatan! \n")
        if self.__sosialisasi > 6 and self.__sosialisasi <= 10:
            print(f"Poin Sosialisasi anda mencapai {self.__sosialisasi}. Anda telah mencapai tingkat yang terbaik! \n")
        if self.__sosialisasi > 10:
            print(f"Poin Sosialisasi anda mencapai {self.__sosialisasi}. Anda telah mencapai tingkat yang sangat terbaik! \n")
        
    def r_tampilkan_sosialisasi(self):
        self.__tampilkan_sosialisasi()


class SosialKampus(KegiatanSosial):
    def __init__(self, nama, alamat, tempatLahir, tanggalLahir, namaKampus, jurusan, fakultas, npm):
        super().__init__(nama, alamat, tempatLahir, tanggalLahir)
        self.namaKampus = namaKampus
        self.jurusan = jurusan
        self.fakultas = fakultas
        self.npm = npm
        #   Akses Modifier
        self.kondisiLokasi = False
        self._kondisiLokasi2 = False
        self._kondisiLokasi3 = False

    def masuk_kelas(self):
        if self.kondisiLokasi is True:
            print("Anda sudah di dalam kelas...")
            return
        if self._kondisiLokasi2 is True:
            print("Mohon keluar dari perpustakaan...")
            return
        if self._kondisiLokasi3 is True:
            print("Mohon keluar dari ruangan organisasi...")
            return
        self.kondisiLokasi = True
        print("Memasuki kelas...")

    def keluar_dari_ruangan(self):
        if self.kondisiLokasi is True:
            print("Keluar dari kelas...")
            self.kondisiLokasi = False
            return
        if self._kondisiLokasi2 is True:
            print("Keluar dari perpustakaan...")
            self._kondisiLokasi2 = False
            return
        if self._kondisiLokasi3 is True:
            print("Keluar dari ruangan organisasi...")
            self._kondisiLokasi3 = False
            return
        print("Anda sudah di luar")

    def diskusi(self):
        if self.kondisiLokasi is True:
            print("Berdiskusi di dalam kelas...")
            return
        if self._kondisiLokasi2 is True:
            print("Berdiskusi di dalam perpustakaan...")
            return
        if self._kondisiLokasi3 is True:
            print("Berdiskusi di dalam ruangan organisasi...")
            return
        print("Berdiskusi di kampus")

    def kerja_kelompok(self):
        if self.kondisiLokasi is True:
            print("Kerja Kelompok di dalam kelas...")
            return
        if self._kondisiLokasi2 is True:
            print("Kerja Kelompok di dalam perpustakaan...")
            return
        if self._kondisiLokasi3 is True:
            print("Kerja Kelompok di dalam ruangan organisasi...")
            return
        print("Kerja Kelompok di kampus...")
        
    
    #   Protected, kegiatan hanya dilakukan di luar kelas
    def _perpustakaan(self):
        if self.kondisiLokasi is True:
            print("Mohon keluar dari kelas terlebih dahulu...")
            return
        if self._kondisiLokasi2 is True:
            print("Anda sudah di dalam perpustakaan..,")
            return
        if self._kondisiLokasi3 is True:
            print("Mohon keluar dari organisasi terlebih dahulu...")
            return
        print("Masuk ke perpustakaan...")
        self._kondisiLokasi2 = True

    
    #   Protected, kegiatan hanya dilakukan di luar kelas
    def _mengikuti_kegiatan_organisasi(self):
        if self.kondisiLokasi is True:
            print("Mohon keluar dari kelas terlebih dahulu...")
            return
        if self._kondisiLokasi2 is True:
            print("Mohon keluar dari perpustakaan terlebih dahulu...")
            return
        if self._kondisiLokasi3 is True:
            print("Anda sudah di dalam ruangan organisasi...")
            return
        print("Masuk ke dalam ruangan organisasi...")
        self._kondisiLokasi3 = True
    
    def info(self):
        print(f"Nama            :   {self.nama}")
        print(f"Alamat          :   {self.alamat}")
        print(f"Tempat Lahir    :   {self.tempatLahir}")
        print(f"Tanggal Lahir   :   {self.tanggalLahir}")
        print(f"Nama Kampus     :   {self.namaKampus}")
        print(f"Jurusan         :   {self.jurusan}")
        print(f"Fakultas        :   {self.fakultas}")
        print(f"NPM             :   {self.npm}")
    


class SosialKelas(SosialKampus):
    def __init__(self, nama, alamat, tempatLahir, tanggalLahir, namaKampus, jurusan, fakultas, npm, kelas, namaMatkul):
        super().__init__(nama, alamat, tempatLahir, tanggalLahir, namaKampus, jurusan, fakultas, npm)
        self.kelas = kelas
        self.matkul = namaMatkul
    
    def belajar(self):
        if self.kondisiLokasi is False:
            print("Belajar di luar kelas...")
            return
        if self.kondisiLokasi is True:
            print("Belajar di dalam kelas")

    def presentasi(self):
        if self.kondisiLokasi is False:
            print("Harap Masuk ke dalam kelas terlebih dahulu")
            return
        print("Presentasi...")

    # Overriding, mengambil dan mengubah salah satu method dari kelas induknya
    def info(self):
        print(f"Nama            :   {self.nama}")
        print(f"Alamat          :   {self.alamat}")
        print(f"Tempat Lahir    :   {self.tempatLahir}")
        print(f"Tanggal Lahir   :   {self.tanggalLahir}")
        print(f"Nama Kampus     :   {self.namaKampus}")
        print(f"Jurusan         :   {self.jurusan}")
        print(f"Fakultas        :   {self.fakultas}")
        print(f"NPM             :   {self.npm}")
        print(f"Kelas           :   {self.kelas}")
        x = 0
        for i in self.matkul:
            x += 1
            print(f"Mata Kuliah {x}   :   {i}")

##################
### CONTROLLER ###

objects_masyarakat = []       # Menyimpan objek ke dalam list kegiatan. Digunakan untuk mengakses salah satu dari beberapa objek
objects_kampus = []
objects_kelas = []  

def main_menu():
    CRUD()
    hasil_input = sistem_CRUD()
    if hasil_input == 1:
        hasil_input_2 = kegiatan_menu()
        if hasil_input_2 is True or hasil_input_2 is False or hasil_input_2 == 1:
            tambah_data(hasil_input_2)
    if hasil_input == 2:
        hasil_input_2 = kegiatan_menu()
        if hasil_input_2 is True or hasil_input_2 is False or hasil_input_2 == 1:
            lihat_data(hasil_input_2)
    if hasil_input == 3:
        hasil_input_2 = kegiatan_menu()
        if hasil_input_2 is True or hasil_input_2 is False or hasil_input_2 == 1:
            hapus_data(hasil_input_2)
    if hasil_input == 0:
        print("Terima Kasih")
        return
    main_menu()
    

def CRUD():
    print("1.   Tambah Data")
    print("2.   Lihat Data")
    print("3.   Hapus Data")
    print("0.   Keluar")
    # Tambahan
    # Tampil => Tampilkan semua data, Tampilkan Masyarakat, Tampilkan Kampus, Tampilkan Kelas
    # Hapus => Cari nama
    # Ubah => 

def sistem_CRUD():
    input_user = int(input("==> "))
    if input_user == 1:
        print("Tambah Data")
        return 1
    if input_user == 2:
        print("Lihat Data")
        return 2
    if input_user == 3:
        print("Hapus Data")
        return 3
    if input_user == 0:
        print("Keluar dari sistem")
        return 0
    print("Input invalid, mohon diulangi")
    return sistem_CRUD()

def kegiatan_menu():
    tempat_kegiatan()
    hasil_input = input_func()
    if hasil_input is True or hasil_input is False:
        if hasil_input is True:
            return True
        if hasil_input is False:
            return False
    else:
        if hasil_input == 1:
            return 1
        print("Kembali ke main menu")
        return 0

def tempat_kegiatan():
    print("Kegiatan di Lingkungan: ")
    print("1.   Masyarakat")
    print("2.   Kampus")
    print("3.   Kelas")
    print("0.   Kembali")

def input_func():
    input_user = int(input("==> "))
    if input_user == 1:
        print("Masyarakat")
        return True
    if input_user == 2:
        print("Kampus")
        return False
    if input_user == 3:
        print("Kelas")
        return 1
    if input_user == 0:
        return 0
    print("Input error, mohon diulangi")
    return input_func()


def masyarakat(objek):
    print(f"Selamat Datang {objek.nama}")
    print("Sosial di lingkungan Masyarakat")
    print("1.   Gotong Royong")
    print("2.   Kegiatan Ronda malam")
    print("3.   Menjenguk Tetangga")
    print("4.   Tampilkan Sosialisasi anda")
    print("5.   Kembali ke main menu")
    input_user = int(input("==> "))
    if input_user == 1:
        objek.gotong_royong()
        masyarakat(objek)
    elif input_user == 2:
        objek.kegiatan_ronda()
        masyarakat(objek)
    elif input_user == 3:
        objek.menjenguk_tetangga()
        masyarakat(objek)
    elif input_user == 4:
        objek.r_tampilkan_sosialisasi()
        masyarakat(objek)
    elif input_user == 5:
        print("Kembali ke main menu")
    else:
        print("Input Invalid, mohon diulangi \n")
        masyarakat(objek)
    

def kampus(objek):
    print(f"Selamat Datang {objek.nama}")
    print("Sosial di lingkungan Kampus")
    print("1.   Masuk Kelas")
    print("2.   Keluar dari ruangan")
    print("3.   Diskusi")
    print("4.   Kerja Kelompok")
    print("5.   Perpustakaan")
    print("6.   Mengikuti Kegiatan Organisasi")
    print("7.   Info Mahasiswa")
    print("8.   Kembali")
    input_user = int(input("==> "))
    if input_user == 1:
        objek.masuk_kelas()
    if input_user == 2:
        objek.keluar_dari_ruangan()
    if input_user == 3:
        objek.diskusi()
    if input_user == 4:
        objek.kerja_kelompok()
    if input_user == 5:
        objek._perpustakaan()
    if input_user == 6:
        objek._mengikuti_kegiatan_organisasi()
    if input_user == 7:
        objek.info()
    if input_user == 8:
        print("Kembali")
        return
    kampus(objek)

def kelas(objek):
    print(f"Selamat Datang {objek.nama}")
    print("Sosial di lingkungan Kelas")
    print("1.   Masuk Kelas")
    print("2.   Keluar dari kelas")
    print("3.   Diskusi")
    print("4.   Kerja Kelompok")
    print("5.   Belajar")
    print("6.   Presentasi")
    print("7.   Info Mahasiswa")
    print("8.   Kembali")
    input_user = int(input("==> "))
    if input_user == 1:
        objek.masuk_kelas()
    if input_user == 2:
        objek.keluar_dari_ruangan()
    if input_user == 3:
        objek.diskusi()
    if input_user == 4:
        objek.kerja_kelompok()
    if input_user == 5:
        objek.belajar()
    if input_user == 6:
        objek.presentasi()
    if input_user == 7:
        objek.info()
    if input_user == 8:
        print("Kembali")
        return
    kelas(objek)    
    

def tambah_data(kondisi):
    print("Silahkan isi data diri anda: ")
    hasil_data = data_diri()
    if kondisi is True or kondisi is False:
        if kondisi is True:
            hasil_data_masyarakat = data_diri_masyarakat()
            hdf = hasil_data + hasil_data_masyarakat
            objek = SosialMasyarakat(hdf[0], hdf[1], hdf[2], hdf[3], hdf[4], hdf[5], hdf[6], 0)
            objects_masyarakat.append(objek)
            masyarakat(objek)
        if kondisi is False:
            hasil_data_kampus = data_diri_kampus()
            hdf = hasil_data + hasil_data_kampus
            objek = SosialKampus(hdf[0], hdf[1], hdf[2], hdf[3], hdf[4], hdf[5], hdf[6], hdf[7])
            objects_kampus.append(objek)
            kampus(objek)
    else:
        if kondisi == 1:
            hasil_data_kampus = data_diri_kampus()
            hasil_data_kelas = data_diri_kelas()
            hdf = hasil_data + hasil_data_kampus + hasil_data_kelas
            objek = SosialKelas(hdf[0], hdf[1], hdf[2], hdf[3], hdf[4], hdf[5], hdf[6], hdf[7], hdf[8], hdf[9])
            objects_kelas.append(objek)
            kelas(objek)
        

def tampil_data(kondisi):
    if kondisi is True or kondisi is False:
        if kondisi is True:
            x = 0
            for i in objects_masyarakat:
                x += 1
                print(f"{x}.    {i.nama}    |   {i.NIK}")
            print("\n")
            
        if kondisi is False:
            x = 0
            for i in objects_kampus:
                x += 1
                print(f"{x}.    {i.nama}    |   {i.npm}")
            print("\n")
    else:
        if kondisi == 1:
            x = 0
            for i in objects_kelas:
                x += 1
                print(f"{x}.    {i.nama}    |   {i.npm}")
            print("\n")
    
        
def lihat_data(kondisi):
    if kondisi is True or kondisi is False:
        if kondisi is True:
            objek = objects_masyarakat
        if kondisi is False:
            objek = objects_kampus
    else:
        if kondisi == 1:
            objek = objects_kelas
    if len(objek) == 0:
        print("Data masih kosong, mohon menambahkan data terlebih dahulu")
        return
    tampil_data(kondisi)
    print("Pilih salah satu angka dari data diatas yang akan dipakai")
    input_user = int(input("==> "))
    if input_user > 0 and input_user <= len(objek):
        if kondisi is True or kondisi is False:
            if kondisi is True:
                masyarakat(objek[input_user-1])
            if kondisi is False:
                kampus(objek[input_user-1])
        else:
            if kondisi == 1:
                kelas(objek[input_user-1])

def hapus_data(kondisi):
    if kondisi is True or kondisi is False:
        if kondisi is True:
            objek = objects_masyarakat
        if kondisi is False:
            objek = objects_kampus
    else:
        if kondisi == 1:
            objek = objects_kelas
    if len(objek) == 0:
        print("Data masih kosong, mohon menambahkan data terlebih dahulu")
        return
    tampil_data(kondisi)
    print("Pilih salah satu angka dari data diatas yang akan dipakai")
    input_user = int(input("==> "))
    if input_user > 0 and input_user <= len(objek):
        objek.pop(input_user-1)


def data_diri():
    nama = input("Nama               :")
    alamat = input("Alamat             :")
    tempatLahir = input("Tempat Lahir       :")
    tanggalLahir = input("Tanggal Lahir      :")
    return [nama, alamat, tempatLahir, tanggalLahir]

def data_diri_masyarakat():
    nik = input("NIK                :")
    kelurahan = input("Kelurahan          :")
    kecamatan = input("Kecamatan          :")
    return [nik, kelurahan, kecamatan]

def data_diri_kampus():
    namaKampus = input("Nama Kampus        :")
    jurusan = input("Jurusan            :")
    fakultas = input("Fakultas           :")
    npm = input("NPM                :")
    return [namaKampus, jurusan, fakultas, npm]

def data_diri_kelas():
    kelas = input("Kelas              :")
    matakuliah = []
    print("Berapa Matakuliah yang akan diambil? (Maksimal 5)")
    def matakuliah_func():
        matakuliah_qty = int(input("==> "))
        if matakuliah_qty > 0 and matakuliah_qty <= 5:
            for i in range(matakuliah_qty):
                matakuliah.append(input(f"Matakuliah {i+1}       :"))
        else:
            print("Input invalid, mohon diulangi...")
            matakuliah_func()
    matakuliah_func()
    return [kelas, matakuliah]
main_menu()
