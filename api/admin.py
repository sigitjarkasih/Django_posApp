from django.contrib import admin
from api.models import PosCategory, PosProducts, posSale, posSalesItems


# Register your models here.
admin.site.register(PosCategory)
admin.site.register(PosProducts)
admin.site.register(posSale)
admin.site.register(posSalesItems)
# admin.site.register(Employees)