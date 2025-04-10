class Mahasiswa:
    def __init__(self, nama, nim, prodi, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.alamat = alamat
    
    def tampilkan_info(self):
        print(f"nama: {self.nama}, NIM: {self.nim}, prodi: {self.prodi}, alamat: {self.alamat}")


mahasiswa_list = []
for i in range(3):
    nama = input(f"masukkan nama mahasiswa {i+1}: ")
    nim = input(f"masukkan NIM mahasiswa {i+1}: ")
    jurusan = input(f"masukkan jurusan mahasiswa {i+1}: ")
    alamat = input(f"masukkan alamat mahasiswa {i+1}: ")
    mahasiswa_list.append(Mahasiswa(nama, nim, jurusan, alamat))


for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()
