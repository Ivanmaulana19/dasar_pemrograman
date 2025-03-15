is_bayar = input("apakah sudah bayar semester? (ya/tidak): ")
nilai_d = input ("apakah anda memiliki nilai d (ya/tidak): ")

if (is_bayar == 'ya' and nilai_d == 'tidak') :
    print("selamat anda lulus")
else:
    print("maaf anda tidak lulus")