from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from rest_framework import serializers
from .models import Cars, Brand, Customers, CarsSold

from rest_framework.generics import  GenericAPIView,ListAPIView
from rest_framework.viewsets import ModelViewSet

# converting objects into data types understandable by javascript and front-end frameworks (json)
# visible also to clients


class CarSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    review = serializers.CharField(max_length=255)
    price = serializers.IntegerField(default=0)
    brand = serializers.SlugRelatedField(queryset=Brand.objects.all(), slug_field='brand')

    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'review', 'price', 'brand']
        # depth = 1

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price can't be negative")
        return value


class CarDetailSerializer(serializers.ModelSerializer):
    customers = serializers.SerializerMethodField(read_only=True)  # for customers buy Cars

    class Meta:
        model = Cars
        fields = ['id', 'name', 'description', 'review', 'price', 'brand', 'customers']
        depth = 1

    # for customers buy Cars
    def get_customers(self, obj):
        customers = CarsSold.objects.filter(cars_id=obj)
        return CarsSoldSerializer(customers, many=True).data

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("The price can't be negative")
        return value


class BrandSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(max_length=255)
    owner_name = serializers.CharField(max_length=255)
    employees = serializers.IntegerField(default=0)
    country = serializers.CharField(max_length=255)
    year = serializers.IntegerField(default=0)
    class Meta:
        model = Brand
        fields = ['id', 'brand', 'year', 'owner_name', 'employees', 'country']

    def validate_year(self, value):
        if value < 1885:
            raise serializers.ValidationError("The year must be >1885.")
        return value


class BrandDetailSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'brand', 'year', 'owner_name', 'employees', 'country', 'cars']

    def validate_year(self, value):
        if value < 1885:
            raise serializers.ValidationError("The year must be >1885.")
        return value


class CustomerSerializer(serializers.ModelSerializer):
    name_of_customer = serializers.CharField(max_length=255)
    year_of_birth = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=255)
    phone = serializers.IntegerField(default=0)

    class Meta:
        model = Customers
        fields = ['id', 'name_of_customer', 'year_of_birth', 'address', 'gender', 'phone']

    def validate_phone(self, value):
        if value < 999999999:
            raise serializers.ValidationError("The phone number must be valid (10 digits).")
        return value


class CustomerDetailSerializer(serializers.ModelSerializer):
    customers_cars = serializers.SerializerMethodField()  # for customers buy Cars

    class Meta:
        model = Customers
        fields = ['id', 'name_of_customer', 'year_of_birth', 'address', 'gender', 'phone', 'customers_cars']

    def get_customers_cars(self, obj):
        customers_cars = CarsSold.objects.filter(customers_id=obj)
        return CarsSoldSerializer(customers_cars, many=True).data

    def validate_phone(self, value):
        if value < 999999999:
            raise serializers.ValidationError("The phone number must be valid (10 digits).")
        return value


class CustomerFilterSerializer(serializers.ModelSerializer):
    year_of_birth = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customers
        fields = ['id', 'year_of_birth']


class CarsSoldSerializer(serializers.ModelSerializer):
    customers_id = serializers.SlugRelatedField(queryset=Customers.objects.all(), slug_field='id')
    cars_id = serializers.SlugRelatedField(queryset=Cars.objects.all(), slug_field='id')

    class Meta:
        model = CarsSold
        fields = ['id', 'amount', 'date', 'customers_id', 'cars_id']


class CarsSoldDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsSold
        fields = ['id', 'amount', 'date', 'customers_id', 'cars_id']
        depth = 1


class StatisticsSerializer(serializers.ModelSerializer):
    avg_price = serializers.IntegerField(read_only=True)
    cars_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Brand
        fields = ['id', 'brand', 'avg_price', 'cars_count']


class StatisticsSerializer2(serializers.ModelSerializer):
    avg_amount = serializers.IntegerField(read_only=True)
    cars_sold_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Customers
        fields = ['id', 'name_of_customer', 'avg_amount', 'cars_sold_count']


class BulkAdd(serializers.ModelSerializer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cars = serializers.IntegerField(required=False)

    brand = serializers.CharField(max_length=255)
    owner_name = serializers.CharField(max_length=255)
    employees = serializers.IntegerField(default=0)
    country = serializers.CharField(max_length=255)
    year = serializers.IntegerField(default=0)

    def update_cars(self):
        Cars.objects.filter(id=int(str(self.publisher))).update(name=self.brand)

    class Meta:
        model = Brand
        fields = ['id', 'brand', 'year', 'owner_name', 'employees', 'country']
