from django.contrib import admin

from .models import Product, Address, Company, Category


# Example
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'company', 'price']
    list_display_links = ['id', 'name']
    list_filter = ['category', 'company']
    sortable_by = ['price']


class CategoryProductInline(admin.StackedInline):
    model = Product
    extra = 0


class CompanyProductInline(admin.TabularInline):
    model = Product
    extra = 0


# Add the rest of admin models here
@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['postal_address', 'city']
    list_filter = ['city']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    inlines = [CompanyProductInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryProductInline]
