class Ayam:
    def __init__(self, nama, warna, usia):  
        self.nama = nama
        self.warna = warna
        self.usia = usia

    def suara(self):
        return "kukuruyuk"

    def tampilkan_info(self):
        print(f"ayam: {self.nama}, warna: {self.warna}, usia: {self.usia}, suara: {self.suara()}")


class Kucing:
    def __init__(self, nama, ras, usia):  
        self.nama = nama
        self.ras = ras
        self.usia = usia

    def suara(self):
        return "miaww"

    def tampilkan_info(self):
        print(f"kucing: {self.nama}, ras: {self.ras}, usia: {self.usia}, suara: {self.suara()}")


class Sapi:
    def __init__(self, nama, jenis, warna):  
        self.nama = nama
        self.jenis = jenis
        self.warna = warna

    def suara(self):
        return "mmoooo"

    def tampilkan_info(self):
        print(f"sapi: {self.nama}, jenis: {self.jenis}, warna: {self.warna}, suara: {self.suara()}")


ayam_list = [
    Ayam("sky", "merah", "2 bulan"),
    Ayam("zapin", "putih", "4 bulan"),
    Ayam("yuvan", "hitam", "1 bulan")
]

kucing_list = [
    Kucing("tamtam", "persia", "7 bulan"),
    Kucing("dendeng", "anggora", "4 bulan"),
    Kucing("wortel", "kucing kampung", "1 tahun")   
]

sapi_list = [
    Sapi("yoya", "brahman", "9 tahun"),
    Sapi("nova", "simental", "7 tahun"),
    Sapi("slamet", "limousin", "5 tahun")
]



print("= daftar ayam =")
for ayam in ayam_list:
    ayam.tampilkan_info()
    

print("= daftar kucing =")
for kucing in kucing_list:
    kucing.tampilkan_info()


print("= daftar sapi =")
for sapi in sapi_list:
    sapi.tampilkan_info()
    
