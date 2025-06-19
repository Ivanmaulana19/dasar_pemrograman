from django.http import HttpResponse

def alamat_view(request):
    return HttpResponse("Alamat: Jl. Cisaat NO.13, Cisaat, Sukabumi, Jawa Barat 43151, Indonesia")

def telepon_view(request):
    return HttpResponse("Telepon: +62 856-2416-9201")
