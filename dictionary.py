# Jawaban Soal Nomor 05
# Nama file: Ega Permana soal 05.py
# Nama: Ega Permana
# Nomor Absen: 4
# Kelas: CTA 3

# baris di bawah ini Anda mulai membuat memrogram:
print("=====================")
print("PROGRAM DICTIONARY")
print("=====================")

pesertaCTA={'nama':'EGA PERMANA','kelas':'CTA3','noabsen':'004'}

for k in pesertaCTA.keys() :
    print(k)

pesertaCTA['nilai_kuis'] = [70,80,90,95,100]
print(pesertaCTA)

jml=0
for x in pesertaCTA['nilai_kuis']:
    jml += x
rataNilai = jml/5
print("Nilai Rata-Rata",rataNilai)

#Hasil keluaran
"""
=====================
PROGRAM DICTIONARY
=====================
nama
kelas
noabsen
{'nama': 'EGA PERMANA', 'kelas': 'CTA3', 'noabsen': '004', 'nilai_kuis': [70, 80, 90, 95, 100]}
Nilai Rata-Rata 87.0

Process finished with exit code 0
"""
