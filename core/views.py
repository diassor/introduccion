from django.views.generic import View
from django.shortcuts import render

class HomeView(View):
    # siempre que trabajemos con class debemos usar self
    # args y kwargs hace referencia a cualquier variable o parametro que cualquier objeto que request 
    # pueda tener
    def get(self, request, *args, **kwargs):
        context = {}
        return render (request, 'index.html', context)