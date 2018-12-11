from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from vendors.models import Vendor, VendorEmail, VendorPhoneNumber
from depots.models import Depot, DepotEmail, DepotPhoneNumber
from trackers.models import Tracker

from .forms import UserChangeForm, UserCreationForm


User = get_user_model()

model_list = [Tracker, Vendor, VendorEmail, VendorPhoneNumber, Depot, DepotEmail, DepotPhoneNumber]
for model in model_list:
    admin.site.register(model)


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]
