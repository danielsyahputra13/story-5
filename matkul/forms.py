from django import forms
from django.forms import fields
from .models import MataKuliah, Semester

class MataKuliahForm(forms.ModelForm):
    # class Meta ngasih tau models apa yang kita untuk ngebuat form ini.
    class Meta:
        model = MataKuliah
        fields = ["term","nama_matkul", "kode_matkul", "jumlah_sks", "dosen_pengajar", "deskripsi", "ruang_kelas"]
        
class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['semester_id']