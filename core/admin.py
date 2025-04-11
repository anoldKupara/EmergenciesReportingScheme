from django.contrib import admin
from .models import SchemeReport, Verification

@admin.register(SchemeReport)
class SchemeReportAdmin(admin.ModelAdmin):
    list_display = ('tracking_id', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('description',)

@admin.register(Verification)
class VerificationAdmin(admin.ModelAdmin):
    list_display = ('report', 'is_legitimate', 'updated_at')