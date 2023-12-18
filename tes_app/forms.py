from django import forms
from .models import Produk, Kategori, Status

class produk_form(forms.ModelForm):
    id_produk   = forms.IntegerField(label="id produk", widget=forms.TextInput(attrs={'placeholder':'id', 'class':'form-control'}))
    nama_produk = forms.CharField(label="nama produk", max_length=100, widget=forms.TextInput(attrs={'placeholder':'nama', 'class':'form-control'}))
    harga       = forms.CharField(label="harga", widget=forms.TextInput(attrs={'placeholder':'harga', 'class':'form-control'}))
    kategori = forms.ModelChoiceField(label="kategori", queryset=Kategori.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    status      = forms.ModelChoiceField(label="status", queryset=Status.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model= Produk
        fields=('id_produk', 'nama_produk', 'harga', 'kategori', 'status')
    
    # terpanggil otomatis untuk validasi harga
    def clean_harga(self):
        harga = self.cleaned_data.get('harga')

        # Check if the value is numeric
        if not harga.isdigit():
            raise forms.ValidationError('Harga harus angka.')

        return harga
		