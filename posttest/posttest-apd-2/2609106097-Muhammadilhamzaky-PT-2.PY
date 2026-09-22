merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

harga_merchandise = [
    merchandise_1,
    merchandise_2,
    merchandise_3,
    merchandise_4,
    merchandise_5,
    merchandise_6
]

total_harga = (
    merchandise_1 +
    merchandise_2 +
    merchandise_3 +
    merchandise_4 +
    merchandise_5 +
    merchandise_6
)

biaya_bungkus = 7500
total_harga = total_harga + biaya_bungkus
rata_rata = total_harga / len(harga_merchandise)
nim = 97 
bolean = nim > rata_rata
dolar = 16500
total_usd = total_harga / dolar
merchandise_2_sampai_4 = harga_merchandise[-5:-2]

print("Harga Merchandise 1 :", merchandise_1)
print("Harga Merchandise 2 :", merchandise_2)
print("Harga Merchandise 3 :", merchandise_3)
print("Harga Merchandise 4 :", merchandise_4)
print("Harga Merchandise 5 :", merchandise_5)
print("Harga Merchandise 6 :", merchandise_6)
print("Daftar Harga Merchandise :", harga_merchandise)
print("Biaya Bungkus Kado :", biaya_bungkus)
print("Total Harga :", total_harga)
print("Rata-rata :", rata_rata)
print("NIM :", nim)
print("Boolean (NIM > Rata-rata) :", bolean)
print("Total Harga dalam USD :", total_usd)
print("Merchandise 2 sampai 4 :", merchandise_2_sampai_4)