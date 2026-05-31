from obat import Obat

class ObatBebas(Obat):
    def __init__(self, *args, kategori_obat, **kwargs):
        super().__init__(*args, **kwargs)
        self.__kategori_obat = kategori_obat

    @property
    def kategori_obat(self):
        return self.__kategori_obat

    def tampilkan_label(self):
        print(f"Kategori Obat: {self.__kategori_obat}")
