from decimal import Decimal

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import connection
from django.test import TransactionTestCase
from django.utils import timezone


class UserDataMigrationTest(TransactionTestCase):
    """
    Test the data migration from old user models to new refactored models.
    Uses TransactionTestCase to handle schema changes during migration testing.
    """

    def setUp(self):
        self.create_sample_fixture_data()

        self.AdminUser = apps.get_model('users_app', 'AdminUser')
        self.CustomerUser = apps.get_model('users_app', 'CustomerUser')
        self.VendorUser = apps.get_model('users_app', 'VendorUser')

        self.CustomUser = apps.get_model('users_app', 'CustomUser')
        self.AdminProfile = apps.get_model('users_app', 'AdminProfile')
        self.CustomerProfile = apps.get_model('users_app', 'CustomerProfile')
        self.VendorProfile = apps.get_model('users_app', 'VendorProfile')

    def create_sample_fixture_data(self):
        self.fixture_data = [
            {
                "model": "users_app.adminuser",
                "pk": 1,
                "fields": {
                    "email": "admin@example.com",
                    "password": make_password("admin123"),
                    "firstname": "Admin",
                    "lastname": "User",
                    "phone": "+1234567890",
                    "national_id": "ADMIN001",
                    "address": "123 Admin St",
                    "admin_code": "ADM001",
                    "permissions_json": {"can_manage_users": True, "can_manage_products": True},
                    "status": "active",
                    "joined_at": timezone.now(),
                }
            },
            {
                "model": "users_app.customeruser",
                "pk": 1,
                "fields": {
                    "email": "customer@example.com",
                    "password": make_password("customer123"),
                    "firstname": "Customer",
                    "lastname": "User",
                    "phone": "+1234567891",
                    "national_id": "CUST001",
                    "address": "456 Customer Ave",
                    "zipcode": "12345",
                    "birth_date": "1990-01-01",
                    "gender": "male",
                    "loyalty_points": 100,
                    "status": "active",
                    "joined_at": timezone.now(),
                }
            },
            {
                "model": "users_app.vendoruser",
                "pk": 1,
                "fields": {
                    "email": "vendor@example.com",
                    "password": make_password("vendor123"),
                    "firstname": "Vendor",
                    "lastname": "User",
                    "phone": "+1234567892",
                    "national_id": "VEND001",
                    "address": "789 Vendor Blvd",
                    "shop_name": "Vendor Shop",
                    "shop_address": "789 Shop St",
                    "shop_license_number": "SHOP001",
                    "shop_phone": "+1234567893",
                    "rating": "4.5",
                    "is_verified": True,
                    "status": "active",
                    "joined_at": timezone.now(),
                }
            }
        ]

    def create_old_models_data(self):
        # Create admin user
        self.admin_user = self.AdminUser.objects.create(
            email="admin@example.com",
            password=make_password("admin123"),
            firstname="Admin",
            lastname="User",
            phone="+1234567890",
            national_id="ADMIN001",
            address="123 Admin St",
            admin_code="ADM001",
            permissions_json={"can_manage_users": True, "can_manage_products": True},
            status="active",
            joined_at=timezone.now()
        )

        # Create customer user
        self.customer_user = self.CustomerUser.objects.create(
            email="customer@example.com",
            password=make_password("customer123"),
            firstname="Customer",
            lastname="User",
            phone="+1234567891",
            national_id="CUST001",
            address="456 Customer Ave",
            zipcode="12345",
            birth_date="1990-01-01",
            gender="male",
            loyalty_points=100,
            status="active",
            joined_at=timezone.now()
        )

        # Create vendor user
        self.vendor_user = self.VendorUser.objects.create(
            email="vendor@example.com",
            password=make_password("vendor123"),
            firstname="Vendor",
            lastname="User",
            phone="+1234567892",
            national_id="VEND001",
            address="789 Vendor Blvd",
            shop_name="Vendor Shop",
            shop_address="789 Shop St",
            shop_license_number="SHOP001",
            shop_phone="+1234567893",
            rating=Decimal('4.5'),
            is_verified=True,
            status="active",
            joined_at=timezone.now()
        )

    def test_migration_forward(self):
        self.create_old_models_data()

        admin_count = self.AdminUser.objects.count()
        customer_count = self.CustomerUser.objects.count()
        vendor_count = self.VendorUser.objects.count()

        print(f"Before migration - Admins: {admin_count}, Customers: {customer_count}, Vendors: {vendor_count}")

        # Step 2: Run the migration (this would normally be done by Django migrations)
        # We'll simulate this by calling the migration functions directly
        from users_app.migrations.utils.user_migration import migrate_users_forward  # Replace with actual import

        # Create schema editor mock for the migration
        from django.db import connection

        # Run the migration function
        migrate_users_forward(apps, connection.schema_editor())

        # Check counts
        self.assertEqual(self.CustomUser.objects.count(), admin_count + customer_count + vendor_count)
        self.assertEqual(self.AdminProfile.objects.count(), admin_count)
        self.assertEqual(self.CustomerProfile.objects.count(), customer_count)
        self.assertEqual(self.VendorProfile.objects.count(), vendor_count)

        # Verify admin user migration
        admin_user = self.CustomUser.objects.get(email="admin@example.com")
        self.assertEqual(admin_user.user_type, 'admin')
        self.assertEqual(admin_user.first_name, "Admin")
        self.assertEqual(admin_user.last_name, "User")
        self.assertEqual(admin_user.phone, "+1234567890")
        self.assertEqual(admin_user.national_id, "ADMIN001")
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        # Verify admin profile
        admin_profile = self.AdminProfile.objects.get(user=admin_user)
        self.assertEqual(admin_profile.admin_code, "ADM001")
        self.assertEqual(admin_profile.permissions, str({"can_manage_users": True, "can_manage_products": True}))

        # Verify customer user migration
        customer_user = self.CustomUser.objects.get(email="customer@example.com")
        self.assertEqual(customer_user.user_type, 'customer')
        self.assertEqual(customer_user.first_name, "Customer")
        self.assertEqual(customer_user.last_name, "User")
        self.assertFalse(customer_user.is_staff)
        self.assertFalse(customer_user.is_superuser)

        # Verify customer profile
        customer_profile = self.CustomerProfile.objects.get(user=customer_user)
        self.assertEqual(customer_profile.zipcode, "12345")
        self.assertEqual(customer_profile.gender, "male")
        self.assertEqual(customer_profile.loyalty_points, 100)

        # Verify vendor user migration
        vendor_user = self.CustomUser.objects.get(email="vendor@example.com")
        self.assertEqual(vendor_user.user_type, 'vendor')
        self.assertEqual(vendor_user.first_name, "Vendor")
        self.assertEqual(vendor_user.last_name, "User")

        # Verify vendor profile
        vendor_profile = self.VendorProfile.objects.get(user=vendor_user)
        self.assertEqual(vendor_profile.shop_name, "Vendor Shop")
        self.assertEqual(vendor_profile.shop_license_number, "SHOP001")
        self.assertEqual(vendor_profile.rating, Decimal('4.5'))
        self.assertTrue(vendor_profile.is_verified)

        print("Forward migration test passed!")

    def test_data_integrity(self):
        """Test that all data is preserved during migration"""
        # Create old model data
        self.create_old_models_data()

        original_admin = self.AdminUser.objects.get(email="admin@example.com")
        original_customer = self.CustomerUser.objects.get(email="customer@example.com")
        original_vendor = self.VendorUser.objects.get(email="vendor@example.com")

        # Run migration
        from users_app.migrations.utils.user_migration import migrate_users_forward
        migrate_users_forward(apps, connection.schema_editor())

        # Check admin data integrity
        migrated_admin = self.CustomUser.objects.get(email="admin@example.com")
        admin_profile = self.AdminProfile.objects.get(user=migrated_admin)

        self.assertEqual(migrated_admin.email, original_admin.email)
        self.assertEqual(migrated_admin.first_name, original_admin.firstname)
        self.assertEqual(migrated_admin.last_name, original_admin.lastname)
        self.assertEqual(migrated_admin.phone, original_admin.phone)
        self.assertEqual(migrated_admin.national_id, original_admin.national_id)
        self.assertEqual(migrated_admin.address, original_admin.address)
        self.assertEqual(migrated_admin.password, original_admin.password)
        self.assertEqual(admin_profile.admin_code, original_admin.admin_code)

        # Check customer data integrity
        migrated_customer = self.CustomUser.objects.get(email="customer@example.com")
        customer_profile = self.CustomerProfile.objects.get(user=migrated_customer)

        self.assertEqual(migrated_customer.email, original_customer.email)
        self.assertEqual(migrated_customer.first_name, original_customer.firstname)
        self.assertEqual(customer_profile.zipcode, original_customer.zipcode)
        self.assertEqual(customer_profile.loyalty_points, original_customer.loyalty_points)

        # Check vendor data integrity
        migrated_vendor = self.CustomUser.objects.get(email="vendor@example.com")
        vendor_profile = self.VendorProfile.objects.get(user=migrated_vendor)

        self.assertEqual(migrated_vendor.email, original_vendor.email)
        self.assertEqual(migrated_vendor.first_name, original_vendor.firstname)
        self.assertEqual(vendor_profile.shop_name, original_vendor.shop_name)
        self.assertEqual(vendor_profile.shop_license_number, original_vendor.shop_license_number)
        self.assertEqual(vendor_profile.rating, original_vendor.rating)
        self.assertEqual(vendor_profile.is_verified, original_vendor.is_verified)

        print("Data integrity test passed!")

    def test_unique_constraints(self):
        """Test that unique constraints are maintained after migration"""
        # Create old model data with unique fields
        self.create_old_models_data()

        # Run migration
        from users_app.migrations.utils.user_migration import migrate_users_forward
        migrate_users_forward(apps, connection.schema_editor())

        # Check email uniqueness
        emails = self.CustomUser.objects.values_list('email', flat=True)
        self.assertEqual(len(emails), len(set(emails)))

        # Check national_id uniqueness
        national_ids = self.CustomUser.objects.values_list('national_id', flat=True)
        self.assertEqual(len(national_ids), len(set(national_ids)))

        # Check admin_code uniqueness
        admin_codes = self.AdminProfile.objects.values_list('admin_code', flat=True)
        self.assertEqual(len(admin_codes), len(set(admin_codes)))

        # Check shop_license_number uniqueness
        shop_licenses = self.VendorProfile.objects.values_list('shop_license_number', flat=True)
        self.assertEqual(len(shop_licenses), len(set(shop_licenses)))

        print("Unique constraints test passed!")

#
# # Additional helper functions for running tests
# def run_migration_test():
#     """Helper function to run the migration tests"""
#     import django
#     from django.conf import settings
#     from django.test.utils import get_runner
#
#     # Configure Django settings if not already configured
#     if not settings.configured:
#         settings.configure(
#             DATABASES={
#                 'default': {
#                     'ENGINE': 'django.db.backends.sqlite3',
#                     'NAME': ':memory:',
#                 }
#             },
#             INSTALLED_APPS=[
#                 'django.contrib.auth',
#                 'django.contrib.contenttypes',
#                 'users_app',  # Replace with your actual app name
#             ],
#             USE_TZ=True,
#         )
#
#     django.setup()
#
#     # Run the tests
#     TestRunner = get_runner(settings)
#     test_runner = TestRunner()
#     failures = test_runner.run_tests(["__main__.UserDataMigrationTest"])
#
#     return failures
#
#
# if __name__ == '__main__':
#     # Run the test
#     failures = run_migration_test()
#     if failures:
#         print(f"Tests failed: {failures}")
#     else:
#         print("All tests passed!")
