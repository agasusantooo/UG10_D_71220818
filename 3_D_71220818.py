tahun = input("Masukkan Tahun: ")
tahun = int(tahun)
if(tahun%4 == 0):
    print(tahun, "merupakan Tahun Kabisat.")
elif(tahun%400 == 0):
    print(tahun, "merupakan Tahun Kabisat.")
else:
    print(tahun, "bukan merupakan Tahun Kabisat.")