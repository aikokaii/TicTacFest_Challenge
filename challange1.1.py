import math
name = input("Masukan nama anda : ")
n = float(input("Masukan panjang persegi name tag (cm) : "))
m = float(input("Masukan panjang trapesium name tag (cm) : "))
jumlah = int(input("Masukan jumlah name tag : "))
#menghitung luas persegi
luas_pesergi = n * n
#menghitung luas segitiga
luas_segitiga = n/2 * n
#menghitung luas trapesium
luas_trapesium = (n + m) * n / 2
#menghitung luas setengah lingkaran
luas_setengahlingkaran = (math.pi * (n/2)**2) / 2
#menghitung luas total
jumlah_luas = luas_pesergi + luas_segitiga + luas_trapesium + luas_setengahlingkaran
jumlah_luas = round(jumlah_luas, 2)
total_luas = jumlah_luas * jumlah
#menghitung uang yang perlu dibayarkan
uang = total_luas * 0.40
uang = math.ceil(uang/1000) * 1000
#print semua le aowkoakwow
print(f"Haloo {name}, Berikut adalah rincian name tag yang anda pesan :")
print(f"Luas name tag : {jumlah_luas} cm2")
print(f"Total luas name tag : {total_luas} cm2")
print(f"Jumlah name tag : {jumlah} pcs")
print(f"Total yang perlu dibayarkan : Rp {uang}")
