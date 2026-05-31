class Transaksi:
    def __init__(self, id_transaksi):
        self.__id_transaksi = id_transaksi
        self.__daftar_produk = []
        self.__total_harga = 0

    @property
    def id_transaksi(self): return self.__id_transaksi
    @property
    def daftar_produk(self): return self.__daftar_produk
    @property
    def total_harga(self): return self.__total_harga

    def tambah_item(self, produk, jumlah):
        self.__daftar_produk.append((produk, jumlah))
        self.__total_harga += produk.get_harga() * jumlah

    def cetak_invoice(self):
        print("\n===== INVOICE =====")
        for produk, jumlah in self.__daftar_produk:
            subtotal = produk.get_harga() * jumlah
            print(f"{produk.nama} x{jumlah} = Rp {subtotal}")
        print(f"Total = Rp {self.__total_harga}")
