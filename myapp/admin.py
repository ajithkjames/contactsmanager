from django.contrib import admin
from .models import Group
from .models import Members_contact
from .models import Member
from .models import contract

admin.site.register(Members_contact)
admin.site.register(Group)
admin.site.register(Member)
admin.site.register(contract)

