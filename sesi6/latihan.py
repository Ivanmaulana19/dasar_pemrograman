a = int(input("Masukan angka: "))
b = int(input("Masukan angka: "))
c = int(input("Masukan angka: "))   

terbesar = a
if (a >=b and a >=c) :
    terbesar = a
elif (b >=c and b >=a) :
    terbesar = b
else:
    terbesar = c
print("Angka terbesar adalah", terbesar)