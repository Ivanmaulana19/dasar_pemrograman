name = input("masukan nama: ")
total = len(name)
nama = name.upper()
print(name[0:1])
print(name[0:2])
print(name[0:3])

for i in range(total):
    print(name[:i+1]+"x"*(total-1-i))

