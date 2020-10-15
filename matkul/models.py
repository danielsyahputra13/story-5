from django.db import models
from django.db.models.deletion import CASCADE

# Buat pilihan untuk drop-down. 
# semester_choices = [("1", "1"), ("2", "2").....("8", "8")]
# Bentuk choice nya tupple (ACTUAL_VALUE, HUMAN_READABLE_NAME)
# If semester % 2 == 0: genap else : ganjil


# Create your models here.
class Semester(models.Model):
    semester_choices = [(i, str(i)) for i in range(1, 9)]
    # Tahun ajaran: Isinya tupple-tuple tahun ajaran. (YANG_GANJIL, YANG_GENAP)
    tahun_ajaran_choices = [
        ('2019/2020', '2019/2020'),
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023')
    ]
    semester_id = models.IntegerField(choices=semester_choices)

    def __str__(self):
        return f"Semester {self.semester_id}"


class MataKuliah(models.Model):
    # Ketika kita punya table yang berhubungan SQL butuh tahu apa yang bakal dilakuin kalau kita delete sesuatu
    # Misalnya, ada matkul di Semester 1 dan kita delete Semester 1 nya apa yang bakal terjadi sama si matkul nya?
    # Untuk itu kita buat on_delete = CASCADE agar otomotis men-delete semua matkul yang berhubungn dengan Semester 1 tadi.
    term = models.ForeignKey(Semester, on_delete=CASCADE, related_name='matkul_semester')

    nama_matkul = models.CharField(max_length=64)
    kode_matkul = models.CharField(max_length=10)
    jumlah_sks = models.PositiveIntegerField()
    dosen_pengajar = models.CharField(max_length=64)
    deskripsi = models.TextField(max_length=200)
    ruang_kelas = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nama_matkul} ({self.kode_matkul}) - {self.jumlah_sks} sks"

class TugasMatkul(models.Model):
    deskripsi_tugas = models.TextField(max_length=100)
    matkul = models.ForeignKey(MataKuliah, on_delete=CASCADE, related_name='tugas_matkul')
    deadline = models.DateTimeField()

    def __str__(self):
        return f"Deskripsi : {self.deskripsi_tugas} \nDeadline : {self.deadline}"