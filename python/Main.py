# import
from Human import Human
from SivitasAkademik import SivitasAkademik
from Mahasiswa import Mahasiswa
from Dosen import Dosen
from ProgramStudi import ProgramStudi
from Course import Course

# instansiasi
h1 = Human()
s1 = SivitasAkademik()
m1 = Mahasiswa()
p1 = ProgramStudi()
c1 = Course()

# mengeset isi atribut human h untuk mahasiswa m1
m1.setNIK("12345");
m1.setNama("Fulan");
m1.setKelamin("Laki-laki");

# mengeset isi atribut sivitas akademik s untuk mahasiswa m1
m1.setUniv("UPI");
m1.setEmail("fulan@email.com");
m1.setFakultas("FPMIPA");

# mengeset isi atribut mahasiswa m1
m1.setNIM("2100000");

# mengeset isi atribut program studi p1
p1.setProdi("Ilmu Komputer");
p1.setKodeP("001");

# mengeset isi atribut course c1
c1.setMatkul("DPBO");
c1.setKodeM("112D");

print("========== Data Manusia ==========")
print("Nama: " + str(m1.getNama()))
print("NIK: " + str(m1.getNIK()))
print("Gender: " + str(m1.getKelamin()))
print("Berkuliah di: " + str(m1.getUniv()))
print("Memiliki email edu: " + str(m1.getEmail()))
print("Memiliki NIM: " + str(m1.getNIM()))
print("Berada di fakultas: " + str(m1.getFakultas()))
print("Memilih Program Studi: " + str(p1.getProdi()))
print("Kode Prodi adalah: " + str(p1.getKodeP()))
print("Saat ini mengontrak matkul: " + str(c1.getMatkul()))
print("yang memiliki kode: " + str(c1.getKodeM()))

# instansiasi
h2 = Human()
s2 = SivitasAkademik()
d2 = Dosen()
p2 = ProgramStudi()
c2 = Course()

# mengeset isi atribut human h untuk dosen d2
d2.setNIK("67890");
d2.setNama("Jane Doe");
d2.setKelamin("Perempuan");

# mengeset isi atribut sivitas akademik s untuk dosen d2
d2.setUniv("UPI");
d2.setEmail("janedoe@email.com");
d2.setFakultas("FPMIPA");

# mengeset isi atribut dosen d2
d2.setNIP("9999999");
d2.setPend("S3");
d2.setAhli("Komputer");

# mengeset isi atribut program studi p2
p2.setProdi("Ilmu Komputer");
p2.setKodeP("001");

# mengeset isi atribut course c2
c2.setMatkul("DPBO");
c2.setKodeM("112D");

print("========== Data Manusia ==========")
print("Nama: " + str(d2.getNama()))
print("NIK: " + str(d2.getNIK()))
print("Gender: " + str(d2.getKelamin()))
print("Mengajar di kampus: " + str(d2.getUniv()))
print("Memiliki email edu: " + str(d2.getEmail()))
print("Memiliki NIP: " + str(d2.getNIP()))
print("Pendidikan terakhir: " + str(d2.getPend()))
print("Memiliki keahlian di bidang: " + str(d2.getAhli()))
print("Berada di fakultas: " + str(d2.getFakultas()))
print("di Program Studi: " + str(p2.getProdi()))
print("Kode Prodi adalah: " + str(p2.getKodeP()))
print("Saat ini mengajar matkul: " + str(c2.getMatkul()))
print("yang memiliki kode: " + str(c2.getKodeM()))
