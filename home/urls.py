from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('subcategory/<slug>', SubCategoryView.as_view(), name='subcategory'),
    path('detail/<slug>', ProductDetailView.as_view(), name='detail'),
    path('search', SearchView.as_view(), name='search'),
    path('review', review, name='review'),
    path('signup', signup, name='signup'),
    path('cart/<slug>', cart, name='cart'),
    path('mycart', CartView.as_view(), name='mycart'),
    path('deletecart/<slug>', deletecart, name='deletecart'),
    path('removecart/<slug>', removecart, name='removecart'),
]

