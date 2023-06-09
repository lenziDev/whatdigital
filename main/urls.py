from main import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path('auth/', csrf_exempt(views.authenticate_user), name='authenticate_user'),
  path('products/', views.ProductAPIListView.as_view(), name="products"),
  path('product/<int:id>/', csrf_exempt(views.change_product), name='change_product'),
]