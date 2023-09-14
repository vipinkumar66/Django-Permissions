from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http.request import HttpRequest
from .models import Category, Product
from django.contrib.auth.models import User, Group

admin.site.unregister(Group)
admin.site.unregister(User)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom user class so that we can control what they can see or not
    from start
    """
    def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        user = request.user.is_superuser
        return not user

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
        user = request.user.is_superuser
        return  user

#  class ReadOnlyAdminMixin:

#     def has_add_permission(self, request):
#         return False

#     def has_view_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
#         if request.user.has_perm('core.change_product'):
#             return False
#         if request.user.groups.acontains("staff"):
#             return True

#     def has_delete_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
#         return False

#     def has_change_permission(self, request: HttpRequest, obj: Any | None = ...) -> bool:
#         return False

# class ProductInline(admin.StackedInline):  # You can use StackedInline or TabularInline depending on your preference
#     model = Product
#     extra = 0  # This controls the number of empty forms to display

# @admin.register(Product)
# class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
#     list_display = ('name',)

#     def get_form(self, request, obj, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         is_staff = request.user.is_staff
#         if not is_staff:
#             form.base_fields["name"].disabled = True
#         return form


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     # list_display = ('name', 'quantity')
#     inlines = [ProductInline,]
#     # Remove the inlines setting for Product
