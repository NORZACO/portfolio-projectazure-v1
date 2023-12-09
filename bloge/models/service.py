# from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class Icon(models.Model):
    icon_class = models.CharField(max_length=255)

    def __str__(self):
        return self.icon_class

    def html(self):
        return mark_safe(
            f'<span class="ico-circle"><i class="{self.icon_class}"></i></span>'
        )


class Service(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = RichTextField()

    def __str__(self):
        return self.title

    # get_icon
    def get_icon(self):
        return mark_safe(f"{self.icon.icon_class}")


class Feature(models.Model):
    feature_name = models.CharField(max_length=100)

    def __str__(self):
        return self.feature_name


# class Properties
class Properties(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    location = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100, default="123 Main Street")
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    garage = models.IntegerField()
    area = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    property_type = models.CharField(max_length=100, default="House")
    status = models.CharField(max_length=100, default="For Sale")

    agent = models.ForeignKey(
        "Agents", on_delete=models.SET_NULL, blank=True, null=True, related_name="agent"
    )

    agent = models.ForeignKey(
        "Agents",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties",
    )

    balcony = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_balcony",
    )
    outdoor_kitchen = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_outdoor_kitchen",
    )
    cable_tv = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_cable_tv",
    )
    swimming_pool = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_swimming_pool",
    )
    barbeque = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_barbeque",
    )
    laundry_room = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_laundry_room",
    )
    window_covering = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_window_covering",
    )
    gym = models.ForeignKey(
        "Feature",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="properties_with_gym",
    )

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


# Best Agents
class Agents(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    facebook = models.URLField()
    twitter = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


# Latest News
class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


# Testimonials
class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/")
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    main_image = models.ImageField(upload_to="images/", default="images/property-3.jpg")

    def __str__(self):
        return self.name

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


# About Us
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    image_tag.short_description = "Image"
    image_tag.allow_tags = True


# Contact Us
# Create your models here.
class Contact(models.Model):
    # contact_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    user_email = models.EmailField()
    descriptions = models.TextField(max_length=500)
    phonenumber = models.IntegerField()
    subject = models.CharField(max_length=100, default="")

    def __int__(self):
        return self.id
