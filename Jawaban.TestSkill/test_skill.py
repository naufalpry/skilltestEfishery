1.Biasanya nya pakai SIT,UIT dan Production test
- SIT : System Integration Testin
Definisinya test yg dilakukan apakah fungsi yang ada dari aplikasi telah terintegrasi.
SIT bersifat lebih teknikal dan dilakukan oleh tester.
- UAT : User Accpect Test 
Desinisinya test yg dilakukan setelah SIT jika aplikasi telah lulus Test UAT maka dapat pidah ke environtment production.
- Production Test : Melakukan Test Data production dengan local server menggunakan etc/host yang di ubah ke ip dan settingan prod (untuk web), Minta build Apk Production yang belum di up ke playstore/Appstore (untuk mobile)

2.Pre-production : Aplikasi masih menggunakan environtment staging (Aplikasi yag Pre-Release) dengan menggunakan data production. 
- post production : hasil commitan atau hasil testing aplikasi yang telah di fixing oleh developer. yang benar2 bebas bebas bug dan menggunakan environtment production dan data production.

3.- Unit testing : mencati eror bug yg disebabkan oleh perubahan code, juga merupakan Testing API yang biasanya dilakukan oleh developer/backend, unit tetsing memastikan result yang di dihasilkan dari test unit sesuai expected.

- Integration testing : sebuah test yang dilakukan dari hasil penggabungan code lama dengan code baru untuk memastikan code lama tidak tersengol atau tidak memiliki bug. dan memastikan fitur terbaru berjalan bebas bug.

4. - Sebenernya itu pun masih menjadi problem di kantor saya karena membutuhkan budget besar. 
jika dikantor saya Toolsnya menggunakan appium, framework pakai testng base on java terus mengambil beberapa plugin yang di butuhkan untuk Device Farm (device cloud) dari AWS atau saucelab dan saya memakai maven repository 


device farm itu wadah emulator berbayar sekitar 1000menit/4jt.

- Build script di local dalam bentuk zip (menggunakan plugin testng), 
git pull data 
git add
git commit
dan git push ke repository
login ke AWS untuk farm device nya dilanjutkan upload apk (latest apk)
pilih zip yg di upload (testng)
pilih appium version
pilih device farm yg akan di pakai
create test run (build)
report

* Kelebihan
	- Mudah di akses
	- Device nya banyak dari versi android 3.0 s/d versi 10 terdapat iphone
	- Dokumentasi nya lengkap
* Kekurangan :
	- Berbayar
	- Dibatasi limit waktu
	- Waktu delay pengetesan lama

5.  * Untuk test memakai tools robot framework version 3.2.2 dengan Python 2.7.17
	* 	- Buat script robot di local
		- pull data repo master
		- git add
		- git commit -m
		- git push 
		- login ke Jenkins server
		- Merge branch local ke master
		- Build
		- Report
	* 	Kelebihan :
		- Free
		- Bahasanya lebih mudah di mengerti
		- Function nya yg flexible dengan bahasa python
		- Punya log untuk debug testcase via web jadi memudahkan kita
	* 	Kekurangan :
		- Robot Framework menyediakan perekam
		- Driver Chrome harus sesuai dengan Compatible laptop local/Server
		- Sensitif Case karena menggunakan Python
		- Untuk user awam robot framework document membuat bingung untuk memilih keyword yg akan di implementasikan

7.  * Dapat bekerja paralel dalam artian QA bisa bekerja Sebagai QA manual Automation dan Unit Test
	* Mudah beradaptasi
	* Mau belajar hal hal baru, saya pribadi tertarik dengan hal hal baru dan senang mengulik
	* Dapat diandalkan

