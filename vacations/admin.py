from django.contrib import admin
from .models import Vacation

class VacationAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'end_date', 'reason', 'status')
    list_filter = ('status', 'user')
    search_fields = ('user__username',)

admin.site.register(Vacation, VacationAdmin)
