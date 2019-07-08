# Jawaban Soal Nomor 06
# Nama file: Ega Permana soal 06_revisi.py
# Nama: Ega Permana
# Nomor Absen: 4
# Kelas: CTA 3

# baris di bawah ini Anda mulai membuat memrogram:

class Rekening:
    limit = 1000

    def __init__(self):
        global limit
        self.saldo = 500

    def kredit(self, jumlahK):
        if jumlahK > self.limit * 4:
            print("Nilai kredit melebihi 4 x batas limit kredit")
            return
        else:
            if jumlahK < 0:
                print("Jumlah tidak boleh kurang dari 0 ")
                return
            else:
                self.saldo += jumlahK

    def debit(self, jumlahD):
        if jumlahD > self.limit:
            print("Anda melebihi batas limit")
        else:
            if jumlahD > self.saldo:
                print("Jumlah lebih dari saldo")
                return
            elif jumlahD < 0:
                print("tidak boleh 0")
                return
            else:
                self.saldo -= jumlahD

    def cetakSaldo(self):
        return print("Jumlah Saldo Anda saat ini adalah : ", str(self.saldo))


rekBank = Rekening()
print("=========================")
print("PROGRAM TABUNGAN")
print("=========================")
rekBank.cetakSaldo()
print("Nilai Limit Saldo Anda adalah     : ", str(rekBank.limit))
jumlahD = int(input("\nMasukkan angka Debit "))
rekBank.debit(jumlahD)
rekBank.cetakSaldo()
jumlahK = int(input("\nMasukkan angka Kredit "))
rekBank.kredit(jumlahK)
rekBank.cetakSaldo()

#Hasil keluaran
"""
=========================
PROGRAM TABUNGAN
=========================
Jumlah Saldo Anda saat ini adalah :  500
Nilai Limit Saldo Anda adalah     :  1000

Masukkan angka Debit 6000
Anda melebihi batas limit
Jumlah Saldo Anda saat ini adalah :  500

Masukkan angka Kredit 2000
Jumlah Saldo Anda saat ini adalah :  2500

Process finished with exit code 0
"""
