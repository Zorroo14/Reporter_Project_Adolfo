'''
Created on 1/8/2016

@author: adolfo
'''

from __future__ import unicode_literals

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from reporter.models import Galleta
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy


class GalletaCreate(CreateView):
    model = Galleta
    fields = '__all__'
    success_url = "galleta/list"
    
class GalletaUpdate(UpdateView):
    model = Galleta
    fields = '__all__'
    success_url = reverse_lazy('galleta_list')
    
class GalletaDelete(DeleteView):
    model = Galleta
    fields = '__all__'
    success_url = "galleta/list"
            
class GalletaListView(ListView):
    model = Galleta