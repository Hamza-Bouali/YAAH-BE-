from django.contrib import admin
from .models import User, Appointment

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'city', 'phone', 'assurance', 'num_assurance')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('city', 'assurance')

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'type', 'comments')
    search_fields = ('user__email', 'date', 'type')
    list_filter = ('date', 'type')

# Enregistrer les modèles dans l'interface d'administration avec personnalisation
admin.site.register(User, UserAdmin)
admin.site.register(Appointment, AppointmentAdmin)
