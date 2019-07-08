# Jawaban Soal Nomor 02
# Nama file: Ega Permana soal 02
# Nama: Ega Permana
# Nomor Absen: 4
# Kelas: CTA 3
# Instruktur : Nurhamid, P.Hd


# baris di bawah ini Anda mulai membuat memrogram:
print("============================================")
print("PROGRAM MENENTUKAN KONDISI BERAT BADAN ANDA")
print("============================================")

berat_badan= float(input("Ketik berat badan Anda (dl Kg) di sini  : "))
tinggi_badan= float(input("Ketik tinggi badan Anda (dl m) di sini : "))
tinggiDlmMeter=tinggi_badan/100
BMI=berat_badan/(tinggiDlmMeter*tinggiDlmMeter)
if BMI < 18.5:
    print ('underweight' )
elif BMI >= 18.5 and BMI <= 22.9:
    print ('normal')
else:
    print('overweight')


#Keluaran Program
"""
============================================
PROGRAM MENENTUKAN KONDISI BERAT BADAN ANDA
============================================
Ketik berat badan Anda (dl Kg) di sini  : 67
Ketik tinggi badan Anda (dl m) di sini : 170
overweight
Process finished with exit code 0

"""
