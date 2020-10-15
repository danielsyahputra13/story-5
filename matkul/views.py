from django.http import request
from django.shortcuts import render, redirect
from .models import Semester, MataKuliah, TugasMatkul
from .forms import MataKuliahForm, SemesterForm

# Create your views here.
def index(request):
    terms = Semester.objects.all()
    return render(request, 'matkul/index.html', {
        "terms" : terms
    })


def semester(request, semester_id):
    semester = Semester.objects.get(semester_id=semester_id)
    courses = MataKuliah.objects.filter(term=semester)
    return render(request, "matkul/semester.html", {
        "semester" : semester,
        "courses" : courses
    })

def tambah(request):
    if request.method == "POST":
        form = MataKuliahForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tambah')
    else:
        form = MataKuliahForm()
        return render(request, 'matkul/tambah.html', {
            'form': form
        })

def tambah_semester(request):
    if request.method == "POST":
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tambah_semester')
    else:
        form = SemesterForm()
        return render(request, 'matkul/tambah_semester.html', {
            'form': form
        })


def detail(request, pk):
    matkul = MataKuliah.objects.get(pk=pk)
    return render(request, 'matkul/detail.html', {
        'course': matkul
    })

def hapus(request, pk):
    matkul = MataKuliah.objects.get(pk=pk)
    matkul.delete()
    return redirect('index')