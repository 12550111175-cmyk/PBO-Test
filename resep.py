class Resep:
    def __init__(self, id_resep, nama_dokter, nama_pasien):
        self.__id_resep = id_resep
        self.__nama_dokter = nama_dokter
        self.__nama_pasien = nama_pasien
        self.__daftar_obat = []

    @property
    def id_resep(self): return self.__id_resep
    @property
    def nama_dokter(self): return self.__nama_dokter
    @property
    def nama_pasien(self): return self.__nama_pasien
    @property
    def daftar_obat(self): return self.__daftar_obat

    def tambah_obat(self, obat):
        self.__daftar_obat.append(obat)

    def tampilkan_resep(self):
        print(f"ID Resep : {self.__id_resep}")
        print(f"Dokter   : {self.__nama_dokter}")
        print(f"Pasien   : {self.__nama_pasien}")
        for obat in self.__daftar_obat:
            print(f"- {obat.nama}")
