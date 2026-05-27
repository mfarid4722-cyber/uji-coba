from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/daftar', methods=['POST'])
def daftar():
    nama = request.form['nama']
    kampus = request.form['kampus']
    jurusan = request.form['jurusan']
    divisi = request.form['divisi']
    alasan = request.form['alasan']

    os.makedirs("data", exist_ok=True)

    with open('data/peserta.txt', 'a', encoding='utf-8') as file:
        file.write(f"""
Nama     : {nama}
Kampus   : {kampus}
Jurusan  : {jurusan}
Divisi   : {divisi}
Alasan   : {alasan}
---------------------------
""")

    return f"""
    <center>
        <h1>Pendaftaran Berhasil!</h1>
        <p>Terima kasih <b>{nama}</b> telah mendaftar.</p>
        <a href="/">Kembali ke Beranda</a>
    </center>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
