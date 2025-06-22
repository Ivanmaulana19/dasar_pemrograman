from ecommerce.pricing import hitung_diskon, hitung_pajak, hitung_total
from ecommerce.order import generate_order_id

def main():
    nama_pelanggan = input ("Masukan nama pelanggan: ")
    nama_produk = input("masukan nama produk:")
    harga_asli = float(input("masukan harga asli: "))
    presentase_diskon = float(input("masukan presentase diskon: "))
    presentase_pajak = float(input("Masukan presentase pajak: "))
    
    diskon = harga_asli * (presentase_diskon / 100)
    total = hitung_total(harga_asli, presentase_diskon, presentase_pajak)
    order_id = generate_order_id()
    #hasil
    print("="*40)
    print(" RINCIAN PEMBELIAN")
    print("="*40)
    print(f"{ 'ID Pesanan' :20} {order_id}")
    print(f"{'Nama Pelanggan':20}: {nama_pelanggan}")
    print(f"{'Nama Produk':20} :{nama_produk}")
    print(f"{'harga Asli':20}: Rp {harga_asli:,.2f}")
    print(f"{'Diskon':20}: Rp {hitung_pajak(harga_asli - diskon, presentase_pajak):,.2f}")
    print("-"*40)
    print(f"{'total Belanja':20}: Rp {total:,.2f}")
    print("="*40)
    
if __name__== "__main__":
    main()