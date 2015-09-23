from django.contrib import admin
from moderation.admin import ModerationAdmin
# Register your models here.
from issue.models import MyModel


class MyModelModerationAdmin(ModerationAdmin):
    pass


admin.site.register(MyModel, MyModelModerationAdmin)
