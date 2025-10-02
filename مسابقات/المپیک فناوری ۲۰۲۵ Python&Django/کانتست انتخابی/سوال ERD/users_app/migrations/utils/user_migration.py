def migrate_users_forward(apps, schema_editor):
    AdminUser = apps.get_model('users_app', 'AdminUser')  # Replace 'users_app' with your actual app name
    CustomerUser = apps.get_model('users_app', 'CustomerUser')
    VendorUser = apps.get_model('users_app', 'VendorUser')

    CustomUser = apps.get_model('users_app', 'CustomUser')
    AdminProfile = apps.get_model('users_app', 'AdminProfile')
    CustomerProfile = apps.get_model('users_app', 'CustomerProfile')
    VendorProfile = apps.get_model('users_app', 'VendorProfile')

    user_id_mapping = {}
    for admin in AdminUser.objects.all():
        user = CustomUser.objects.create(
            username=admin.email,
            email=admin.email,
            first_name=admin.firstname,
            last_name=admin.lastname,
            phone=admin.phone,
            national_id=admin.national_id,
            address=admin.address,
            user_type='admin',
            status=admin.status,
            is_staff=True,
            is_superuser=True,
            date_joined=admin.joined_at,
        )
        user.created_at = admin.joined_at
        user.save()

        user.password = admin.password
        user.save()

        AdminProfile.objects.create(
            user=user,
            admin_code=admin.admin_code,
            permissions=admin.permissions_json if admin.permissions_json else {},
            created_at=admin.joined_at,
        )

        user_id_mapping[f'admin_{admin.id}'] = user.id


    for customer in CustomerUser.objects.all():
        user = CustomUser.objects.create(
            username=customer.email,
            email=customer.email,
            first_name=customer.firstname,
            last_name=customer.lastname,
            phone=customer.phone,
            national_id=customer.national_id,
            address=customer.address,
            user_type='customer',
            status=customer.status,
            date_joined=customer.joined_at,
        )
        user.created_at = customer.joined_at
        user.save()

        user.password = customer.password
        user.save()

        CustomerProfile.objects.create(
            user=user,
            zipcode=customer.zipcode,
            birth_date=customer.birth_date,
            gender=customer.gender,
            loyalty_points=customer.loyalty_points,
            created_at=customer.joined_at,
        )

        user_id_mapping[f'customer_{customer.id}'] = user.id


    for vendor in VendorUser.objects.all():
        user = CustomUser.objects.create(
            username=vendor.email,
            email=vendor.email,
            first_name=vendor.firstname,
            last_name=vendor.lastname,
            phone=vendor.phone,
            national_id=vendor.national_id,
            address=vendor.address,
            user_type='vendor',
            status=vendor.status,
            date_joined=vendor.joined_at,
        )
        user.created_at = vendor.joined_at
        user.save()

        user.password = vendor.password
        user.save()

        VendorProfile.objects.create(
            user=user,
            shop_name=vendor.shop_name,
            shop_address=vendor.shop_address,
            shop_license_number=vendor.shop_license_number,
            shop_phone=vendor.shop_phone,
            rating=vendor.rating,
            is_verified=vendor.is_verified,
            created_at=vendor.joined_at,
        )

        user_id_mapping[f'vendor_{vendor.id}'] = user.id
