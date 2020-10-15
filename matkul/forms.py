from django import forms
from .models import MataKuliah

class MataKuliahForm(forms.ModelForm):
    # class Meta ngasih tau models apa yang kita untuk ngebuat form ini.
    class Meta:
        model = MataKuliah
        fields = ["term","nama_matkul", "kode_matkul", "jumlah_sks", "dosen_pengajar", "deskripsi", "ruang_kelas"]
        