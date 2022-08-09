from tkinter import ttk
from tkinter import *
from pymongo import MongoClient


class Mahasiswa:

    mongo_uri = 'mongodb://localhost'

    def __init__(self, window):

        self.run_db()

        # window utama
        self.wind = window
        self.wind.title('Aplikasi Biodata Mahasiswa')

        frame = LabelFrame(self.wind, text="daftar")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        Label(frame, text='nim: ').grid(row=1, column=0)
        self.nim = Entry(frame)
        self.nim.focus()
        self.nim.grid(row=1, column=1)

        Label(frame, text='nama: ').grid(row=2, column=0)
        self.nama = Entry(frame)
        self.nama.grid(row=2, column=1)

        ttk.Button(frame, text='simpan', command=self.tambah_mahasiswa).grid(row=3, columnspan=2, sticky=W + E)

        self.message = Label(text='', fg='red')
        self.message.grid(row=3, column=0, columnspan=2, sticky=W + E)

        # menampilkan data yang tersimpan
        self.tree = ttk.Treeview(height=10, column=2)
        self.tree.grid(row=4, column=0, columnspan=2)
        self.tree.heading('#0', text='nim', anchor=CENTER)
        self.tree.heading('#1', text='nama', anchor=CENTER)

        ttk.Button(text='hapus', command=self.hapus_mahasiswa).grid(row=5, column=0, sticky=W + E)
        ttk.Button(text='ubah', command=self.ubah_mahasiswa).grid(row=5, column=1, sticky=W + E)

        self.simpan_mahasiswa()
    
    def run_db(self):
        client = MongoClient(self.mongo_uri)
        db = client['mahasiswa'] # buat database dengan nama 'mahasiswa'
        self.collection = db['biodata'] # buat collection dengan nama 'biodata'

    def simpan_mahasiswa(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        
        results = self.collection.find().sort('nim', -1)

        for row in results:
            self.tree.insert('', 0, text=row['nim'], values=row['nama'])

    def validasi(self):
        return len(self.nim.get()) != 0 and len(self.nama.get()) != 0

    def tambah_mahasiswa(self):
        if self.validasi():
            self.collection.insert_one(
                {'nim': self.nim.get(),
                 'nama': self.nama.get()}
            )
            self.message['text'] = 'mahasiswa berhasil ditambah'.format(self.nama.get())
            self.nim.delete(0, END)
            self.nama.delete(0, END)
        else:
            self.message['text'] = 'nim dan nama wajib ditulis'
        self.simpan_mahasiswa()

    def hapus_mahasiswa(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except:
            self.message['text'] = 'Silakan, pilih data yang akan dihapus'
            return
        self.message['text'] = ''
        nim = self.tree.item(self.tree.selection())['text']
        self.collection.delete_one({'nim': nim})
        self.message['text'] = 'Data {} berhasil dihapus'.format(nim)
        self.simpan_mahasiswa()

    def ubah_mahasiswa(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'Silakan, pilih data yang akan diubah'
            return
        nim = self.tree.item(self.tree.selection())['text']
        nama_sebelumnya = self.tree.item(self.tree.selection())['values'][0]

        # menampilkan window baru
        self.edit_wind = Toplevel()
        self.edit_wind.title = 'Ubah Mahasiswa'

        # nim lama        
        Label(self.edit_wind, text='nim lama: ').grid(row=0, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=nim), state='readonly').grid(row=0, column=2)

        # nim baru
        Label(self.edit_wind, text='nim baru: ').grid(row=1, column=1)
        nim_baru = Entry(self.edit_wind)
        nim_baru.grid(row=1, column=2)

        # nama lama
        Label(self.edit_wind, text='nama lama: ').grid(row=2, column=1)
        Entry(self.edit_wind, textvariable=StringVar(self.edit_wind, value=nama_sebelumnya), state='readonly').grid(row=2, column=2)

        # nama baru
        Label(self.edit_wind, text='nama baru: ').grid(row=3, column=1)
        nama_baru = Entry(self.edit_wind)
        nama_baru.grid(row=3, column=2)

        print(nim)

        Button(self.edit_wind, text='ubah data', command=lambda:
        self.ubah_records(nim_baru.get(), nim, nama_baru.get(), nama_sebelumnya)).grid(row=4, column=2, sticky=W)
        self.edit_wind.mainloop()

    def ubah_records(self, nim_baru, nim, nama_baru, nama_sebelumnya):
        print(nim)
        print(nama_sebelumnya)
        self.collection.update_one(
            {'nim': nim},
            {'$set': {'nim': nim_baru, 'nama': nama_baru}}
        )
        self.edit_wind.destroy()
        self.message['text'] = 'record {} berhasil diubah'.format(nim)
        self.simpan_mahasiswa()


if __name__ == '__main__':
    window = Tk()
    application = Mahasiswa(window)
    window.mainloop()
