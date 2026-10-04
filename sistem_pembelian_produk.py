class Produk:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def info_produk(self):
        print(f"Produk: {self.nama} | Harga: Rp{self.harga:,.0f}")

    def total_pembelian(self, jumlah):
        return self.harga * jumlah

    def hitung_diskon(self, total):
        if total > 5000:
            return total * 0.05
        return 0


print("=== SISTEM PEMBELIAN PRODUK ===")

jumlah_produk = int(input("Masukkan jumlah produk: "))

total_semua = 0

for i in range(jumlah_produk):
    print(f"\nProduk ke-{i + 1}")

    nama = input("Nama produk: ")
    harga = float(input("Harga produk: Rp"))
    jumlah = int(input("Jumlah beli: "))

    produk = Produk(nama, harga)
    produk.info_produk()

    total = produk.total_pembelian(jumlah)
    print(f"Total produk: Rp{total:,.0f}")

    total_semua += total

produk_akhir = Produk("Total", 0)
diskon = produk_akhir.hitung_diskon(total_semua)
total_bayar = total_semua - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian : Rp{total_semua:,.0f}")
print(f"Diskon 5%       : Rp{diskon:,.0f}")
print(f"Total Bayar     : Rp{total_bayar:,.0f}")