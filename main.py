# ===================================
# Capstone Project - Hospital Patient Data
# ===================================
# Developed by Kevianwillie Handoyo
# JCDS - 0412


# /************************************/

# /===== Data Model =====/
# Create your data model here
from datetime import datetime
import mysql.connector

# data = [
#         {'ID': 'P1011', 'Nama': 'Ari', 'Umur': 30, 'Tanggal Masuk RS': '2020-10-01', 'Nomor Kamar': 101, 'Status': 'Normal'},
#         {'ID': 'P2011', 'Nama': 'Bari', 'Umur': 35, 'Tanggal Masuk RS': '2020-10-04', 'Nomor Kamar': 201, 'Status': 'Butuh Perhatian Lebih'},
#         {'ID': 'P2021', 'Nama': 'Cari', 'Umur': 52, 'Tanggal Masuk RS': '2020-10-09', 'Nomor Kamar': 202, 'Status': 'Normal'},
#         {'ID': 'P3011', 'Nama': 'Dari', 'Umur': 45, 'Tanggal Masuk RS':  '2020-10-02', 'Nomor Kamar': 301, 'Status': 'Normal'},
#         {'ID': 'P3021', 'Nama': 'Eri', 'Umur': 20, 'Tanggal Masuk RS': '2020-10-05', 'Nomor Kamar': 302, 'Status': 'Butuh Perhatian Lebih'}
#         ]# Example data model

def create_connection(db: str):

    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password',
            database=db
        )

        print('Connection success!')
        return conn


    except Exception as e:
        print(f'Error connecting to database: {e}')

def execute_query(conn: object, query: str):
    # Create access to database
    myCursor = conn.cursor()

    # Access to query
    myCursor.execute(query)

    return myCursor.fetchall(), myCursor.column_names

conn = create_connection('rumahsakit')


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

def show_patient(conn):
    query = ''' SELECT * FROM pasien
                JOIN kamarrawatinap ON kamarrawatinap.kamarID = pasien.kamarID
            '''
    data, column_names = execute_query(conn, query)

    if len(data) == 0:
        print('Data kosong! Mengalihkan aplikasi ke menu utama.')
        main()

    for pasien in data:
        id = pasien[0]
        nama = pasien[1]
        umur = pasien[2]
        tmrs = pasien[3]
        nokamar = pasien[6]
        print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamar}')


def show_staff(conn):
    query = ''' SELECT * FROM staff
                JOIN kamarrawatinap ON kamarrawatinap.kamarID = staff.kamarID
            '''
    data, column = execute_query(conn, query)

    if len(data) == 0:
        print('Data kosong! Mengalihkan aplikasi ke menu utama.')
        main()

    for staff in data:
        id = staff[0]
        nama = staff[1]
        posisi = staff[2]
        nokamar = staff[5]
        print(f'ID: {id} Nama: {nama} Posisi: {posisi} Nomor Kamar: {nokamar}')

def patient_by_id(conn):
    id_pasien = input('Masukkan ID Pasien : ')
    query =f''' SELECT * FROM pasien
                JOIN kamarrawatinap ON kamarrawatinap.kamarID = pasien.kamarID
                WHERE pasienID = '{id_pasien}'
            '''
    try:
        data, column_names = execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()

    if len(data) == 0:
        print('Data kosong! Mengalihkan aplikasi ke menu utama.')
        main()

    for pasien in data:
        id = pasien[0]
        nama = pasien[1]
        umur = pasien[2]
        tmrs = pasien[3]
        nokamar = pasien[6]
        print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamar}')
        return data

    return


