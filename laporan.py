import requests
from flask import Flask, jsonify, request #panggil flask dan jsonify
from flask_mysqldb import MySQL

app = Flask(__name__) #bikin objek

#config mysql
app.config ['MYSQL_HOST'] = 'localhost'
app.config ['MYSQL_USER'] = 'root'
app.config ['MYSQL_PASSWORD'] = ''
app.config ['MYSQL_DB'] = 'laporan_iae'
mysql = MySQL(app)

@app.route('/laporan') #halaman utama
def coba(): #bebas menulis nama fungsinyaa /// bisa main, root, dll
    return 'Selamat datang di Lapporan - API'

#Endpoint laporan | Get all data laporan
@app.route('/laporan/getall', methods = ['GET'])
def getlaporan():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM laporan")
        #dosen = cursor.fetchall() #menyimpan ke dalam var dosen
        #return jsonify(dosen)

        #ambil columns name from cursor.decription
        column_names = [i[0] for i in cursor.description] 
        #fetch data and format inti list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        return jsonify(data)

        cursor.close()


@app.route('/laporan/post', methods=['POST'])
def postlaporan():
    if request.method == 'POST':
        laporan_bulan = request.json['laporan_bulan']
        tgl_pembelian = request.json['tgl_pembelian']
        merk_kendaraan = request.json['merk_kendaraan']
        harga_modal = request.json['harga_modal']
        harga_satuan = request.json['harga_satuan']
        total_terjual = request.json['total_terjual']

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO laporan (laporan_bulan, tgl_pembelian, merk_kendaraan, harga_modal, harga_satuan, total_terjual) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (laporan_bulan, tgl_pembelian, merk_kendaraan, harga_modal, harga_satuan, total_terjual)
        cursor.execute(sql, val)
        mysql.connection.commit()

        # Hitung total_income dan total_profit
        total_income = harga_satuan * total_terjual
        total_profit = total_income - (harga_modal * total_terjual)

        # Update total_income dan total_profit dalam tabel laporan
        update_sql = "UPDATE laporan SET total_income = %s, total_profit = %s WHERE laporan_bulan = %s AND tgl_pembelian = %s"
        update_val = (total_income, total_profit, laporan_bulan, tgl_pembelian)
        cursor.execute(update_sql, update_val)
        mysql.connection.commit()

        cursor.close()

        return jsonify({'message': 'Data added successfully!'})

#Endpoint laporan | Delete data laporan
@app.route('/laporan/del', methods = ['DELETE'])
def laporandel():
    if request.method == 'DELETE':
        # Mengambil id dari parameter URL
        id_laporan = request.args.get('id')

        # Open connection to db
        cursor = mysql.connection.cursor()

        # Eksekusi perintah DELETE menggunakan cursor
        cursor.execute("DELETE FROM laporan WHERE id_laporan = %s", (id_laporan,))

        # Commit perubahan ke database
        mysql.connection.commit()

        # Mengembalikan respons
        response = {
            'message': 'Data deleted successfully!',
            'id': id_laporan
        }

        cursor.close()

        return jsonify(response)

#Endpoint laporan | Get data yang lebih spesifik
#membuat endpoint GET /laporancz untuk mengambil berdasarkan id dan tanggal/bulan/tahun
@app.route('/laporancz', methods=['GET'])
def laporanid():
    if 'id' in request.args:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM laporan WHERE id_laporan = %s"
        val = (request.args['id'],)
        cursor.execute(sql, val)
        #ambil columns name from cursor.decription
        column_names = [i[0] for i in cursor.description]
        #fetch data and format inti list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))

        cursor.close()
        return jsonify(data)
    
    elif 'tgl' in request.args:
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM laporan WHERE tgl_pembelian = %s"
        val = (request.args['tgl'],)
        cursor.execute(sql, val)
        #ambil columns name from cursor.decription
        column_names = [i[0] for i in cursor.description]
        #fetch data and format inti list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))

        cursor.close()
        return jsonify(data)

    elif 'bulan' in request.args:
        bulan = request.args['bulan']
        cursor = mysql.connection.cursor()
        sql = "SELECT * FROM laporan WHERE laporan_bulan = %s"
        val = (bulan,)
        cursor.execute(sql, val)
        # ambil columns name dari cursor.description
        column_names = [i[0] for i in cursor.description]
        # fetch data dan format menjadi list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))

        cursor.close()
        return jsonify(data)


    else:
        return 'Parameter tidak ditemukan'


