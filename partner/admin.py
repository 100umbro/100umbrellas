from django.contrib import admin


from .models import Currency,Partner

class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ["name","date_sign_up","currency"]
    # list_display_links = ["date"]
    date_hierarchy = 'date_sign_up'
    list_per_page = 20
    list_editable = ['currency','date_sign_up']

    class Meta:
        model = Partner


admin.site.register(Partner,PartnerModelAdmin)
admin.site.register(Currency)