def staff_by_id(conn):
    id_staff = input('Masukkan ID Staff : ')
    query = f''' SELECT * FROM staff
                JOIN kamarrawatinap ON kamarrawatinap.kamarID = staff.kamarID
                WHERE staffID = '{id_staff}'
            '''
    try:
        data, column = execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()

    if len(data) == 0:
        print('Data kosong! Mengalihkan aplikasi ke menu utama.')
        main()

    for staff in data:
        id = staff[0]
        nama = staff[1]
        posisi = staff[2]
        nokamar = staff[5]
        print(f'ID: {id} Nama: {nama} Posisi: {posisi} Nomor Kamar: {nokamar}')
        return data

    return


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
                3. 103
                ''')

    nokamar = input('Masukkan pilihan anda: ')

    if nokamar == '1':
        return 1
    elif nokamar == '2':
        return 2
    elif nokamar == '3':
        return 3
    else:
        print('Input tidak tersedia pada pilihan!')
        input_nokamar()
    return

def input_posisi():
    print('''Pilih Posisi

                1. Dokter
                2. Perawat
                ''')

    nokamar = input('Masukkan pilihan anda: ')

    if nokamar == '1':
        return 'Dokter'
    elif nokamar == '2':
        return 'Perawat'
    else:
        print('Input tidak tersedia pada pilihan!')
        input_posisi()
    return

def id_generator_patient(conn):
    id_increment = 1
    query = '''SELECT * FROM pasien'''
    data, column_name = execute_query(conn, query)
    unique_id = f'P00{id_increment}'
    id_list = [patient[0] for patient in data]

    while unique_id in id_list:
        id_increment += 1
        unique_id = f'P00{id_increment}'
    return unique_id

def id_generator_staff(conn):
    id_increment = 1
    query = '''SELECT * FROM staff'''
    data, column_name = execute_query(conn, query)
    unique_id = f'S00{id_increment}'
    id_list = [staff[0] for staff in data]

    while unique_id in id_list:
        id_increment += 1
        unique_id = f'S00{id_increment}'
    return unique_id

def input_data(conn):
    nama = input_nama()
    umur = input_umur()
    tmrs = input_tmrs()
    nokamar = input_nokamar()
    id = id_generator_patient(conn)

    # nokamarprint = 1
    if nokamar == 1:
        nokamarprint = 101
    elif nokamar == 2:
        nokamarprint = 102
    else:
        nokamarprint = 103

    query = f"INSERT INTO pasien (pasienID, nama, umur, tanggalMasukRS, kamarID) VALUES ('{id}', '{nama}', {umur}, '{tmrs}', {nokamar})"
    try:
        execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()


    print(f'ID: {id} Nama: {nama} Umur: {umur} Tanggal Masuk RS: {tmrs} Nomor Kamar: {nokamarprint}')

    confirm = confirmation()
    if confirm:
        conn.commit()
        print('Data telah ditambahkan')
        main()
    else:
        print('Data batal ditambahkan')
        main()
    return

def input_data_staff(conn):
    nama = input_nama()
    posisi = input_posisi()
    nokamar = input_nokamar()
    id = id_generator_patient(conn)

    # nokamarprint = 1
    if nokamar == 1:
        nokamarprint = 101
    elif nokamar == 2:
        nokamarprint = 102
    else:
        nokamarprint = 103

    query = f"INSERT INTO staff (staffID, nama, posisi, kamarID) VALUES ('{id}', '{nama}', '{posisi}', '{nokamar}')"
    try:
        execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()


    print(f'ID: {id} Nama: {nama} Posisi: {posisi} Nomor Kamar: {nokamarprint}')

    confirm = confirmation()
    if confirm:
        conn.commit()
        print('Data telah ditambahkan')
        main()
    else:
        print('Data batal ditambahkan')
        main()
    return

def update_kamar(staff, conn):
    new_kamar = input_nokamar()
    if staff[3] == new_kamar:
        print('Nomor kamar saat ini sama dengan status yang dipilih!')
        update_kamar(staff, conn)
    staff_id = staff[0]
    query = f"""UPDATE staff
            SET kamarID = '{new_kamar}'
            WHERE CustomerID = '{staff_id}'
            """
    try:
        execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()

    confirm = confirmation()
    if confirm:
        conn.commit()
        print('Update nomor kamar berhasil')
        main()
    else:
        print('Update nomor kamar dibatalkan')
        main()
    return

def delete_by_id(conn, row, table):
    row_id = row[0]
    query = f"""DELETE FROM {table}
                WHERE pasienID = '{row_id}'
            """
    try:
        execute_query(conn, query)
    except Exception as e:
        print(f'Error: {e}')
        main()

    confirm = confirmation()
    if confirm:
        conn.commit()
        print('Data telah dihapus')
        main()
    else:
        print('Data batal dihapus')
        main()
    return

def read(conn):
    """Function for read the data
    """
    print('''======= Report Data Pasien =======

                1. Report Seluruh Data Pasien
                2. Report Seluruh Data Staff
                3. Cari Pasien Berdasarkan ID
                4. Cari Staff Berdasarkan ID
                5. Kembali Ke Menu Utama
                ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        show_patient(conn)
        main()
    elif input_user == '2':
        show_staff(conn)
        main()
    elif input_user == '3':
        patient_by_id(conn)
        main()
    elif input_user == '4':
        staff_by_id(conn)
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        read(conn)
    return

def create(conn):
    """Function for create the data
    """
    print('''======= Tambah Data Pasien =======

                    1. Tambah Data Pasien
                    2. Tambah Data Staff
                    3. Kembali Ke Menu Utama
                    ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        input_data(conn)# Fungsi tambah data pasien
    elif input_user == '2':
        input_data_staff(conn)
    elif input_user == '3':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        create()
    return

def update(conn):
    """Function for update the data
    """
    print('''======= Update Data Pasien =======

                        1. Update Nomor Kamar Staff
                        2. Kembali Ke Menu Utama
                        ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        staff = staff_by_id(conn)
        if staff:
            update_kamar(staff, conn)
    elif input_user == '2':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        update(conn)
    return

def delete(conn):
    """Function for delete the data
    """
    print('''======= Hapus Data Pasien =======

                            1. Hapus Berdasarkan ID Pasien
                            2. Hapus Berdasarkan ID Staff
                            3. Kembali Ke Menu Utama
                            ''')

    input_user = input("Silakan pilih menu tersedia: ")

    if input_user == '1':
        table = 'pasien'
    else:
        table = 'staff'

    if input_user == '1':
        patient = patient_by_id(conn)
        if patient:
            delete_by_id(conn, patient, table)
    elif input_user == '2':
        staff = staff_by_id(conn)
        if staff:
            delete_by_id(conn, staff, table)
    elif input_user == '3':
        main()
    else:
        print("Pilihan tidak tersedia pada menu!")
        delete(conn)
    return

# /===== Main Program =====/
# Create your main program here
def main():
    """Function for main program
    """
    print('''======= Data Pasien Rumah Sakit =======

            1. Report Data Pasien & Staff
            2. Tambah Data Pasien & Staff
            3. Ubah Data Staff
            4. Hapus Data Pasien & Staff
            5. Mengakhiri Program
            ''')

    input_user = input("Insert your option: ")
    if input_user == "1":
        read(conn)
    elif input_user == "2":
        create(conn)
    elif input_user == "3":
        update(conn)
    elif input_user == "4":
        delete(conn)
    elif input_user == "5":
        print('Aplikasi telah ditutup.')
        return
    else:
        print("Input is not valid !")
        main()


if __name__ == "__main__":
    main()