from django.shortcuts import render
from django.views.generic import ListView, DetailView
import pandas as pd
from .models import Sale
from .forms import SalesSearchForm


def home_view(request):
    form = SalesSearchForm(request.POST or None)  # without or None it get executed automatically

    if request.method == "POST":
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

    qs = Sale.objects.filter(created__date=date_from)
    obj = Sale.objects.get(id=1)
    df1 = pd.DataFrame(qs.values())

    context = {'form': form}
    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'


class SaleDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
