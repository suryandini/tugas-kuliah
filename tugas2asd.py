#Tipe data List adalah tipe data yang di tandai dengan kurung siku [] yang bersifat ordered (terurut)
# dan juga bersifat changable (bisa di ubah). 
#tipe data list juga bisa menggabungkan beberapa nilai tipe data seperti string,float,integer, dan boolean
#contoh tipe data list dalam perulangan 
data_list =["dini",14,1.7,False,12]
i=0
for i in (data_list):
    print(i)
data_list[2]="alika" #update
print(data_list)
data_list.remove(14) #menghapus
print(data_list)
data_list.append(13) #menambahkan
print(data_list)

#tipe data tuple dapat di defenisikan dengan tanda kurung ()
#adalah tipe data struktur data yang digunakan untuk menyimpan sekumpulan data.
#tuple data bersifat immutable, artinya isi tuple tidak bisa di ubah dan di hapus
#tuple juga berguna untuk menyimpan lebih dari satu nilai dalam satu variabel secara sekaligus
#contoh data tuple
angka =(10,20,30,40,50,60,70)
print(angka, type(angka))
for i in angka:   #perulangan
    print(i)

#tipe data set adalah tipe data yang di gunakan untuk menyimpan banyak nilai dalam satu variabel
#dan yang tidak beraturan serta memiliki nilai yang unik (tidak duplikat).jika terdapat dua atau lebih
#nilai yang sama, maka set akan menyimpan hanya satu nilai dari nilai yang sama dan sisanya akan di hilangkan
#tipe data set di tandai dengan kurung kurawal{}
#contoh tipe data set   
data_set ={"andini","afifa","naya",1,2,3}
i=0
while i<2:
    print(data_set)#perulangan
    i+=1
data_set.remove("andini")
print(data_set) #menghapus
data_set.add(30) #menambahkan
print(data_set)

#tipe data dictionary
#dalam pembuatan tipe data dictionary, dapat di tandai dengan tanda{} 
#selain itu setiap elemen merupakan pasangan dari key dan value.
#antara satu dengan elemen lain di pisah dengan tanda koma
data_dictionary ={
"nama":"suryandini",
"umur":"17 tahun",
"alamat":"mambi"}
i=0
while i<2:
    print(data_dictionary) #perulangan
    i+=2
data_dictionary["nama"]="taslim" #update
print(data_dictionary)
data_dictionary["umur"]="15 tahun"
print(data_dictionary)
del data_dictionary["alamat"] #menghapus
print(data_dictionary)