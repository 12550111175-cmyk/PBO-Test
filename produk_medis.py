from abc import ABC, abstractmethod

class ProdukMedis(ABC):
    def __init__(self, id_produk, nama, harga, stok, supplier, lokasi_rak):
        self.__id_produk = id_produk
        self.__nama = nama
        self.__harga = harga
        self.__stok = stok
        self.__supplier = supplier
        self.__lokasi_rak = lokasi_rak

    # GETTER
    @property
    def id_produk(self): return self.__id_produk

    @property
    def nama(self): return self.__nama

    @property
    def harga(self): return self.__harga

    @property
    def stok(self): return self.__stok

    @property
    def supplier(self): return self.__supplier

    @property
    def lokasi_rak(self): return self.__lokasi_rak

    # SETTER
    @harga.setter
    def harga(self, value):
        if value >= 0:
            self.__harga = value
        else:
            print("Harga tidak boleh negatif!")

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print(f"Stok {self.__nama} berhasil ditambah")

    def kurangi_stok(self, jumlah):
        if jumlah <= self.__stok:
            self.__stok -= jumlah
            print(f"Stok {self.__nama} berhasil dikurangi")
        else:
            print("Stok tidak mencukupi")

    def tampilkan_info(self):
        print(f"ID Produk : {self.__id_produk}")
        print(f"Nama      : {self.__nama}")
        print(f"Harga     : Rp {self.__harga}")
        print(f"Stok      : {self.__stok}")
        print(f"Supplier  : {self.__supplier}")
        print(f"Lokasi    : {self.__lokasi_rak}")

    @abstractmethod
    def cek_kelayakan_jual(self):
        pass
