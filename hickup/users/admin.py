from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.contrib.flatpages.admin import FlatPageAdmin, FlatpageForm
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from tinymce.widgets import TinyMCE
from django.utils.translation import gettext_lazy as _

from hickup.users.forms import UserChangeForm, UserCreationForm
from .models import Profile

User = get_user_model()


class CustomFlatPageAdmin(FlatPageAdmin):
    """
    FlatPage Admin
    """

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == "content":
            return db_field.formfield(
                widget=TinyMCE(
                    attrs={"cols": 40, "rows": 10},
                    mce_attrs={"external_link_list_url": reverse("tinymce-linklist")},
                )
            )
        return super().formfield_for_dbfield(db_field, **kwargs)


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, CustomFlatPageAdmin)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "first_name", "last_name", "role", "is_active", "is_staff", "is_superuser"]
    list_display_links = ["username"]
    list_editable = ["first_name", "last_name", "role", "is_active", "is_staff", "is_superuser"]
    search_fields = ["first_name", "last_name"]


admin.site.register(Profile)