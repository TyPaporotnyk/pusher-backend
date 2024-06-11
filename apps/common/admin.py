from django.contrib import admin

from apps.common.models import Blacklist, Category, Group, Keyword


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Blacklist)
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name", "category__name")


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "category")
    list_filter = ("category",)
    search_fields = ("name", "url", "category__name")


@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name", "category__name")
