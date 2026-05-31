from datetime import date

from obat_bebas import ObatBebas
from obat_resep import ObatResep
from vaksin import Vaksin
from psikotropika import Psikotropika
from alat_kesehatan import AlatKesehatan

from admin import Admin
from apoteker import Apoteker
from kasir import Kasir

from resep import Resep
from transaksi import Transaksi

from auth_service import AuthService
from inventory_service import InventoryService
from laporan_service import LaporanService

# ==========================
# OBJECT PRODUK
# ==========================
paracetamol = ObatBebas(
    id_produk="OB001",
    nama="Paracetamol",
    harga=5000,
    stok=50,
    supplier="PT Sehat",
    lokasi_rak="A1",
    nomor_batch="BATCH01",
    tanggal_kedaluwarsa=date(2026, 5, 20),
    dosis="500mg",
    bentuk_sediaan="Tablet",
    kategori_obat="Obat Bebas"
)

amoxicillin = ObatResep(
    id_produk="OB002",
    nama="Amoxicillin",
    harga=15000,
    stok=20,
    supplier="PT Farma",
    lokasi_rak="B1",
    nomor_batch="BATCH02",
    tanggal_kedaluwarsa=date(2025, 12, 20),
    dosis="250mg",
    bentuk_sediaan="Kapsul",
    nomor_resep="RSP001"
)

vaksin = Vaksin(
    id_produk="OB003",
    nama="Vaksin COVID",
    harga=100000,
    stok=10,
    supplier="PT Bio",
    lokasi_rak="FREEZER",
    nomor_batch="BATCH03",
    tanggal_kedaluwarsa=date(2027, 1, 1),
    dosis="1ml",
    bentuk_sediaan="Injeksi",
    suhu_minimum=2,
    suhu_maksimum=8,
    suhu_saat_ini=5
)

psikotropika = Psikotropika(
    id_produk="OB004",
    nama="Diazepam",
    harga=25000,
    stok=5,
    supplier="PT Medika",
    lokasi_rak="LEMARI KHUSUS",
    nomor_batch="BATCH04",
    tanggal_kedaluwarsa=date(2025, 11, 10),
    dosis="10mg",
    bentuk_sediaan="Tablet",
    nomor_resep="RSP002",
    level_bahaya="Tinggi"
)

thermometer = AlatKesehatan(
    id_produk="ALK001",
    nama="Thermometer Digital",
    harga=75000,
    stok=15,
    supplier="PT Alkes",
    lokasi_rak="C1",
    nomor_seri="SR001",
    tanggal_kalibrasi=date(2026, 1, 1),
    kondisi="Baik"
)

semua_produk = [paracetamol, amoxicillin, vaksin, psikotropika, thermometer]

# ==========================
# USER
# ==========================
admin = Admin(
    id_user="USR01",
    nama="Bintang",
    no_hp="082247497172",
    alamat="Riau",
    username="admin",
    password="admin123"
)

apoteker = Apoteker(
    id_user="USR02",
    nama="Rian, S.Farm",
    no_hp="08123456789",
    alamat="Pekanbaru",
    username="apoteker",
    password="apoteker123",
    nomor_sip="SIP001"
)

kasir = Kasir(
    id_user="USR03",
    nama="Siti",
    no_hp="08987654321",
    alamat="Padang",
    username="kasir",
    password="kasir123",
    kode_kasir="KSR001"
)

semua_user = [admin, apoteker, kasir]

# ==========================
# LOGIN
# ==========================
print("\n===== LOGIN SISTEM =====")
username = input("Username : ")
password = input("Password : ")

user_login = AuthService.login(semua_user, username, password)

if user_login:
    print(f"\nSelamat datang {user_login.username}")
    user_login.akses_menu()
else:
    print("Login gagal")

# ==========================
# TAMPILKAN PRODUK
# ==========================
InventoryService.tampilkan_semua_produk(semua_produk)

# ==========================
# POLYMORPHISM
# ==========================
print("\n===== POLYMORPHISM =====")
for produk in semua_produk:
    print(produk.cek_kelayakan_jual())

# ==========================
# MIXIN
# ==========================
print("\n===== MIXIN =====")
print(f"Status Suhu Vaksin Aman: {vaksin.cek_suhu_aman()}")
psikotropika.validasi_izin()
psikotropika.catat_pengeluaran(2)

# ==========================
# RESEP
# ==========================
resep = Resep("R001", "Dr. Andi", "Budi")
resep.tambah_obat(amoxicillin)
print("\n===== RESEP DOKTER =====")
resep.tampilkan_resep()

# ==========================
# TRANSAKSI
# ==========================
transaksi = Transaksi("TRX001")
transaksi.tambah_item(paracetamol, 2)
transaksi.tambah_item(thermometer, 1)
transaksi.cetak_invoice()

# ==========================
# LAPORAN STOK
# ==========================
LaporanService.laporan_stok(semua_produk)

# ==========================
# INPUT TAMBAH STOK
# ==========================
print("\n===== INPUT STOK =====")
nama_produk = input("Masukkan nama produk: ")
jumlah = int(input("Jumlah stok tambahan: "))

for produk in semua_produk:
    if produk.nama.lower() == nama_produk.lower():
        produk.tambah_stok(jumlah)
        print(f"Stok terbaru {produk.nama}: {produk.get_stok()}")
        break
else:
    print("Produk tidak ditemukan")
