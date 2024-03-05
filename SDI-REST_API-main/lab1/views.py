from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt

from .models import Cars, Brand, Customers, CarsSold
from .serializers import CarSerializer, CarDetailSerializer, CarsSoldSerializer, CarsSoldDetailSerializer
from .serializers import StatisticsSerializer, StatisticsSerializer2
from .serializers import BrandSerializer, BrandDetailSerializer
from .serializers import CustomerSerializer, CustomerFilterSerializer, CustomerDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count

# A request handler that returns the relevant template and content - based on the request from the user
# takes http requests and returns http response, like HTML documents


class CarsAPIView(APIView):
    @api_view(('GET', 'POST'))
    def cars_list(request, format=None):

        # get all Cars
        # serialize them
        # return response (json)

        id = request.query_params.get('id')
        if request.method == 'GET':
            # get id
            if id:
                cars = Cars.objects.filter(id=id)
            # Cars = Cars.objects.all()
            # serializer = CarSerializer(Cars, many=True)
            # return JsonResponse({"Cars": serializer.data})
            # return Response(serializer.data)
            else:
                cars = Cars.objects.all()
            serializer = CarSerializer(cars, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(serializer.errors)
                return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'PUT', 'DELETE'])
    def cars_detail(request, id, format=None):
        try:
            cars = Cars.objects.get(pk=id)
        except Cars.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            # get id
            serializer = CarDetailSerializer(cars)
            return Response(serializer.data)

        if request.method == 'PUT':
            # update id
            serializer = CarDetailSerializer(cars, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        if request.method == 'DELETE':
            cars.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class BrandAPIView(APIView):
    @api_view(['GET', 'POST'])
    def brand_list(request, format=None):
        if request.method == 'GET':
            brand = Brand.objects.all()
            serializer = BrandSerializer(brand, many=True)

            return Response(serializer.data)

        if request.method == 'POST':
            serializer = BrandSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'PUT', 'DELETE'])
    def brand_detail(request, id, format=None):

        try:
            brand = Brand.objects.get(pk=id)
        except Brand.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BrandDetailSerializer(brand)
            return Response(serializer.data)

        elif request.method == 'PUT':
            # update
            serializer = BrandSerializer(brand, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            brand.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerAPIView(APIView):
    @api_view(['GET', 'POST'])
    def customer_list(request, format=None):

        if request.method == 'GET':
            customers = Customers.objects.all()
            serializer = CustomerSerializer(customers, many=True)

            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CustomerSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'PUT', 'DELETE'])
    def customer_detail(request, id, format=None):

        try:
            customers = Customers.objects.get(pk=id)
        except Customers.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CustomerDetailSerializer(customers)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CustomerSerializer(customers, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            customers.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(['GET'])
    def customer_filtered_list(request, year, format=None):

        if request.method == 'GET':

            customers = Customers.objects.filter(year_of_birth__gt=year)

            serializer = CustomerFilterSerializer(customers, many=True)

            return Response(serializer.data)


class CarsSoldAPIView(APIView):
    @api_view(['GET', 'POST'])
    def cars_sold_list(request, format=None):
        if request.method == 'GET':
            cars_sold = CarsSold.objects.all()
            serializer = CarsSoldSerializer(cars_sold, many=True)

            return Response(serializer.data)

        if request.method == 'POST':
            serializer = CarsSoldSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            print(serializer.errors)
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'PUT', 'DELETE'])
    def cars_sold_detail(request, id, format=None):

        try:
            cars_sold = CarsSold.objects.get(pk=id)
        except CarsSold.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CarsSoldDetailSerializer(cars_sold)
            # serializer = CustomerscarsSerializer(cars_sold)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CarsSoldSerializer(cars_sold, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            cars_sold.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


class Statistics(APIView):
    @api_view(['GET'])
    def statistics_brands(request):
        # brands ordered by the average of their cars price
        statistics = Brand.objects.annotate(
            avg_price=Avg('cars__price'),
            car_count=Count('cars')
        ).order_by('-avg_price')

        serializer = StatisticsSerializer(statistics, many=True)
        return Response(serializer.data)

    # done in class
    @api_view(['GET'])
    def statistics_customers(request):
        # customers ordered by the average of their cars bought amount
        statistics = Customers.objects.annotate(
            avg_amount=Avg('customers_id__amount'),
            cars_sold_count=Count('customers_id')
        ).order_by('-avg_amount')

        serializer = StatisticsSerializer2(statistics, many=True)
        return Response(serializer.data)


class BulkAddView(APIView):
    @csrf_exempt
    @api_view(['POST'])
    def bulkAddBrand(request):
        car_id_new_brand_list = request.data.get('car_id_new_brand_list')

        # Loop through the list of car ids and new brand to update
        for item in car_id_new_brand_list:
            cars = Cars.objects.get(id=item['cars_id'])
            cars.brand = Brand.objects.get(brand=item['new_brand'])
            cars.save()

        return Response({'message': 'Cars updated successfully.'})
