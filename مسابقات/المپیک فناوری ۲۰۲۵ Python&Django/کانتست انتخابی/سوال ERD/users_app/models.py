from django.db import models


class AdminUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    national_id = models.CharField(max_length=10)
    address = models.TextField()
    admin_code = models.CharField(max_length=10)
    permissions_json = models.TextField()
    status = models.CharField(max_length=20, default='active')
    joined_at = models.DateTimeField(auto_now_add=True)


class CustomerUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    national_id = models.CharField(max_length=10)
    address = models.TextField()
    zipcode = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    loyalty_points = models.IntegerField(default=0)
    status = models.CharField(max_length=20, default='active')
    joined_at = models.DateTimeField(auto_now_add=True)


class VendorUser(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    national_id = models.CharField(max_length=10)
    address = models.TextField()
    shop_name = models.CharField(max_length=150)
    shop_address = models.TextField()
    shop_license_number = models.CharField(max_length=50)
    shop_phone = models.CharField(max_length=20)
    rating = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='active')
    joined_at = models.DateTimeField(auto_now_add=True)

class CustomUser(models.Model):
    USER_TYPES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin')
    )

    USER_STATUS = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('suspended', 'Suspended')
    )

    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=17)
    profile_picture = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20)
    address = models.TextField()
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    status = models.CharField(max_length=20, choices=USER_STATUS)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class CustomerProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    zipcode = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=20)
    loyalty_points = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class VendorProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=150)
    shop_address = models.TextField()
    shop_license_number = models.CharField(max_length=50)
    shop_phone = models.CharField(max_length=17)
    rating = models.FloatField(default=0.0)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AdminProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admin_code = models.CharField(max_length=10)
    permissions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)