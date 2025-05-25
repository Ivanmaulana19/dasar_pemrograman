def hitung_diskon(harga, presentase_diskon):
    diskon = harga * (presentase_diskon /100)
    return max(harga - diskon, 0)

def hitung_pajak(harga, presentase_pajak):
    return harga * (presentase_pajak /100)
def hitung_total(harga, presentase_diskon, presentase_pajak):
    harga_setelah_diskon = hitung_diskon(harga, presentase_diskon)
    pajak = hitung_pajak(harga_setelah_diskon, presentase_pajak)
    return harga_setelah_diskon + pajak