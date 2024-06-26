from django.contrib.auth.admin import UserAdmin, admin

from .models import User, NurseInfo, CustomerInfo
from rest_framework.authtoken.models import Token

admin.site.register(Token)

admin.site.register(NurseInfo)
admin.site.register(CustomerInfo)


@admin.register(User)
class UserAdminCustom(UserAdmin):
    readonly_fields = ('jwt_token', 'token')
    list_display = ['username', 'first_name', 'last_name', 'role']
    list_filter = ['role',]
    fieldsets = UserAdmin.fieldsets + (
        ('Информация', {'fields': (
            'jwt_token','token', 'role', 'telegram_username', 'chat_telegram_id' ,'linked_card', 'card_mask', 'card_type')}),
    )

    