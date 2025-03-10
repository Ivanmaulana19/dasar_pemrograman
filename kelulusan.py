def cek_kelulusan(full_bayar, rata_rata_nilai):
    if full_bayar and rata_rata_nilai >=75:
        return "lulus"
    else :
        return "tidak lulus"
    