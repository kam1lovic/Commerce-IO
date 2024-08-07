from django.contrib import admin

from shops.models import Attachment


@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass
