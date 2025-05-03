daftar_belanja = [] 
for i in range(5):
    item = input(f"Masukan item belanja {i+1}: ")
    daftar_belanja.append(item) 

hapus = input("Masukan nama item yang dibeli (hapus): ")

if hapus in daftar_belanja:
    daftar_belanja.remove(hapus)
    print("Daftar belanja setelah dihapus:")
    print(daftar_belanja)
else:
    print("Item tidak ditemukan dalam daftar.")
    print("List daftar belanja:", daftar_belanja)
4