#Endpoint pembayaran | Get all data pembayaran
@app.route('/pembayaran/getall', methods = ['GET'])
def getpembayaran():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM pembayaran")
        #dosen = cursor.fetchall() #menyimpan ke dalam var dosen
        #return jsonify(dosen)

        #ambil columns name from cursor.decription
        column_names = [i[0] for i in cursor.description] 
        #fetch data and format inti list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        return jsonify(data)

        cursor.close()
"""
@app.route('/pembayaran', methods=['POST'])
def create_pembayaran():
    if request.method == 'POST':
        # Mendapatkan data dari permintaan (request)
        harga_modal = request.json['harga_modal']
        harga_satuan = request.json['harga_satuan']
        merk_kendaraan = request.json['merk_kendaraan']
        tgl_pembelian = request.json['tgl_pembelian']
        total_terjual = request.json['total_terjual']
        
        # Melakukan operasi perhitungan
        total_income = harga_satuan * total_terjual
        total_profit = total_income - (harga_modal * total_terjual)
        
        # Menyimpan data ke dalam tabel pembayaran
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO pembayaran (harga_modal, harga_satuan, merk_kendaraan, tgl_pembelian, total_terjual, total_income, total_profit) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (harga_modal, harga_satuan, merk_kendaraan, tgl_pembelian, total_terjual, total_income, total_profit)
        cursor.execute(sql, val)
        mysql.connection.commit()
        
        # Mengambil ID pembayaran yang baru saja ditambahkan
        pembayaran_id = cursor.lastrowid
        
        # Memperbarui data di tabel laporan
        sql_update = "UPDATE laporan SET total_income = %s, total_profit = %s WHERE id_laporan = %s"
        val_update = (total_income, total_profit, pembayaran_id)
        cursor.execute(sql_update, val_update)
        mysql.connection.commit()
        
        cursor.close()
        
        return jsonify({'message': 'Data pembayaran berhasil ditambahkan dan laporan diperbarui!'})

"""
@app.route('/pembayaran/post', methods=['POST'])
def postpembayaran():
    if request.method == 'POST':
        laporan_bulan = request.json['laporan_bulan']
        tgl_pembelian = request.json['tgl_pembelian']
        merk_kendaraan = request.json['merk_kendaraan']
        harga_modal = request.json['harga_modal']
        harga_satuan = request.json['harga_satuan']
        total_terjual = request.json['total_terjual']

        cursor = mysql.connection.cursor()
        sql = "INSERT INTO laporan (laporan_bulan, tgl_pembelian, merk_kendaraan, harga_modal, harga_satuan, total_terjual) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (laporan_bulan, tgl_pembelian, merk_kendaraan, harga_modal, harga_satuan, total_terjual)
        cursor.execute(sql, val)
        mysql.connection.commit()

        # Hitung total_income dan total_profit
        total_income = harga_satuan * total_terjual
        total_profit = total_income - (harga_modal * total_terjual)

        # Update total_income dan total_profit dalam tabel laporan
        update_sql = "UPDATE laporan SET total_income = %s, total_profit = %s WHERE laporan_bulan = %s AND tgl_pembelian = %s"
        update_val = (total_income, total_profit, laporan_bulan, tgl_pembelian)
        cursor.execute(update_sql, update_val)
        mysql.connection.commit()

        cursor.close()

        return jsonify({'message': 'Data added successfully!'})

#Endpoint laporan | 
@app.route('/laporan/provide', methods = ['GET'])
def getprovide():
    if request.method == 'GET':
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT id_laporan, merk_kendaraan, total_terjual, total_profit FROM laporan")
        #dosen = cursor.fetchall() #menyimpan ke dalam var dosen
        #return jsonify(dosen)

        #ambil columns name from cursor.decription
        column_names = [i[0] for i in cursor.description] 
        #fetch data and format inti list of dictionaries
        data = []
        for row in cursor.fetchall():
            data.append(dict(zip(column_names, row)))
        return jsonify(data)

        cursor.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070, debug=True)