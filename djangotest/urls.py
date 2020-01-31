from django.contrib import admin
from django.urls import path, include
from customers import views
from django.views.decorators.csrf import csrf_exempt

#customer_url = Customers()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', csrf_exempt(views.CustomerCollectionView.as_view()), name= 'customer_collection'),
]
