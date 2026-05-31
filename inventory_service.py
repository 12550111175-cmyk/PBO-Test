class InventoryService:
    @staticmethod
    def tampilkan_semua_produk(daftar_produk):
        print("\n===== DAFTAR PRODUK =====")
        for produk in daftar_produk:
            produk.tampilkan_info()
            print(produk.cek_kelayakan_jual())
            print("-------------------")
