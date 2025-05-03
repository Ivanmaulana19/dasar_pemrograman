daftar_belanja = []
for i in range (5):
    item= input(f"Masukan itemm belanja {i+1} :")
    daftar_belanja.append(item)
    
hapus =input("masukan nama item yang di beli :")

if hapus in daftar_belanja:
    daftar_belanja.remove
    print("daftar belanja setelah di hapus:")
    print(daftar_belanja)
    
else:
    print("item tidak di temukan dalam daftar.")
    print("list daftar belanja:", daftar_belanja)