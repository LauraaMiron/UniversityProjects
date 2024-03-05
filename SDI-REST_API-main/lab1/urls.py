from django.contrib import admin
from django.urls import path
from lab1 import views
from rest_framework.urlpatterns import format_suffix_patterns

# When a user requests a URL, Django decides which view it will send it to.

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cars/", views.CarsAPIView.cars_list),
    path("cars/<int:id>", views.CarsAPIView.cars_detail),
    path('brand/', views.BrandAPIView.brand_list),
    path('brand/<int:id>', views.BrandAPIView.brand_detail),
    path('customers/', views.CustomerAPIView.customer_list),
    path('customers/<int:id>', views.CustomerAPIView.customer_detail),
    path('customers/filtered/<int:year>', views.CustomerAPIView.customer_filtered_list),
    path('buy/', views.CarsSoldAPIView.cars_sold_list),
    path('buy/<int:id>', views.CarsSoldAPIView.cars_sold_detail),
    path("brand/statistics/", views.Statistics.statistics_brands, name='statistics_brands'),
    path("customers/statistics/", views.Statistics.statistics_customers, name='statistics_customers')
]

urlpatterns = format_suffix_patterns(urlpatterns)
