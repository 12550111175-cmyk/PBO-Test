from abc import ABC, abstractmethod

class Pengguna(ABC):
    def __init__(self, id_user, nama, no_hp, alamat, username, password, role):
        self.__id_user = id_user
        self.__nama = nama
        self.__no_hp = no_hp
        self.__alamat = alamat
        self.__username = username
        self.__password = password
        self.__role = role
        self.__status_login = False

    # GETTER (Kontrol Akses Baca)
    @property
    def id_user(self): return self.__id_user

    @property
    def nama(self): return self.__nama

    @property
    def no_hp(self): return self.__no_hp

    @property
    def alamat(self): return self.__alamat

    @property
    def username(self): return self.__username

    @property
    def role(self): return self.__role

    @property
    def status_login(self): return self.__status_login

    # SETTER (Kontrol Akses Tulis + Validasi)
    @nama.setter
    def nama(self, value):
        if value.strip():
            self.__nama = value
        else:
            print("Nama tidak boleh kosong!")

    @no_hp.setter
    def no_hp(self, value):
        if value.isdigit():
            self.__no_hp = value
        else:
            print("Nomor HP harus berupa angka!")

    def login(self, username_input, password_input):
        if username_input == self.__username and password_input == self.__password:
            self.__status_login = True
            print(f"Login berhasil sebagai {self.__role}")
            return True
        return False

    def logout(self):
        self.__status_login = False
        print(f"{self.__username} logout")

    def ubah_password(self, password_lama, password_baru):
        if password_lama == self.__password:
            if len(password_baru) >= 6:
                self.__password = password_baru
                print("Password berhasil diubah")
            else:
                print("Password baru terlalu pendek (Minimal 6 karakter)!")
        else:
            print("Password lama salah")

    @abstractmethod
    def akses_menu(self):
        pass
