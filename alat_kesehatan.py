from datetime import date
from produk_medis import ProdukMedis

class AlatKesehatan(ProdukMedis):
    def __init__(self, id_produk, nama, harga, stok, supplier, lokasi_rak, nomor_seri, tanggal_kalibrasi, kondisi):
        super().__init__(id_produk, nama, harga, stok, supplier, lokasi_rak)
        self.__nomor_seri = nomor_seri
        self.__tanggal_kalibrasi = tanggal_kalibrasi
        self.__kondisi = kondisi

    @property
    def nomor_seri(self): return self.__nomor_seri

    @property
    def tanggal_kalibrasi(self): return self.__tanggal_kalibrasi

    @property
    def kondisi(self): return self.__kondisi

    @kondisi.setter
    def kondisi(self, value):
        if value.lower() in ["baik", "rusak", "maintenance"]:
            self.__kondisi = value

    def cek_kelayakan_jual(self):
        if self.__kondisi.lower() == "baik" and self.__tanggal_kalibrasi >= date.today():
            return f"{self.nama} layak digunakan"
        return f"{self.nama} perlu maintenance"
