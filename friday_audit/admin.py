"""
admin.py
"""

from django.contrib import admin

from friday_audit.models import AuditTag, FridayAuditInfo, FridayAuditLog

# Register your models here.

admin.site.register(AuditTag)
