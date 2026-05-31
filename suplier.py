class Supplier:
    def __init__(self, id_supplier, nama_supplier, alamat):
        self.__id_supplier = id_supplier
        self.__nama_supplier = nama_supplier
        self.__alamat = alamat

    @property
    def id_supplier(self): return self.__id_supplier
    @property
    def nama_supplier(self): return self.__nama_supplier
    @property
    def alamat(self): return self.__alamat

    def tampilkan_supplier(self):
        print(f"Supplier : {self.__nama_supplier}")
        print(f"Alamat   : {self.__alamat}")
