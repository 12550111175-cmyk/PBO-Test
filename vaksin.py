from obat import Obat
from mixins import SuhuKhususMixin

class Vaksin(Obat, SuhuKhususMixin):
    def __init__(self, *args, suhu_minimum, suhu_maksimum, suhu_saat_ini, **kwargs):
        Obat.__init__(self, *args, **kwargs)
        SuhuKhususMixin.__init__(self, suhu_minimum, suhu_maksimum, suhu_saat_ini)
