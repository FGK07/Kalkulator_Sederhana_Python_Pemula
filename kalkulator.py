def operator():
    print("Masukkan jenis operator:")
    print("1.Penjumlahan")
    print("2.Pengurangan")
    print("3.Perkalian")
    print("4.Pembagian")
    print("5.Modulus")
    print("6.keluar")
    
def penjumlahan():
    angka1 = int(input("Masukkan Angka1: "))
    angka2 = int(input("Masukkan Angka2: "))
    hasil = angka1 + angka2
    print(f"hasil dari {angka1} + {angka2} adalah {hasil}")
    return hasil

def pengurangan():
    angka1 = int(input("Masukkan Angka1: "))
    angka2 = int(input("Masukkan Angka2: "))
    hasil = angka1 - angka2
    print(f"hasil dari {angka1} - {angka2} adalah {hasil}")
    return hasil

def perkalian():
    angka1 = int(input("Masukkan Angka1: "))
    angka2 = int(input("Masukkan Angka2: "))
    hasil = angka1 * angka2
    print(f"hasil dari {angka1} * {angka2} adalah {hasil}")
    return hasil

def pembagian():
    angka1 = int(input("Masukkan Angka1: "))
    angka2 = int(input("Masukkan Angka2: "))
    if angka1 == 0 or angka2 == 0:
        print("Pembagian dengan angka nol tidak bisa")
        return
    hasil = angka1 / angka2
    print(f"hasil dari {angka1} / {angka2} adalah {hasil}")
    return hasil

def modulus():
    angka1 = int(input("Masukkan Angka1: "))
    angka2 = 2
    hasil = angka1 % angka2
    print(f"hasil dari {angka1} % {angka2} adalah {hasil}")
    return hasil


while True:
    operator()
    keluar = False
    pilihan = int(input("Masukkan Pilihan: "))
    if pilihan >= 1 and pilihan < 6:
        if pilihan == 1:
            penjumlahan()
            while True:
                opsi = int(input("Masukkan angka 1 untuk mengulangi dan 0 untuk keluar "))
                if opsi >= 0 and opsi <=1:
                    if opsi == 1:
                        penjumlahan()
                    if opsi == 0:
                        break
                else:
                   print("Pilihan tidak valid. Ulangi!")
                        
        elif pilihan == 2:
            pengurangan()
            while True:
                opsi = int(input("Masukkan angka 1 untuk mengulangi dan 0 untuk keluar "))
                if opsi >= 0 and opsi <=1:
                    if opsi == 1:
                        pengurangan()
                    if opsi == 0:
                        break
                else:
                   print("Pilihan tidak valid. Ulangi!")
                   
        elif pilihan == 3:
            perkalian()
            while True:
                opsi = int(input("Masukkan angka 1 untuk mengulangi dan 0 untuk keluar "))
                if opsi >= 0 and opsi <=1:
                    if opsi == 1:
                        perkalian()
                    if opsi == 0:
                        break
                else:
                   print("Pilihan tidak valid. Ulangi!")
                   
        elif pilihan == 4:
            pembagian()
            while True:
                opsi = int(input("Masukkan angka 1 untuk mengulangi dan 0 untuk keluar "))
                if opsi >= 0 and opsi <=1:
                    if opsi == 1:
                        pembagian()
                    if opsi == 0:
                        break
                else:
                   print("Pilihan tidak valid. Ulangi!")
                   
        elif pilihan == 5:
            modulus()
            while True:
                opsi = int(input("Masukkan angka 1 untuk mengulangi dan 0 untuk keluar "))
                if opsi >= 0 and opsi <=1:
                    if opsi == 1:
                        modulus()
                    if opsi == 0:
                        break
                else:
                   print("Pilihan tidak valid. Ulangi!")
                   
        else:
            print("Pilihan tidak valid. Ulangi!")
        
    if pilihan == 6 :
        print("Anda telah keluar. Terima Kasih telah menggunakan program kalkulator sederhana ini.")
        break
    
