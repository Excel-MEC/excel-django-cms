from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    exclude = ('contributor', )
    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
