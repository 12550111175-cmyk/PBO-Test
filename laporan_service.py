class LaporanService:
    @staticmethod
    def laporan_stok(daftar_produk):
        print("\n===== LAPORAN STOK =====")
        for produk in daftar_produk:
            print(f"{produk.nama} | Stok: {produk.get_stok()}")
