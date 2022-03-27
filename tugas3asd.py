pilihan= 0
nama_barang= ["kursi","meja"]
while pilihan <= 1:
    print ("selesai")
    print ("1. mencetak list")
    print ("2. Menambahkam nama ke dalam list")
    print ("3. Menghapus nama dari list")
    print ("4. Mengubah data dalam list")
    print ("5. Menampilkan index barang tertentu")
    print ("6. Mengetahui apakah barang sudah ada di dalam list atau belum")
    print ("9. keluar")
    menu_item = int(input("pilih menu: "))
    if menu_item == 1:
        current = 0
        if len(nama_barang) > 0:
              while current < len(nama_barang):
                print (current, ".", nama_barang[current])
                current = current + 1
        else:
              print ("list kosong")

    elif menu_item == 2 : 
            name = input("Masukkan nama: ")
            nama_barang.append(name)
            print(nama_barang)
    elif menu_item == 3:
        del_name = input("Nama yang ingin di hapus: ")
        if del_name in nama_barang:
#namelist.remove(del_name) dapat di gunakan
            item_number = nama_barang.index(del_name)
            del nama_barang[item_number]
            print(nama_barang)
#kode di atas hanya menghapus nama pertama yang ada
#kode di bawah ini menghapus semua nama
#while del_name in namelist:
#item_number = namalist.index(del_name)
#del namelist[item_number]
        else:
             print (del_name, "tidak di temukan")
    elif menu_item == 4:
        old_name = input("Nama apa yang ingin di ubah")
        if old_name in nama_barang:
            item_number = nama_barang.index(old_name)
            new_name = input("nama baru: ")
            nama_barang[item_number] = new_name
            print(nama_barang)
        else:
              print (old_name, "tidak di temukan")

    elif menu_item == 5:
         print(nama_barang)
         barang_yang_ingin_dicari = input("masukan barang yang di cari :")
         print(barang_yang_ingin_dicari,"berada pada index",nama_barang.index(barang_yang_ingin_dicari))

    elif menu_item == 6:
        barang_yang_ingin_dicari =input("masukkan barang  yang ingin di cari :")
        if barang_yang_ingin_dicari in nama_barang:
            print("barang ini terdapat dalam nama_barang")
        elif barang_yang_ingin_dicari not in nama_barang :
            print("barang ini tidak terdapat dalam nama_barang")