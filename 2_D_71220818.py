nama1 = input("Masukkan nama pemain pertama:")
nama2 = input("Masukkan nama pemain kedua:")
nama3 = input("Masukkan nama pemain ketiga:")

kartu1 = input("Masukkan jumlah kartu pemain pertama:")
kartu2 = input("Masukkan jumlah kartu pemain kedua:")
kartu3 = input("Masukkan jumlah kartu pemain ketiga:")

kartu1 = int(kartu1)
kartu2 = int(kartu2)
kartu3 = int(kartu3)

if(kartu1 > 21):
    print("Jumlah kartu yang dimiliki melebihi batas")
elif(kartu2 > 21):
    print("Jumlah kartu yang dimiliki melebihi batas")  
elif(kartu3 > 21):
    print("Jumlah kartu yang dimiliki melebihi batas") 
elif(kartu1 > kartu2 and kartu1 > kartu3):
    print(nama1, "menang dengan jumlah kartu sebanyak", kartu1)
elif(kartu2 > kartu1 and kartu2 > kartu3):
    print(nama2, "menang dengan jumlah kartu sebanyak", kartu2)
else:
    print(nama3, "menang dengan jumlah kartu sebanyak", kartu3)
