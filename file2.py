
def soal():
    print('''D0221360
    gaji_pokok =1.000.000
    gaji_lembur/jam =6.000
    lama_lembur = sesuai dari angka terakhir nim
    gaji_lemburnya =(gaji_lembur/jam)lama_lembur
    pajak = 11%''')
jumlah_gaji_lembur = 6000*60
gaji_kena_pajak = 1000000*11/100
gaji_kotor =1000000 + jumlah_gaji_lembur
gaji_bersih = gaji_kotor - gaji_kena_pajak
soal()
print("nama:suryandini (D0221360)")
print("gaji pokok : 1000000")
print("gaji lembur :",jumlah_gaji_lembur)
print("gaji kotor :",gaji_kotor)
print("pajak:", 11/100)
print("potongan :", gaji_kena_pajak)
print("gaji_bersih :", gaji_bersih)
