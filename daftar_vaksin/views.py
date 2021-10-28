from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import DaftarVaksinForm
from tambah_vaksin.models import Vaksin
from biodata.models import Peserta

# Create your views here.

@login_required(login_url='/auth/login/')
def daftar_vaksin(request):
    form = DaftarVaksinForm(request.POST or None)

    if (form.is_valid() and request.method == 'POST'):
        person = Peserta.objects.get(superUser=request.user)
        jadwal = form.save(commit=False)
        jadwal.penerima = person
        jadwal.save()
        return HttpResponseRedirect('/')
    else:
        form = DaftarVaksinForm()

    return render(request, 'daftar_vaksin.html', {'form': form})


def load_tanggal(request):
    kota_id = request.GET.get('kota')
    tanggal = Vaksin.objects.filter(penyedia__kota=kota_id).values_list(
        'tanggal', flat=True).distinct()
    return render(request, 'hr/tanggal_dropdown.html', {'tanggal': tanggal})

def load_jenis_vaksin(request):
    tanggal_id = request.GET.get('tanggal')
    jenis_vaksin = Vaksin.objects.filter(tanggal=tanggal_id).values_list('jenis', flat=True).distinct()
    return render(request, 'hr/jenis_dropdown.html', {'jenis_vaksin': jenis_vaksin})

def load_tempat(request):
    jenis_id = request.GET.get('jenis_vaksin')
    tempat = Vaksin.objects.filter(jenis=jenis_id).distinct()
    return render(request, 'hr/tempat_dropdown.html', {'tempat': tempat})

