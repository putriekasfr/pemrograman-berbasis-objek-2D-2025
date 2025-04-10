class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def berjalan(self):
        print(f"{self.nama} lagi berjalan.")
    
    def berlari(self):
        print(f"{self.nama} lagi berlari.")

anomali1 = Manusia("putri", 18, "bojonegoro")
anomali2 = Manusia("eka ", 17, "lamongan")
anomali3 = Manusia("safira", 19, "surabaya")
anomali4 = Manusia("ergi", 18, "gresik")
anomali5 = Manusia("shava", 19, "malang")

print(anomali1.berjalan())
print(anomali2.berlari())
print(anomali3.berlari())
print(anomali4.berjalan())
print(anomali5.berlari())