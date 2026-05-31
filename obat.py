from datetime import date
from produk_medis import ProdukMedis

class Obat(ProdukMedis):
    def __init__(self, id_produk, nama, harga, stok, supplier, lokasi_rak, nomor_batch, tanggal_kedaluwarsa, dosis, bentuk_sediaan):
        super().__init__(id_produk, nama, harga, stok, supplier, lokasi_rak)
        self.__nomor_batch = nomor_batch
        self.__tanggal_kedaluwarsa = tanggal_kedaluwarsa
        self.__dosis = dosis
        self.__bentuk_sediaan = bentuk_sediaan

    @property
    def nomor_batch(self): return self.__nomor_batch
    @property
    def tanggal_kedaluwarsa(self): return self.__tanggal_kedaluwarsa
    @property
    def dosis(self): return self.__dosis
    @property
    def bentuk_sediaan(self): return self.__bentuk_sediaan

    def cek_kedaluwarsa(self):
        return date.today() <= self.__tanggal_kedaluwarsa

    def cek_kelayakan_jual(self):
        if self.cek_kedaluwarsa() and self.get_stok() > 0:
            return f"{self.nama} layak dijual"
        return f"{self.nama} tidak layak dijual"
