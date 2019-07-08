# Jawaban Soal Nomor 04
# Nama file: Ega Permana soal 04
# Nama: Ega Permana
# Nomor Absen: 4
# Kelas: CTA 3

# baris di bawah ini Anda mulai membuat memrogram:
print("============================================")
print("PROGRAM HAPUS VOKAL DAN CETAK KAPITAL")
print("============================================")
def hapusVokal(kalimat):
    simpan = ""
    # variabel vokal merupakan kumpulan huruf hidup
    vokal = "ieaouIEAOU"
    # variabel huruf untuk mengambil setiap huruf dari variabel teks
    for huruf in kalimat:
        # proses mengecek apakah huruf merupakan vokal
        if huruf not in vokal:
            # jika tidak maka huruf dimasukkan ke simpan
            simpan += huruf
    return simpan


text = input("Input: ")
hapusVokal(text)
print("Output :", hapusVokal(text).upper().replace(" ", ""))


#Keluaran Program
"""
============================================
PROGRAM HAPUS VOKAL DAN CETAK KAPITAL
============================================
Input: Digital Talent
Output : DGTLTLNT

Process finished with exit code 0

"""
