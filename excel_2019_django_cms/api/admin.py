from django.contrib import admin
from .models import Event, Contact, Competition, CompetitionContactInfo


class CompetitionContactInfoInline(admin.StackedInline):
    model = CompetitionContactInfo
    max_num = 20
    extra = 1
    exclude = ('created_at', 'contributor')
    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class EventAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    exclude = ('contributor', )
    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)

class CompetitionContactInfoAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class CompetitionAdmin(admin.ModelAdmin):
    inlines = (CompetitionContactInfoInline,)
    exclude = ('contributor', )

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class ContactAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Competition, CompetitionAdmin)
#admin.site.register(CompetitionContactInfo, CompetitionContactInfoAdmin)
