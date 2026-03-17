from django.contrib import admin
from .models import Temple, Pooja, Booking

@admin.register(Temple)
class TempleAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_number', 'email')
    search_fields = ('name', 'location')

@admin.register(Pooja)
class PoojaAdmin(admin.ModelAdmin):
    list_display = ('pooja_name', 'temple', 'price', 'active')
    list_filter = ('temple', 'active')
    search_fields = ('pooja_name',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('devotee_name', 'pooja', 'temple', 'date', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'date', 'temple')
    search_fields = ('devotee_name', 'transaction_id')
    readonly_fields = ('created_at',)