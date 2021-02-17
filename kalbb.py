#!/usr/bin/python3

###MODUL IMPORT####
from tkinter import *
from os import system
import time

#Deskripsi
deskripsi='''KALKULATOR BERAT BADAN
Pembuat		: Aries Aprilian (abex888@gmail.com)
Versi		: 1.0.0
Lisensi		: GNU GPL versi 2
Program ini dibuat dengan python3 menggunakan beberapa
modul diantaranya adalah:
1. modul Tkinter untuk gui
2. modul os untuk mengakses shell (bash)

CARA KERJA
Program ini menggunakan rumus Borcha dan Body Mass Index (BMI).
rumus Borcha digunakan untuk menentukan berat badan ideal,
sedangkan BMI digunakan untuk menentukan kategori yang terdiri
atas kurus, normal, kegemukan dan obesitas.

Variabel yang diminta adalah jenis kelamin, tinggi badan, dan berat
badan. Variabel jenis kelamin untuk menentukan rumus borcha dan
kategori. Variabel tinggi dan berat badan kemudian di pass sebagai
argumen ke fungsi rumus BMI, sedangkan rumus Borcha hanya menggunakan
variabel tinggi badan'''

###CLASS DAN FUNGSI###
class jendela_utama():
	FontBadag = 'serif 20 bold'
	FontRadaBadag = 'serif 16 bold'
	FontSedeng = 'serif 10'
	FontLeutik = 'courier 8'
	listjk = ['Pria','Wanita']
	hasilbb=''
	def __init__(self):
		###ATRIBUT WINDOW UTAMA. JUDUL ADA DI BAWAH DEKAT MAINLOOP
		self.root = Tk()
		self.root.resizable(0,0)
		self.JUDUL = 'KALKULATOR BERAT BADAN'
		#______________________________________________________________________________________________________________________________#
		###DEKLARASI VARIABEL###
		self.varjk = IntVar()
		self.entvartb = IntVar()
		self.entvarbb = IntVar()
		self.entvartb.set('')
		self.entvarbb.set('')	
		#______________________________________________________________________________________________________________________________#
		###FRAME###
		self.frame_data = Frame(self.root, bd=3, relief=SUNKEN)
		self.frame_lap = Frame(self.root, bd=3, relief=GROOVE)
		#______________________________________________________________________________________________________________________________#
		###WIDGET MILIK ROOT###
		self.judul1 = Label(self.root, text='KALKULATOR')
		self.judul1.configure(font=jendela_utama.FontBadag)
		self.judul2 = Label(self.root, text='BERAT BADAN')
		self.judul2.configure(font=jendela_utama.FontRadaBadag)
		self.judul1.grid(row=0, column=0, columnspan=2, sticky='we', padx=3, pady=3)
		self.judul2.grid(row=1, column=0, columnspan=2, sticky='we', padx=3, pady=3)
		
		#Catatan dan copyright di paling bawah
		self.catatan1 = Label(self.root, text='F1 untuk deskripsi')
		self.catatan1.configure(font=jendela_utama.FontLeutik)
		self.catatan1.grid(row=4, column=0, sticky='w', padx=2, pady=2)
		
		self.catatan2 = Label(self.root, text='F4 untuk keluar')
		self.catatan2.configure(font=jendela_utama.FontLeutik)
		self.catatan2.grid(row=5, column=0, sticky='w', padx=2, pady=2)
		
		self.copyright = Label(self.root, text='(c)2017 Aries Aprilian')
		self.copyright.configure(font=jendela_utama.FontLeutik)
		self.copyright.grid(row=4, column=1, sticky='e', padx=2, pady=2)
		
		#Jam
		self.dwaktu = Label(self.root, text='JAM')
		self.dwaktu.configure(font=jendela_utama.FontLeutik)
		self.dwaktu.grid(row=5, column=1, sticky='e', padx=2, pady=2)
		
		
		#binding milik root
		
		self.root.bind('<Return>', lambda event: jendela_utama.hitung(self, event, self.entvartb, self.entvarbb, self.varjk))
		self.root.bind('<F1>', tentang)
		self.root.bind('<F4>', lambda kaluar: self.root.destroy())
		self.root.bind('<F2>', lambda event: jendela_utama.ulangi(self, event))
		#______________________________________________________________________________________________________________________________#
		###WIDGET MILIK frame_data###
		#Label 'Jenis Kelamin'
		self.labjk = Label(self.frame_data, text='Jenis Kelamin')
		self.labjk.configure(font=jendela_utama.FontSedeng)
		self.labjk.grid(row=0, column=0,  sticky='w', padx=5, pady=5)
		
		#Radio Button Jenis Kelamin
		for self.hitjk in range(2):
			self.radjk = 'radjk'+str(self.hitjk)
			self.radjk = Radiobutton(self.frame_data, text=jendela_utama.listjk[self.hitjk], value=self.hitjk, variable=self.varjk)
			self.radjk.configure(font=jendela_utama.FontSedeng)
			self.radjk.grid(row=self.hitjk+1, column=0, sticky='w', padx=5, pady=5)
		
		#Label Tinggi Badan dan Berat Badan
		self.labtb = Label(self.frame_data, text='Tinggi Badan (cm)')
		self.labtb.configure(font=jendela_utama.FontSedeng)
		self.labtb.grid(row=0, column=1, sticky='w', padx=5, pady=5)
		self.labbb = Label(self.frame_data, text='Berat Badan (kg)')
		self.labbb.configure(font=jendela_utama.FontSedeng)
		self.labbb.grid(row=1, column=1, sticky='w', padx=5, pady=5)
		
		#Entry Tinggi Badan dan Berat Badan
		self.enttb = Entry(self.frame_data, textvariable=self.entvartb, width=3, justify=RIGHT)
		self.enttb.grid(row=0, column=2, sticky='w', padx=5, pady=5)
		self.enttb.focus() #Fokus ke entry tinggi badan
		self.entbb = Entry(self.frame_data, textvariable=self.entvarbb, width=3, justify=RIGHT)
		self.entbb.grid(row=1, column=2, sticky='w', padx=5, pady=5)
		
		
		#Tombol Hitung
		self.tombol_hitung = Button(self.frame_data, text='Hitung', width=5)
		self.tombol_hitung.grid(row=2, column=1, sticky='e', padx=5, pady=5)
		#perhatian, untuk binding ke method lain pass value ke argumen menggunakan lambda
		self.tombol_hitung.bind('<Button-1>', lambda event: jendela_utama.hitung(self, event, self.entvartb, self.entvarbb, self.varjk))
		
		#Tombol Keluar
		#self.tombol_keluar = Button(self.frame_data, text='Keluar', width=5)
		#self.tombol_keluar.grid(row=2, column=2, sticky='e', padx=5, pady=5)
		#self.tombol_keluar.bind('<Button-1>', lambda kaluar: self.root.destroy())
		
		#Tombol Reset
		self.tombol_reset = Button(self.frame_data, text='Ulang (F2)', width=6)
		self.tombol_reset.grid(row=2, column=2, sticky='e', padx=5, pady=5)
		self.tombol_reset.bind('<Button-1>', lambda event: jendela_utama.ulangi(self, event))
		
		
		#______________________________________________________________________________________________________________________________#
		###WIDGET MILIK frame_lap###
		#Label "Hasil Penghitungan
		self.labjudulhasil = Label(self.frame_lap, text='HASIL PERHITUNGAN')
		self.labjudulhasil.configure(font = jendela_utama.FontSedeng)
		self.labjudulhasil.grid(row=0, column=0, sticky='w', padx=5, pady=5)
		
		self.labhasilborcha = Label(self.frame_lap, text='Berat Ideal Anda')
		self.labhasilborcha.configure(font = jendela_utama.FontSedeng)
		self.labhasilborcha.grid(row=1, column=0, sticky='w', padx=5, pady=5)
		
		self.labhasilbmi = Label(self.frame_lap, text='Nilai Body Mass Index (BMI)')
		self.labhasilbmi.configure(font = jendela_utama.FontSedeng)
		self.labhasilbmi.grid(row=2, column=0, sticky='w', padx=5, pady=5)
		
		self.labkategori = Label(self.frame_lap, text='Kategori Tubuh Anda')
		self.labkategori.configure(font = jendela_utama.FontSedeng)
		self.labkategori.grid(row=3, column=0, sticky='w', padx=5, pady=5)
		
		#Titik dua
		for self.ttkdua in range(3):
			self.labttkdua = 'labtktkdua'+str(self.ttkdua)
			self.labttkdua = Label(self.frame_lap, text=':')
			self.labttkdua.configure(font=self.FontSedeng)
			self.labttkdua.grid(row=self.ttkdua+1, column=1)
		
		#Tampilan hasil perhitungan dan kategori
		self.lapborcha = Label(self.frame_lap, text='', width=5, bg='white')
		self.lapborcha.configure(font=self.FontSedeng)
		self.lapborcha.grid(row=1, column=2, sticky='e', padx=3, pady=3)
		
		self.lapbmi = Label(self.frame_lap, text='', width=5, bg='white')
		self.lapbmi.configure(font=self.FontSedeng)
		self.lapbmi.grid(row=2, column=2, sticky='e', padx=3, pady=3)
		
		self.lapkategori = Label(self.frame_lap, text='', width=10, bg='white')
		self.lapkategori.configure(font=self.FontSedeng)
		self.lapkategori.grid(row=3, column=2, sticky='w', padx=3, pady=3)
		#______________________________________________________________________________________________________________________________#
		###TAMPILKAN frame_data dan frame_lap###
		self.frame_data.grid(row=2, column=0,  sticky='we', columnspan=2, padx=10, pady=10)
		self.frame_lap.grid(row=3, column=0,  sticky='we', columnspan=2, padx=10, pady=10)
		#______________________________________________________________________________________________________________________________#
		###LOOP UTAMA###
		jendela_utama.jam(self)
		self.root.title(self.JUDUL)
		self.root.mainloop()
		#______________________________________________________________________________________________________________________________#
	
	def hitung(self, event, tb, bb, varjk):
		try:
			tb = self.entvartb.get()
			bb = self.entvarbb.get()
			varjk = self.varjk.get()
		#jika pria jalankan class pria, jika wanita jalankan class wanita
			if varjk == 0:
				hasil_borcha = pria.brocha_pria(self, tb)
				hasil_bmi = bmi.hit_bmi(self, bb, tb)
				kategori = pria.kategori_pria(self, hasil_bmi)
				self.lapborcha.configure(text=hasil_borcha)
				self.lapbmi.configure(text=hasil_bmi)
				self.lapkategori.configure(text=kategori)
				system('clear')
				print('Anda Seorang Pria')
				print('Berat ideal anda: ', hasil_borcha)
				print('Nilai BMI anda: ', hasil_bmi)
				print('Kategori Tubuh anda: ', kategori)
			elif varjk == 1:
				hasil_borcha = wanita.brocha_wanita(self, tb)
				hasil_bmi = bmi.hit_bmi(self, bb, tb)
				kategori = wanita.kategori_wanita(self, hasil_bmi)
				self.lapborcha.configure(text=hasil_borcha)
				self.lapbmi.configure(text=hasil_bmi)
				self.lapkategori.configure(text=kategori)
				system('clear')
				print('Anda Seorang Wanita')
				print('Berat ideal anda: ', hasil_borcha)
				print('Nilai BMI anda: ', hasil_bmi)
				print('Kategori Tubuh anda: ', kategori)
			#Ubah warna sesuai kategori
			if kategori == 'Kurus': self.lapkategori.configure(bg='yellow')
			elif kategori == 'Normal': self.lapkategori.configure(bg='lightgreen')
			elif kategori == 'Kegemukan': self.lapkategori.configure(bg='yellow')
			elif kategori == 'Obesitas': self.lapkategori.configure(bg='red')
		except:
			system('clear')
			print('Periksa kembali data yang dimasukkan, nilai tidak boleh 0')
		
	def jam(self):
		self.waktu = time.strftime("%H:%M:%S")
		self.varjam = self.waktu[0:2]
		self.varmenit = self.waktu[3:5]
		self.vardetik = self.waktu[6:8]
		self.dwaktu.configure(text=self.waktu)
		self.root.after(1000, lambda: jendela_utama.jam(self))
		return self.waktu
	
	def ulangi(self, event):
		self.entvartb.set('')
		self.entvarbb.set('')
		self.enttb.focus()
		
		self.lapborcha.configure(text='')
		self.lapbmi.configure(text='')
		self.lapkategori.configure(text='')

