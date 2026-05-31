from pengguna import Pengguna

class Apoteker(Pengguna):
    def __init__(self, id_user, nama, no_hp, alamat, username, password, nomor_sip):
        super().__init__(id_user, nama, no_hp, alamat, username, password, "Apoteker")
        self.__nomor_sip = nomor_sip

    @property
    def nomor_sip(self):
        return self.__nomor_sip

    @nomor_sip.setter
    def nomor_sip(self, value):
        if value.strip():
            self.__nomor_sip = value

    def validasi_resep(self):
        print("Resep berhasil divalidasi")

    def cek_obat(self):
        print("Apoteker mengecek obat")

    def monitoring_suhu(self):
        print("Monitoring suhu vaksin")

    def akses_menu(self):
        while True:
            print("\n===== MENU APOTEKER =====")
            print("1. Validasi Resep")
            print("2. Cek Obat")
            print("3. Tambah Stok")
            print("4. Monitoring Suhu")
            print("5. Logout")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                self.validasi_resep()
            elif pilihan == "2":
                self.cek_obat()
            elif pilihan == "3":
                print("Tambah stok dilakukan")
            elif pilihan == "4":
                self.monitoring_suhu()
            elif pilihan == "5":
                self.logout()
                break
            else:
                print("Menu tidak tersedia")
