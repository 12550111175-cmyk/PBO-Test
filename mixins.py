class SuhuKhususMixin:
    def __init__(self, suhu_minimum, suhu_maksimum, suhu_saat_ini):
        self.__suhu_minimum = suhu_minimum
        self.__suhu_maksimum = suhu_maksimum
        self.__suhu_saat_ini = suhu_saat_ini
        self.__alarm_aktif = False

    @property
    def suhu_minimum(self): return self.__suhu_minimum
    @property
    def suhu_maksimum(self): return self.__suhu_maksimum
    @property
    def suhu_saat_ini(self): return self.__suhu_saat_ini
    @property
    def alarm_aktif(self): return self.__alarm_aktif

    def cek_suhu_aman(self):
        return self.__suhu_minimum <= self.__suhu_saat_ini <= self.__suhu_maksimum

    def update_suhu(self, suhu_baru):
        self.__suhu_saat_ini = suhu_baru
        if not self.cek_suhu_aman():
            self.aktifkan_alarm()

    def aktifkan_alarm(self):
        self.__alarm_aktif = True
        print("PERINGATAN! Suhu tidak aman!")


class BahanBerbahayaMixin:
    def __init__(self, level_bahaya):
        self.__level_bahaya = level_bahaya
        self.__catatan_penggunaan = []

    @property
    def level_bahaya(self): return self.__level_bahaya
    @property
    def catatan_penggunaan(self): return self.__catatan_penggunaan

    def validasi_izin(self):
        print("Izin penggunaan berhasil divalidasi")

    def catat_pengeluaran(self, jumlah):
        self.__catatan_penggunaan.append(jumlah)
        print(f"Pengeluaran dicatat: {jumlah}")