class pria(jendela_utama):
	def brocha_pria(self, tb):
		bb = (tb-100)-((10/100) * (tb-100))
		bb = int(bb)
		return bb
	
	def kategori_pria(self, idx):
		if idx < 17: kategori = 'Kurus'
		elif idx <= 23: kategori = 'Normal'
		elif idx <= 27: kategori = 'Kegemukan'
		elif idx > 27: kategori = 'Obesitas'
		return kategori
		
class wanita(jendela_utama):	
	def brocha_wanita(self, tb):
		bb = (tb-100)-((15/100) * (tb-100))
		bb = int(bb)
		return bb
	
	def kategori_wanita(self, idx):
		if idx < 18: kategori = 'Kurus'
		elif idx <= 25: kategori = 'Normal'
		elif idx <= 27: kategori = 'Kegemukan'
		elif idx > 27: kategori = 'Obesitas'
		return kategori

class bmi(jendela_utama):	
	def hit_bmi(self, bb, tb):
		tb = tb / 100
		idx = bb / (tb * tb)
		idx = int(idx)
		return idx

class tentang():
	def __init__(self, event=None):
				
		self.jendela_tentang = Toplevel()
		self.jendela_tentang.title('About')
		self.jendela_tentang.resizable(0,0)
		
		self.frame_deskripsi=Frame(self.jendela_tentang, bd=3, bg='white', relief=SUNKEN)
		self.frame_deskripsi.pack()
		
		self.label_deskripsi = Label(self.frame_deskripsi, text='', bg='white', fg='black', justify=LEFT)
		self.label_deskripsi.config(text=deskripsi)
		self.label_deskripsi.pack()			
				
		self.q = Button(self.jendela_tentang, text='Tutup')
		self.q.pack()
		self.q.bind('<Button-1>', lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Button-3>',lambda kaluar: self.jendela_tentang.destroy())
		self.jendela_tentang.bind('<Escape>',lambda kaluar: self.jendela_tentang.destroy())

	
###JALANKAN PROGRAM!###	
awal = '''
============================
|| KALKULATOR BERAT BADAN ||
============================  
'''
akhir = '''(c)2017 Aries Aprilian
abex888@gmail.com
http://www.facebook.com/abex888
http://abexthegreat.tk/
'''
if __name__=='__main__':
	system('clear')
	print(awal)
	print(deskripsi)
	aplikasi = jendela_utama()
	system('clear')
	print(akhir)
	time.sleep(2)
	#system('clear')
