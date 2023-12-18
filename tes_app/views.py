from django.shortcuts import redirect, render
from .models import Produk, Kategori, Status
from django.contrib import messages
from .forms import produk_form

# Create your views here.
def produk(request):
    produk=Produk.objects.all()
    return render(request, 'produk.html', {'produk': produk})

def delete_produk(request, pk):
    produk=Produk.objects.get(id_produk=pk)
    produk.delete()
    messages.success(request, "Produk terhapus")
    return redirect('produk')

def insert_produk(request):
    form=produk_form(request.POST or None)
    # ketika method post dan valid (submit form)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "produk berhasil ditambahkan")
        return redirect('produk')
    # jika tidak valid arahkan ke halaman insert
    else:
        return render(request, 'insert_produk.html', {'form': form})

def update_produk(request, pk):
    produk=Produk.objects.get(id_produk=pk)
    form=produk_form(request.POST or None, instance=produk, initial={'kategori_id': produk.kategori, 'status_id': produk.status})

    # # ketika valid, maka dianggap submit update
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, "produk berhasil diupdate")
    #     return redirect('produk')
    # # jika tidak valid, arahkan ke halaman edit
    # else:
    return render(request, 'update_produk.html', {'form': form, 'produk_id':pk})

def produk_bisa_dijual(request):
    produk=Produk.objects.filter(status_id=1)
    return render(request, 'produk.html', {'produk': produk})