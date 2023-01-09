from django.contrib import admin
from django.contrib.auth.models import User
# 我们看到的这个用户选项就是官方默认通过UserAdmin这个类注册到后台的，那么我们也引入进来，后边继承这个类
from django.contrib.auth.admin import UserAdmin
# 再引入我们定义的模型
from .models import UserProfile

# 必须先通过unregister将User取消注册
admin.site.unregister(User)


# 定义关联对象样式 横行
class UserProfileInline(admin.StackedInline):
    model = UserProfile


# 关联对象 UserProfile
class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]


# 注册user模型
admin.site.register(User, UserProfileAdmin)
