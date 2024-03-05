from rest_framework import status
from rest_framework.reverse import reverse

from lab1.models import Cars, Customers, Brand, CarsSold
from rest_framework.test import APIClient

from lab1.urls import urlpatterns

from django.test import TestCase
from lab1.serializers import serializers, StatisticsSerializer, StatisticsSerializer2


class statistics_testcase(TestCase):

    def setUp(self):
        brand1 = Brand.objects.create(
            brand='a',
            year=2000,
            owner_name="aa",
            employees=3000,
            country="aaa"
        )
        brand2 = Brand.objects.create(
            brand='b',
            year=2010,
            owner_name="bb",
            employees=2500,
            country="bbb"
        )
        car1 = Cars.objects.create(
            name='car1',
            description='descr',
            brand=brand1,
            review="review",
            price=5000,
        )
        car2 = Cars.objects.create(
            name='car2',
            description='descr',
            brand=brand2,
            review="review",
            price=4000,
        )
        car3 = Cars.objects.create(
            name='car3',
            description='descr',
            brand=brand2,
            review="review",
            price=3000,
        )


        customer1 = Customers.objects.create(
            name_of_customer='customer1',
            year_of_birth=2000,
            address="addr",
            gender="M",
            phone=123
        )

        customer2 = Customers.objects.create(
            name_of_customer='customer2',
            year_of_birth=1990,
            address="addr",
            gender="F",
            phone=234
        )

        CarsSold.objects.create(
            customers_id=customer1,
            cars_id=car1,
            date="2000-12-20",
            amount=4500
        )

        CarsSold.objects.create(
            customers_id=customer2,
            cars_id=car2,
            date="2000-12-20",
            amount=3500
        )

    # brands ordered by the average of their car prices
    def test_statistics_brands(self):
        client = APIClient()
        url = reverse('statistics_brands')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                "id": 1,
                "brand": "a",
                "avg_price": 5000,
            },
            {
                "id": 2,
                "brand": "b",
                "avg_price": 3500,
            }
        ]
        serializer = StatisticsSerializer(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)

    # customers ordered by the average of their cars bought amount
    def test_statistics_customers(self):
        client = APIClient()
        url = reverse('statistics_customers')
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {
                "id": 1,
                "name_of_customer": "customer1",
                "avg_amount": 4500,
                "cars_sold_count": 1
            },
            {
                "id": 2,
                "name_of_customer": "customer2",
                "avg_amount": 3500,
                "cars_sold_count": 1
            }

        ]
        serializer = StatisticsSerializer2(expected_data, many=True)
        self.assertEqual(response.data, serializer.data)
