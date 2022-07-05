import csv
from encodings.utf_8 import encode
from django.contrib import admin
from .forms import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.http import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, encode('utf8'))

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "download"


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = (
        'first_name', 'last_name', 'username', 'phone_number', 'is_active', 'join_date',)
    actions = ["export_as_csv"]
    add_form = UserCreationForm
    change_form = UserAdminChangeForm
    # readonly_fields = ('password',)
    list_display_links = ['username', 'first_name', 'last_name']

    def get_form(self, request, obj=None, **kwargs):
        if not obj:
            self.form = self.add_form
        else:

            self.form = self.change_form
        if obj is not None:
            print(None)

        return super(AccountAdmin, self).get_form(request, obj, **kwargs)

    # The fields to be used in displaying the User model.


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    change_form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'username', 'phone_number', 'admin', 'is_active',)

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    # list_display = ('email', 'date_of_birth', 'is_admin')
    list_filter = ('is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'username', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active',)})
    )
    # # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'username', 'first_name', 'last_name')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.unregister(Group)
# admin.site.register(UserAdmin)
