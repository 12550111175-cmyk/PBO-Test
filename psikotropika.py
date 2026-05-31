from obat_resep import ObatResep
from mixins import BahanBerbahayaMixin

class Psikotropika(ObatResep, BahanBerbahayaMixin):
    def __init__(self, *args, level_bahaya, **kwargs):
        ObatResep.__init__(self, *args, **kwargs)
        BahanBerbahayaMixin.__init__(self, level_bahaya)
