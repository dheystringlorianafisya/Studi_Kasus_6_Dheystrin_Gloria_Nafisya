import csv

nama = []

with open('csv/nilai.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    for row in csv_reader:
        nama.append(row)

while True:
    print("\nMenu:")
    print("1. Tampilkan data mahasiswa")
    print("2. Tambah data mahasiswa")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print("\nData Mahasiswa:")
        for row in nama:
            print(row)
    elif pilihan == "2":
        no = input("Masukkan NO: ")
        nama_mahasiswa = input("Masukkan Nama: ")
        prodi = input("Masukkan Prodi: ")
        nilai = input("Masukkan Nilai: ")

        with open('csv/nilai.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)

            writer.writerow([no, nama_mahasiswa, prodi, nilai])

        print("\nBaris baru berhasil ditambahkan ke nilai.csv!")
    elif pilihan == "3":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")