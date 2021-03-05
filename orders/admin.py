import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from .models import *



class  Ordered_itemInline(admin.TabularInline):
    model = Ordered_item
    raw_id_fields = ['product']


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = "attachment; filename=file.csv"
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not \
    field.many_to_many and not field.one_to_many]
    # Write a first row with header information
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'


@admin.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'building', 'room_number', 'created', 'updated']
    list_filter = ['created', 'updated', 'building']
    inlines = [Ordered_itemInline]
    actions = [export_to_csv]

@admin.register(ServiceOrder)
class ServiceOrder(admin.ModelAdmin):
    list_display = ['name', 'surname','ordered_product', 'building', 'number', 'room_number', 'created', 'updated']
    list_filter = ['created', 'updated', 'building']

@admin.register(SpecialOrder)
class ServiceOrder(admin.ModelAdmin):
    list_display = ['name', 'surname','ordered_product', 'building', 'number', 'room_number', 'created', 'updated']
    list_filter = ['created', 'updated', 'building']