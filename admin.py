from pengguna import Pengguna

class Admin(Pengguna):
    def __init__(self, id_user, nama, no_hp, alamat, username, password):
        super().__init__(id_user, nama, no_hp, alamat, username, password, "Admin")

    def tambah_user(self):
        print("Admin menambahkan user")

    def hapus_user(self):
        print("Admin menghapus user")

    def lihat_laporan(self):
        print("Admin melihat laporan")

    def akses_menu(self):
        while True:
            print("\n===== MENU ADMIN =====")
            print("1. Kelola User")
            print("2. Tambah Produk")
            print("3. Hapus Produk")
            print("4. Lihat Laporan")
            print("5. Logout")

            pilihan = input("Pilih menu: ")
            if pilihan == "1":
                self.tambah_user()
            elif pilihan == "2":
                print("Admin menambahkan produk")
            elif pilihan == "3":
                print("Admin menghapus produk")
            elif pilihan == "4":
                self.lihat_laporan()
            elif pilihan == "5":
                self.logout()
                break
            else:
                print("Menu tidak tersedia")
