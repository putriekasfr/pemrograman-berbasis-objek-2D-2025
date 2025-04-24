class MataKuliah:
    def __init__(self, kode, nama, sks):
        if not MataKuliah.cek_sks_valid(sks):
            print(f"SKS untuk {nama} tidak valid, harus 2 atau 3. mata kuliah tidak dibuat.")
            self.kode = self.nama = None
            self.sks = 0
        else:
            self.kode = kode
            self.nama = nama
            self.sks = sks

    @staticmethod
    def cek_sks_valid(sks):
        return sks in (2, 3)


class Mahasiswa:
    jumlah_mahasiswa = 0

    def __init__(self, nama, nim, prodi):
        if not Mahasiswa.validasi_nim(nim):
            print(f"NIM {nim} tidak valid. objek mahasiswa tidak dibuat.")
            self.__nama = self.__nim = self.__prodi = None
            self.__mata_kuliah = []
            return
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi
        self.__mata_kuliah = []
        Mahasiswa.jumlah_mahasiswa += 1

    def tambah_mata_kuliah(self, matkul):
        if matkul.nama:  
            self.__mata_kuliah.append(matkul)

    def tampilkan_biodata(self):
        if self.__nama is None:
            return
        print(f"Nama   : {self.__nama}")
        print(f"NIM    : {self.__nim}")
        print(f"Prodi  : {self.__prodi}")
        print("Mata Kuliah:")
        for mk in self.__mata_kuliah:
            print(f" - {mk.kode} {mk.nama} ({mk.sks} SKS)")
        print("-" * 40)

    @classmethod
    def tampilkan_jumlah_mahasiswa(cls):
        print(f"Jumlah Mahasiswa: {cls.jumlah_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return isinstance(nim, str) and nim.startswith("23") and len(nim) == 10 and nim.isdigit()


class Kampus:
    def __init__(self, nama, alamat):
        if not Kampus.validasi_nama_kampus(nama):
            print(f"nama kampus '{nama}' tidak valid (mengandung angka). objek tidak dibuat.")
            self.nama = self.alamat = None
            return
        self.nama = nama
        self.alamat = alamat

    @staticmethod
    def validasi_nama_kampus(nama):
        return not any(char.isdigit() for char in nama)


# ======================================
# DATA
# ======================================

matkul1 = MataKuliah("SI221", "ANALISA PROSES BISNIS", 2)
matkul2 = MataKuliah("UNG112", "PENDIDIKAN AGAMA ISLAM", 2)
matkul3 = MataKuliah("SI224", "DESAIN MANAJEMEN JARINGAN", 3)
matkul4 = MataKuliah("UNG118", "KEWARGANEGARAAN", 2)
matkul5 = MataKuliah("SI226", "E-BUSINESS DAN E-COMMERCE", 6)  
matkul6 = MataKuliah("SI222", "PEMROGRAMAN BERBASIS OBJEK", 3)
matkul7 = MataKuliah("SI225", "PEMROGRAMAN BERBASIS WEB", 3)
matkul8 = MataKuliah("SI223", "PENGANTAR BASIS DATA", 2)

mh1 = Mahasiswa("putri eka safira", "2304948382", "sistem informasi")
mh2 = Mahasiswa("eka safira putri", "2304411035", "sistem Informasi")
mh3 = Mahasiswa("safira putri eka", "2212332509", "pendidikan informatika")  
mh4 = Mahasiswa("shavaru erlan", "2304411567", "teknik Komputer")
mh5 = Mahasiswa("ocean yuvan", "2312345675", "pendidikan informatika")
mh6 = Mahasiswa("jericho adji", "2312345907", "sistem Informasi")

for mh in [mh1]:  
    for mk in [matkul1, matkul2, matkul3, matkul4]:
        mh.tambah_mata_kuliah(mk)
        
for mh in [mh3]:  
    for mk in [matkul3, matkul8, matkul7, matkul6]:
        mh.tambah_mata_kuliah(mk)

for mh in [mh4]:  
    for mk in [matkul3, matkul4, matkul5, matkul1]:
        mh.tambah_mata_kuliah(mk)

for mh in [mh5]:  
    for mk in [matkul5, matkul6, matkul7, matkul8]:
        mh.tambah_mata_kuliah(mk)

for mh in [mh6]:  
    for mk in [matkul2, matkul4, matkul6, matkul8]:
        mh.tambah_mata_kuliah(mk)
kampus = Kampus("universitas trunojoyo madura", "madura")  

# ======================================
# OUTPUT
# ======================================
print("\n=== DATA MAHASISWA ===")

mh1.tampilkan_biodata()

mh2.tampilkan_biodata()

mh3.tampilkan_biodata()

mh4.tampilkan_biodata()

mh5.tampilkan_biodata()

mh6.tampilkan_biodata()
print("=== INFO KAMPUS ===")
if kampus.nama:
    print(f"Nama Kampus : {kampus.nama}")
    print(f"Alamat      : {kampus.alamat}")
    print(f"Valid Nama? {'Ya' if Kampus.validasi_nama_kampus(kampus.nama) else 'Tidak'}")
else:
    print("Objek kampus tidak valid.")

Mahasiswa.tampilkan_jumlah_mahasiswa()
