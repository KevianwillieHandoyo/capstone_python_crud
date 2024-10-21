# ===================================
# Capstone Project - Hospital Patient Data
# ===================================
# Developed by Kevianwillie Handoyo
# JCDS - 0412


# /************************************/

# /===== Data Model =====/
# Create your data model here
from datetime import datetime

data = [
        {'ID': 'P1011', 'Nama': 'Ari', 'Umur': 30, 'Tanggal Masuk RS': '2020-10-01', 'Nomor Kamar': 101, 'Status': 'Normal'},
        {'ID': 'P2011', 'Nama': 'Bari', 'Umur': 35, 'Tanggal Masuk RS': '2020-10-04', 'Nomor Kamar': 201, 'Status': 'Butuh Perhatian Lebih'},
        {'ID': 'P2021', 'Nama': 'Cari', 'Umur': 52, 'Tanggal Masuk RS': '2020-10-09', 'Nomor Kamar': 202, 'Status': 'Normal'},
        {'ID': 'P3011', 'Nama': 'Dari', 'Umur': 45, 'Tanggal Masuk RS':  '2020-10-02', 'Nomor Kamar': 301, 'Status': 'Normal'},
        {'ID': 'P3021', 'Nama': 'Eri', 'Umur': 20, 'Tanggal Masuk RS': '2020-10-05', 'Nomor Kamar': 302, 'Status': 'Butuh Perhatian Lebih'}
        ]# Example data model


# /===== Feature Program =====/
# Create your feature program here
def confirmation():
    confirm = input('Konfirmasi untuk melanjutkan? (Y/N) : ')
    if confirm in ['Y','N']:
        if confirm == 'Y':
            return True
        else:
            return False
    else:
        print('Inputan tidak valid. Sillahkan masukkan Y atau N')
        confirmation()

def show_patient(data):
    tabel_data = []
    if len(data) == 0:
        print('Data kosong! Mengalihkan aplikasi ke menu utama.')
        main()
    for pasien in data:
        tabel_data.append([[pasien['ID'], pasien['Nama'], pasien['Umur'], pasien['Tanggal Masuk RS'], pasien['Nomor Kamar'], pasien['Status']]])

    for i in range(len(tabel_data)):
        id = data[i]['ID']
        nama = data[i]['Nama']
        umur = data[i]['Umur']
        tmrs = data[i]['Tanggal Masuk RS']
        nokamar = data[i]['Nomor Kamar']
        status = data[i]['Status']
        print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamar} Status: {status}')

def patient_by_id(data):
    id_pasien = input('Masukkan ID Pasien : ')
    for i in range(len(data)):
        if data[i]['ID'] == id_pasien:
            tabel_data = data[i]
            id = data[i]['ID']
            nama = data[i]['Nama']
            umur = data[i]['Umur']
            tmrs = data[i]['Tanggal Masuk RS']
            nokamar = data[i]['Nomor Kamar']
            status = data[i]['Status']
            print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamar} Status: {status}')
            return tabel_data
    print(f'Data pasien dengan ID {id_pasien} tidak tersedia')
    main()

def input_nama():
    nama = input('Masukkan nama: ')
    if all(x.isalpha() or x.isspace() for x in nama):
        return nama
    else:
        print("Input tidak boleh berisi nomor atau karakter spesial!")
        input_nama()

def input_umur():
    umur = input('Masukkan umur: ')
    if len(umur) <= 3 and umur.isdigit():
        return umur
    else:
        print("Maksimum input hanya 3 digit dan input harus hanya berisi nomor!")
        input_umur()

def input_tmrs():
    tmrs = input('Masukkan tanggal masuk RS dengan format YYYY-MM-DD: ')
    try:
        datetime.strptime(tmrs, '%Y-%m-%d')
        return tmrs
    except ValueError:
        print('Input tidak sesuai format!')
        input_tmrs()
    return

def input_nokamar():
    print('''Pilih Nomor Kamar

                1. 101
                2. 102
                3. 201
                4. 202
                5. 301
                6. 302
                ''')

    nokamar = input('Masukkan pilihan anda: ')

    if nokamar == '1':
        return 101
    elif nokamar == '2':
        return 102
    elif nokamar == '3':
        return 201
    elif nokamar == '4':
        return 202
    elif nokamar == '5':
        return 301
    elif nokamar == '6':
        return 302
    else:
        print('Input tidak tersedia pada pilihan!')
        input_nokamar()
    return

