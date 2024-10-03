from django.contrib import admin
from cars.models import Brand, Car

admin.site.index_title = "Painel de Administração"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'color', 'factory_year', 'model_year', 'created_at',)
    search_fields = ('model',)
    list_filter = ('brand',)
