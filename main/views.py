from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.response import Response
from main.models import Product
from main.serializers import ProductSerializer, ProductCheckSerializer
from main.utils import get_or_create_user_auth_with_email
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def authenticate_user(request):
    
    if request.method == 'POST':
        
        email = json.loads(request.body)['email']
        user, token = get_or_create_user_auth_with_email(email)
        login(request, user)

        return JsonResponse({'success': True, 'token': token.key})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})


def change_product(request, id):
    try:
        item = Product.objects.get(pk=id)
    except Product.DoesNotExist:
        return Response(status=404)
    serializer = ProductCheckSerializer(item, data=json.loads(request.body))
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
    
class ProductAPIListView(APIView):
    def get(self, request, format=None):
        items = Product.objects.order_by('pk')
        serializer = ProductSerializer(items, many=True)
        return Response(serializer.data)