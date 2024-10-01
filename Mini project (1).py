print("-----------------------------------------------------------------------------------")
print("Program Menghitung Total Harga Barang Berdasarkan Harga Barang dan Jumlah Pembelian")
print("-----------------------------------------------------------------------------------")

print("Selamat Datang di Cawmarket")
print("Silahkan scan keanggotaan anda terlebih")
Username = input("Masukkan Nama: ")
PIN = input("Masukkan Pin: ")
print("Anda teerdaftar sebagai member, selamat berbelanja")

harga = float(input("Harga Produk: "))
jumlah = int(input("Jumlah Produk: "))
total = harga * jumlah
print("Keseluruhan harga:", total)

if  total > 250000:
    diskon = total * 0.25 
    total -= diskon 
    print("Harga setelah diskon: ", total)
else: 
   print("Maaf, Anda tidak mendapat diskon")

while True:
  kembali = input("Apakah ada lagi yang ingin dibeli lagi? (ya/tidak): ")
 
  if kembali == 'ya':
    harga = float(input("Harga Produk: "))
    jumlah = int(input("Jumlah Produk: "))
    total = harga * jumlah
    print("Keseluruhan harga:", total)
  if total > 250000:
    diskon = total * 0.25 
    total -= diskon 
    print("Harga setelah diskon: ", total)
  else: 
   print("Maaf, Anda tidak mendapat diskon")

else:
  print("Terima Kasih telah berbelanja di cawmarket, Ditunggu kedatangan anda berikutnya")
