from main.models import Product

from rest_framework.serializers import ModelSerializer



class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'is_checked', 'name', 'description', 'price', 'stock')

class ProductCheckSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ('is_checked',)
