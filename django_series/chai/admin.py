from django.contrib import admin
from .models import chaivarity,chaicertificate,chaiReview,store

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model=chaiReview
    extra=2
    
class ChaivarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines = [ChaiReviewInline]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=('name','location')
    filter_horizontal=('chai_varity',)
    
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display=('chai','certificate_number')
    
admin.site.register(chaivarity,ChaivarietyAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(chaicertificate,ChaiCertificateAdmin)


