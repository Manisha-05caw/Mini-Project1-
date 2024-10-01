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
print("Total harga:", total)

if  total > 250000:
    diskon = total * 0.25 
    total -= diskon 
    print("Keseluruhan harga: ", total)
else: 
   print("Maaf, Anda tidak mendapat diskon")

while True:
  lanjut = input("Apakah ada lagi yang ingin dibeli lagi? (y/t): ")
 
  if lanjut == 'y':
    harga = float(input("Harga Produk: "))
    jumlah = int(input("Jumlah Produk: "))
    total = harga * jumlah

  else:
    print("Terima Kasih telah berbelanja di cawmarket, Ditunggu kedatangan anda berikutnya")

    break