from rest_framework import serializers
from .models import *

# Serializers define the API representation.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['title','slug','price','discounted_price','description','image','category','subcategory','status','stock','labels']

