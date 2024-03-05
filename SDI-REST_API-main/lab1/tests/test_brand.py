from unittest import TestCase

from lab1.models import Brand


class BrandModelTestcase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Brand.objects.create(brand="Mercedes", year=1990, owner_name="Daniel", employees=1000, country="France")

    #def test_string_method(self):
    #     brand = Brand.objects.get(brand="Mercedes")
    #     expected_string = "Mercedes"
    #     self.assertEqual(str(brand), expected_string)