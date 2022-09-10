from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    catalog_item = CatalogItem.objects.all()
    context = {
        'list_barang': catalog_item,
        'nama': 'Vinsensius Ferdinando'
    }
    return render(request, "katalog.html", context)