import qrcode

from fpdf import FPDF




class PDF(FPDF):
    def header(self):
        self.image('Logo_BA.png', 10, 8, 55,)
        self.ln(30)
        self.set_font('times', 'B', 30)
        self.cell(0, 10, 'Dokumen Persetujuan', border=False, ln=1, align='C' )
        self.ln(10)
        self.set_font('times', 'B', 12)
        self.cell(0, 5, 'Nomor Surat   : ', border=False, ln=1, align='L' )
        self.cell(0, 5, 'Lampiran        : ', border=False, ln=1, align='L' )
        self.cell(0, 5, 'Hal                   : ', border=False, ln=1, align='L' )
        self.cell(0, 5, 'Sifat                 : ', border=False, ln=1, align='L' )
        self.ln(10)

pdf = PDF('P', 'mm', format='A4')
pdf.add_page()
pdf.set_font('times', 'B', 12)
pdf.cell(0, 5, 'Dengan hormat,', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Dengan ini kami sampaikan bahwa Fakultas Teknik UGM telah menjalin kerjasama dengan PT PLN ', border=False, ln=1, align='L' )
pdf.cell(0, 5, '(Persero) Kantor Pusat dengan perjanjian nomor: 0443.PJ/DAN.02.07/010505/2019 ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Sehubungan dengan hal tersebut, mohon berkenan kebijaksanaan ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Bapak untuk dapat menerbitkan, E-Faktur, guna kelengkapan administrasi pembayaran,', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'dengan data sebagai berikut: ', border=False, ln=1, align='L' )
pdf.ln(10)
pdf.cell(0, 5, 'Nama Perusahan  : ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Besar dana            : ', border=False, ln=1, align='L' )
pdf.cell(0, 5, 'Jenis Kejasama     : ', border=False, ln=1, align='L' )
pdf.ln(10)
pdf.cell(0, 5, 'Demikian dokumen Kerjasama, terimakasih atas perhatiannya.', border=False, ln=1, align='L' )

pdf.ln(30)
pdf.cell(0, 5, 'Manajer', border=False, ln=0, align='L' )
pdf.cell(0, 5, 'Penanggung Jawab', border=False, ln=1, align='R' )
pdf.ln(30)
img = qrcode.make('https://www.youtube.com/watch?v=-GmJLI122ZM')
type(img)
img.save("some_file.png")
pdf.image('some_file.png', 10,195,30)


pdf.cell(0, 5, 'Budi Budiman', border=False, ln=0, align='L' )
pdf.cell(0, 5, 'Sudriman', border=False, ln=0, align='R' )










pdf.output('Coba.pdf','F')

