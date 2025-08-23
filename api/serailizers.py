from rest_framework import serializers
from .models import Profile, Category, Product, Tag
from django.contrib.auth.models import User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
        
        

class ProfileSerializers(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'bio', 'user']
        read_only_fields = ['user']
        
class CategorySerializers(serializers.ModelSerializer):
    product_count = serializers.IntegerField(source='products.count', read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'product_count']
        
