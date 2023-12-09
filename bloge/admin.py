from django.contrib import admin
from django.utils.html import format_html
from bloge.models.service import (
    Service,
    Icon,
    Properties,
    Agents,
    About,
    Testimonials,
    News,
    Feature,
)  # noqa: F401, F403


class AboutAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "date",
    )

class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "description")


class IconAdmin(admin.ModelAdmin):
    list_display = ("icon_class",)


class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "client", "project_date")
    search_fields = ("title", "category", "client")


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "image")
    search_fields = ("name", "description")


class FeatureAdmin(admin.ModelAdmin):
    list_display = ("feature_name",)
    search_fields = ("feature_name",)


class PropertiesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "price",
        "location",
        "street_address",
        "bedroom",
        "bathroom",
        "garage",
        "area",
        "date",
        "agent",
        "image_tag",
    )
    search_fields = ("title", "description", "location")
    readonly_fields = ("image_tag",)

    def image_tag(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))
    



admin.site.register(About, AboutAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Icon, IconAdmin)
admin.site.register(Properties)
admin.site.register(Agents)
# admin.site.register(About, AboutAdmin)
admin.site.register(News)
admin.site.register(Testimonials, TestimonialAdmin)
admin.site.register(Feature)
