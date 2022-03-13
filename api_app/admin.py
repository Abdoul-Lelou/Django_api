from .models import User,ArchiveUser,ArchiveCour,Cour

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):


  fieldsets = (
      (None, {'fields': ('email', 'password', )}),
      (('Personal info'), {'fields': ('first_name', 'last_name')}),
      (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions','role')}),
      (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('user_info'), {'fields': ('first_name','last_name', 'tel')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'first_name', 'last_name', 'is_staff', "role", "tel"]
  search_fields = ('email', 'first_name', 'last_name')
  ordering = ('email', )

admin.site.register(User)
admin.site.register(ArchiveUser)
admin.site.register(ArchiveCour)
admin.site.register(Cour)