def input_status():
    print('''Pilih Status Pasien

                    1. Normal
                    2. Butuh Perhatian Lebih
                    3. Keadaan Membaik
                    ''')

    status = input('Masukkan pilihan anda: ')

    if status == '1':
        return 'Normal'
    elif status == '2':
        return 'Butuh Perhatian Lebih'
    elif status == '3':
        return 'Keadaan Membaik'
    else:
        print('Input tidak tersedia pada pilihan!')
        input_status()
    return

def id_generator(nokamar, data):
    id_increment = 1
    unique_id = f'P{nokamar}{id_increment}'
    id_list = [patient['ID'] for patient in data]

    while unique_id in id_list:
        id_increment += 1
        unique_id = f'P{nokamar}{id_increment}'
    return unique_id

def input_data(data):
    nama = input_nama()
    umur = input_umur()
    tmrs = input_tmrs()
    nokamar = input_nokamar()
    status = input_status()
    id = id_generator(nokamar, data)

    new_data = {'ID': id, 'Nama': nama, 'Umur': umur, 'Tanggal Masuk RS': tmrs, 'Nomor Kamar': nokamar, 'Status': status}
    print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamar} Status: {status}')

    confirm = confirmation()
    if confirm:
        data.append(new_data)
        print('Data telah ditambahkan')
        main()
    else:
        print('Data batal ditambahkan')
        main()
    return

def update_status(patient):
    new_status = input_status()
    if patient['Status'] == new_status:
        print('Status saat ini sama dengan status yang dipilih!')
        update_status(patient)
    confirm = confirmation()
    if confirm:
        patient['Status'] = new_status
        print('Update status berhasil')
        main()
    else:
        print('Update status dibatalkan')
        main()
    return

def delete_by_id(data, patient):
    confirm = confirmation()
    if confirm:
        data.remove(patient)
        print('Data telah dihapus')
        main()
    else:
        print('Data batal dihapus')
        main()
    return

def read(data):
    """Function for read the data
    """
    print('''======= Report Data Pasien =======

                1. Report Seluruh Data
                2. Cari Pasien Berdasarkan ID
                3. Kembali Ke Menu Utama
                ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        show_patient(data)# Fungsi tampilkan seluruh data
        main()
    elif input_user == '2':
        if len(data) == 0:
            print('Data kosong! Mengalihkan aplikasi ke menu utama.')
            main()
        else:
            patient_by_id(data)# Fungsi pasien_by_id
            main()
    elif input_user == '3':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        read(data)
    return

def create(data):
    """Function for create the data
    """
    print('''======= Tambah Data Pasien =======

                    1. Tambah Data Pasien
                    2. Kembali Ke Menu Utama
                    ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        input_data(data)# Fungsi tambah data pasien
    elif input_user == '2':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        create()
    return

def update(data):
    """Function for update the data
    """
    print('''======= Update Data Pasien =======

                        1. Update Status Pasien
                        3. Kembali Ke Menu Utama
                        ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        patient = patient_by_id(data)
        if patient:
            update_status(patient)# Fungsi update status pasien
    elif input_user == '2':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        update(data)
    return

def delete(data):
    """Function for delete the data
    """
    print('''======= Hapus Data Pasien =======

                            1. Hapus Berdasarkan ID Pasien
                            3. Kembali Ke Menu Utama
                            ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        patient = patient_by_id(data)
        if patient:
            delete_by_id(data, patient)
    elif input_user == '2':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        delete(data)
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    print('''======= Data Pasien Rumah Sakit =======

            1. Report Data Pasien
            2. Tambah Data Pasien
            3. Ubah Data Pasien
            4. Hapus Data Pasien
            5. Mengakhiri Program
            ''')

    input_user = input("Insert your option: ")
    if input_user == "1":
        read(data)
    elif input_user == "2":
        create(data)
    elif input_user == "3":
        update(data)
    elif input_user == "4":
        delete(data)
    elif input_user == "5":
        print('Aplikasi telah ditutup.')
    else:
        print("Input is not valid !")
        main()


if __name__ == "__main__":
    main()