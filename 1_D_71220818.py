print("\(^0^) Selamat datang di Kalkulator Sederhana (^0^)/")
print("Ketik 1 untuk menghitung penjumlahan.")
print("Ketik 2 untuk menghitung pengurangan.")
print("Ketik 3 untuk menghitung perkalian.")
print("Ketik 4 untuk menghitung pembagian.")
print("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
print("Ketik 6 untuk menghitung pemangkatan.")

operasi = input("Masukkan pilihan Anda :")
angka1 = input("Masukkan bilangan pertama :")
angka2 = input("Masukkan bilangan kedua :")
operasi = int(operasi)
angka1 = int(angka1)
angka2 = int(angka2)
if(operasi == 1) :
    print("Hasil dari", angka1, "dijumlahkan dengan", angka2, "adalah", angka1 + angka2)
elif(operasi == 2) :
    print("Hasil dari", angka1, "dikurangkan dengan", angka2, "adalah", angka1 - angka2)
elif(operasi == 3) :
    print("Hasil dari", angka1, "dikalikan dengan", angka2, "adalah", angka1 * angka2)
elif(operasi == 4) :
    print("Hasil dari", angka1, "dibagi dengan", angka2, "adalah", angka1 / angka2)
elif(operasi == 5) :
    print("Hasil dari", angka1, "dimodulus dengan", angka2, "adalah", angka1 % angka2)
else:
    print("Hasil dari", angka1, "dipangkatkan dengan", angka2, "adalah", angka1 ** angka2)