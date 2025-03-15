def ambil_pilihan_komputer():
    return random.choice(["batu", "kertas", "gunting"])
def tentukan_pemenang(pilihan_pemain, pilihan_komputer):
    if pilihan_pemain == pilihan_komputer :
        return "Seri"
    elif (pilihan_pemain == 'batu' and pilihan_komputer == 'gunting') or \
         (pilihan_pemain == 'gunting' and pilihan_komputer == 'kertas') or\
         (pilihan_pemain == 'kertas' and pilihan_komputer == 'batu'):
         return "pemain pemenang"
    else :
        return "komputer menang"
    
def main():
    skor_pemain = 0 
    skor_komputer = 0

    while True:
        print("\nPilihan: batu,gunting, kertas")
        pilihan_pemain = input("masukkan pilihan anda: ").lower()
        print("Pilian tidak valid, Silahkan coba lagi.")
        continue
    pilihan_komputer = ambil_pilihan_omputer()
    print(f"pilihan kompter: {pilihan_komputer}")

    hasil = tentukan_pemenang(pilihan_pemain, pilihan_komputer)
    print(hasil)
    
    if hasil == "pemain menang":
        skor_pemain += 1
    elif hasil == "komputer menang":
        skor_komputer += 1
