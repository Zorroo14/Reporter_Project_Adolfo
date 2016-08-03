'''
Created on 1/8/2016

@author: adolfo
'''

from __future__ import unicode_literals

from django.conf.urls import url
from reporter.generic import GalletaCreate, GalletaListView, GalletaUpdate, GalletaDelete

urlpatterns = [
        url("create$", GalletaCreate.as_view(),
            name="galleta_create"),
        url("update/(?P<pk>\d+)$", GalletaUpdate.as_view(),
            name="galleta_update"),
        url("delete/(?P<pk>\d+)$", GalletaDelete.as_view(),
            name="galleta_delete"),  
        url(r"list$", GalletaListView.as_view(),
            name="galleta_list")     
]
