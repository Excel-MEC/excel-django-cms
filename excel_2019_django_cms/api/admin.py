from django.contrib import admin
from .models import(
    Event,
    Contact,
    Competition,
    CompetitionContactInfo,
    Schedule,
    EventContactInfo,
    EventButton,
    CompetitionButton
)


class CompetitionContactInfoInline(admin.StackedInline):
    model = CompetitionContactInfo
    max_num = 20
    extra = 1
    exclude = ('created_at', 'contributor')
    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)

class CompetitionButtonInline(admin.StackedInline):
    model = CompetitionButton
    max_num = 20
    extra = 1


class EventContactInfoInline(admin.StackedInline):
    model = EventContactInfo
    max_num = 20
    extra = 1
    exclude = ('created_at', 'contributor')
    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class EventButtonInline(admin.StackedInline):
    model = EventButton
    max_num = 20
    extra = 1


class EventAdmin(admin.ModelAdmin):
    inlines = (EventContactInfoInline, EventButtonInline)
    readonly_fields = ('created_at',)
    exclude = ('contributor', )
    list_display = ('name', 'codename', 'img', 'website', 'contributor')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class CompetitionContactInfoAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class CompetitionAdmin(admin.ModelAdmin):
    inlines = (CompetitionContactInfoInline, CompetitionButtonInline)
    exclude = ('contributor', )
    list_display = ('name', 'codename', 'img', 'venue', 'date', 'time', 'category', 'active', 'contributor')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class ContactAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')
    list_display = ('name', 'email', 'phone_number', 'img', 'contributor')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class ScheduleAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')
    list_display = ('name', 'venue', 'date', 'time', 'img', 'day', 'category', 'daytime', 'contributor')
    search_fields = ('name',)

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


class EventContactInfoAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'contributor')

    def save_model(self, request, obj, form, change):
        obj.contributor = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Event, EventAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Competition, CompetitionAdmin)
#admin.site.register(CompetitionContactInfo, CompetitionContactInfoAdmin)
#admin.site.register(EventContactInfo, EventContactInfoAdmin)
admin.site.register(Schedule, ScheduleAdmin)
