from obat import Obat

class ObatResep(Obat):
    def __init__(self, *args, nomor_resep, perlu_resep=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.__nomor_resep = nomor_resep
        self.__perlu_resep = perlu_resep

    @property
    def nomor_resep(self): return self.__nomor_resep
    @property
    def perlu_resep(self): return self.__perlu_resep

    def validasi_resep(self):
        print("Resep berhasil divalidasi")

    def proses_penjualan(self):
        print(f"Obat resep {self.nama} diproses")
