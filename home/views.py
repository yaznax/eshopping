from django.shortcuts import render
from django.views.generic import View
from .models import *
# Create your views here.
class BaseViews(View):
    views = {}

class HomeView(BaseViews):
    def get(self,request):
        self.views['items'] = Item.objects.filter(labels = 'hot')
        self.views['sale_items'] = Item.objects.filter(labels = 'sale')
        self.views['category'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['subcategory'] = SubCategory.objects.all()
        self.views['ad'] = Ad.objects.all()
        self.views['brand'] = Brand.objects.all()
        

                 
        return render(request,"index.html",self.views)
