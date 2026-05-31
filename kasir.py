from pengguna import Pengguna

class Kasir(Pengguna):
    def __init__(self, id_user, nama, no_hp, alamat, username, password, kode_kasir):
        super().__init__(id_user, nama, no_hp, alamat, username, password, "Kasir")
        self.__kode_kasir = kode_kasir

    @property
    def kode_kasir(self):
        return self.__kode_kasir

    def proses_pembayaran(self):
        print("Pembayaran berhasil")

    def cetak_struk(self):
        print("Struk berhasil dicetak")

    def akses_menu(self):
        while True:
            print("\n===== MENU KASIR =====")
            print("1. Transaksi")
            print("2. Pembayaran")
            print("3. Cetak Struk")
            print("4. Logout")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                print("Kasir melakukan transaksi")
            elif pilihan == "2":
                self.proses_pembayaran()
            elif pilihan == "3":
                self.cetak_struk()
            elif pilihan == "4":
                self.logout()
                break
            else:
                print("Menu tidak tersedia")
