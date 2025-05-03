nama = input ("masukan nama: ") 
    if len(nama) < 7:
        print("masukan nama kalian minimal 7 huruf")
    else :
        for i in range(len(nama)):
            print(nama [:i+1] +'*' * (7-(i+1))):azzaza