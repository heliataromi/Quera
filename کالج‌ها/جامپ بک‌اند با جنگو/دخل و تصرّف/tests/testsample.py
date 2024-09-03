from django.contrib import admin
from django.test import TestCase

from store.models import Product, Company, Address, Category


class CustomAdminTest(TestCase):
    fixtures = ['store']

    def setUp(self):
        self.prod_admin = admin.site._registry.get(Product)
        self.comp_admin = admin.site._registry.get(Company)
        self.addr_admin = admin.site._registry.get(Address)
        self.catg_admin = admin.site._registry.get(Category)

    def test_models_are_registered(self):
        self.assertTrue(Product in admin.site._registry, '\nپنل ادمینی برای مدل Product ایجاد نکرده‌اید.')
        self.assertTrue(Company in admin.site._registry, '\nپنل ادمینی برای مدل Company ایجاد نکرده‌اید.')
        self.assertTrue(Address in admin.site._registry, '\nپنل ادمینی برای مدل Address ایجاد نکرده‌اید.')
        self.assertTrue(Category in admin.site._registry, '\nپنل ادمینی برای مدل Category ایجاد نکرده‌اید.')