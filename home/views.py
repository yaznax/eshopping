from django.shortcuts import render
from django.views.generic import View
from .models import *
# from django.urls import redirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
# def home(request):
# 	view = {"value":"Hello World"}

# 	return render(request,'index.html',view)

class BaseViews(View):
    views = {}
    views['category'] = Category.objects.all()
    views['subcategory'] = SubCategory.objects.all()
    views['brands'] = Brand.objects.all()

class HomeView(BaseViews):
    def get(self,request):
        self.views['items'] = Item.objects.filter(labels = 'hot')
        self.views['sale_items'] = Item.objects.filter(labels = 'sale')
        self.views['sliders'] = Slider.objects.all()
        self.views['ad'] = Ad.objects.all()
        

        return render(request,'index.html',self.views)

class SubCategoryView(BaseViews):
    def get(self,request,slug):
        slug_id = SubCategory.objects.get(slug = slug).id
        self.views['subcat_items'] = Item.objects.filter(subcategory_id = slug_id)
        return render(request,'subcat.html',self.views)


class ProductDetailView(BaseViews):
    def get(self,request,slug):
        self.views['details'] = Item.objects.filter(slug = slug)
        self.views['reviews'] = Review.objects.filter(product = slug)
        return render(request,'product-details.html',self.views)


def review(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        product = request.POST['product']
        comment = request.POST['comment']

        data = Review.objects.create(
            name = name,
            email = email,
            product = product,
            comment = comment
            )
        data.save()

    return redirect(f'/detail/{product}')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'This username is already taken')
                return redirect('home:signup')

            elif User.objects.filter(email = email).exists():
                messages.error(request,'This username is already taken')
                return redirect('home:signup')

            else:
                user = User.objects.create_user(
                    username = username,
                    email = email,
                    password = password,
                    first_name = fname,
                    last_name = lname
                    
                    )
                user.save()
                messages.success(request,'You are signuped!')
                return redirect('/')

        else:
            messages.success(request,'You are signuped!')
            return redirect('home:signup')

    return render(request,'signup.html')

class SearchView(BaseViews):
    def get(self,request):
        query = request.GET.get('query')
        if not query:
            return redirect('/')
        self.views['search_product'] = Item.objects.filter(title__icontains = query)
        return render(request,'search.html',self.views)

def cart(request,slug):
    if Cart.objects.filter(slug = slug, checkout = False).exists():
        quantity = Cart.objects.get(slug = slug, checkout = False).quantity
        quantity = quantity+1 
        Cart.objects.filter(slug = slug, checkout = False).update(quantity=quantity)
    else:
        username = request.user
        data = Cart.objects.create(
            user =username,
            slug = slug,
            itrms = Item.objects.filter(slug=slug),
            )
        data.save()
        return redirect('home:mycart')

class CartView(BaseViews):
        def get(self,request):
            self.views['carts'] = Cart.objects.filter(user = request.user)
            return render(request,'cart.html',self.views)