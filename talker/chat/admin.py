from django.contrib import admin
from chat.models import user_data,relation,friend,record,active,chat_data,channel

# Register your models here.

admin.site.register(user_data)
admin.site.register(relation)
admin.site.register(friend)
admin.site.register(chat_data)
admin.site.register(record)
admin.site.register(active)
admin.site.register(channel)
