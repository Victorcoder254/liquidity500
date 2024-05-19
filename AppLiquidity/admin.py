from django.contrib import admin
from .models import *


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ["ip_address", "visit_date"]


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ["retailrush", "merchant"]


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ["service_name_1", "service_name_2", "service_name_3"]


@admin.register(Liquidation_Steps)
class LiquidationStepsAdmin(admin.ModelAdmin):
    list_display = ["step_1", "step_2", "step_3", "step_4", "step_5", "step_6"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["Years_1", "Years_2", "Years_3", "Years_4"]


@admin.register(AmazingTeam)
class AmazingTeamAdmin(admin.ModelAdmin):
    list_display = ["name1", "name2", "name3"]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "date_created"]


@admin.register(OurSocials)
class OurSocialsAdmin(admin.ModelAdmin):
    list_display = ["facebook", "twitter", "linkedin"]


@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ["date_created"]


@admin.register(TermsAndConditions)
class TermsAndConditionsAdmin(admin.ModelAdmin):
    list_display = ["date_created"]


@admin.register(Copyright)
class CopyrightAdmin(admin.ModelAdmin):
    list_display = ["date_created"]
