from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import View,ListView
from CartApp.models import Products
from django.db.models import Sum
from CartApp.models import Carts
from CartApp.filters import productfilter
from django.contrib import messages
# Create your views here.


class IndexView(View):
    def get(self,request,*args,**kwargs):
        qs=Products.objects.all()
        filter=productfilter(request.GET,queryset=Products.objects.all())
        context = {'datas': qs,'filter': filter}
        return render(request,"product.html",context)
        
    

class AddToCart(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=Products.objects.get(id=id)
        cart=Carts(item=book)
        cart.save()
        messages.success(request, "Product is added to the cart")
        return redirect("home")


class CartsView(ListView):
    def get(self,request,*args,**kwargs):
        datas=Carts.objects.all()
        context = {'datas': datas}
        return render(request,"carts.html",context)
    