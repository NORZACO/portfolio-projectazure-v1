from email.mime import image  # noqa: F401
from django.test import TestCase
from .models.service import (
    Icon,
    Service,
    Properties,
    Agents,
    About,
    Testimonials,
    News,
    Feature,
    Contact,
)  # noqa: F401

# Create your tests here.
from datetime import datetime  # noqa: F401
from django.utils import timezone  # noqa: F401

# import datetime.date
from datetime import date  # noqa: F401


# IconTest
class IconTest(TestCase):
    def setUp(self):
        Icon.objects.create(icon_class="fa fa-home")

    def test_icon_class(self):
        """Icon are correctly identified"""
        icon = Icon.objects.get(icon_class="fa fa-home")
        self.assertEqual(icon.icon_class, "fa fa-home")


# ServiceTest
class ServiceTest(TestCase):
    def setUp(self):
        Service.objects.create(
            # icon foreign key from Icon class
            icon=Icon.objects.create(icon_class="fa fa-home"),
            title="Web Development",
            description="Web Development",
        )

    def test_service_title(self):
        """Service are correctly identified"""
        service = Service.objects.get(title="Web Development")
        self.assertEqual(service.title, "Web Development")

    def test_service_description(self):
        """Service are correctly identified"""
        service = Service.objects.get(description="Web Development")
        self.assertEqual(service.description, "Web Development")


# # FeatureTest
class FeatureTest(TestCase):
    def setUp(self):
        Feature.objects.create(feature_name="Web Development")

    def test_feature_name(self):
        """Feature are correctly identified"""
        feature = Feature.objects.get(feature_name="Web Development")
        self.assertEqual(feature.feature_name, "Web Development")


# PropertiesTest
class PropertiesTest(TestCase):
    def setUp(self):
        Properties.objects.create(
            title="Web Development",
            description="Web Development",
            price=100,
            # image="Web Development",
            location="Web Development",
            street_address="Web Development",
            bedroom=1,
            bathroom=1,
            garage=1,
            area=1,
            property_type="Web Development",
            status="Web Development",
        )

    def test_properties_title(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(title="Web Development")
        self.assertEqual(properties.title, "Web Development")

    def test_properties_description(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(description="Web Development")
        self.assertEqual(properties.description, "Web Development")

    def test_properties_price(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(price=100)
        self.assertEqual(properties.price, 100)

    def test_properties_location(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(location="Web Development")
        self.assertEqual(properties.location, "Web Development")

    def test_properties_street_address(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(street_address="Web Development")
        self.assertEqual(properties.street_address, "Web Development")

    def test_properties_bedroom(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(bedroom=1)
        self.assertEqual(properties.bedroom, 1)

    def test_properties_bathroom(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(bathroom=1)
        self.assertEqual(properties.bathroom, 1)

    def test_properties_garage(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(garage=1)
        self.assertEqual(properties.garage, 1)

    def test_properties_area(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(area=1)
        self.assertEqual(properties.area, 1)

    def test_properties_property_type(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(property_type="Web Development")
        self.assertEqual(properties.property_type, "Web Development")

    def test_properties_status(self):
        """Properties are correctly identified"""
        properties = Properties.objects.get(status="Web Development")
        self.assertEqual(properties.status, "Web Development")


# # AgentsTest
class AgentsTest(TestCase):
    def setUp(self):
        Agents.objects.create(
            name="Web Development",
            image="Web Development",
            phone="Web Development",
            email="Web Development",
            description="Web Development",
            facebook="Web Development",
            twitter="Web Development",
            instagram="Web Development",
        )

    def test_agents_name(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(name="Web Development")
        self.assertEqual(agents.name, "Web Development")

    def test_agents_image(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(image="Web Development")
        self.assertEqual(agents.image, "Web Development")

    def test_agents_phone(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(phone="Web Development")
        self.assertEqual(agents.phone, "Web Development")

    def test_agents_email(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(email="Web Development")
        self.assertEqual(agents.email, "Web Development")

    def test_agents_description(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(description="Web Development")
        self.assertEqual(agents.description, "Web Development")

    def test_agents_facebook(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(facebook="Web Development")
        self.assertEqual(agents.facebook, "Web Development")

    def test_agents_twitter(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(twitter="Web Development")
        self.assertEqual(agents.twitter, "Web Development")

    def test_agents_instagram(self):
        """Agents are correctly identified"""
        agents = Agents.objects.get(instagram="Web Development")
        self.assertEqual(agents.instagram, "Web Development")


test_date = datetime.strptime("2023-12-09", "%Y-%m-%d").date()


# # AboutTest
class AboutTest(TestCase):
    def setUp(self):
        About.objects.create(
            title="Web Development",
            description="Web Development",
            image="Web Development",
            date=test_date,
        )

    def test_about_title(self):
        """About are correctly identified"""
        about = About.objects.get(title="Web Development")
        self.assertEqual(about.title, "Web Development")

    def test_about_description(self):
        """About are correctly identified"""
        about = About.objects.get(description="Web Development")
        self.assertEqual(about.description, "Web Development")

    def test_about_image(self):
        """About are correctly identified"""
        about = About.objects.get(image="Web Development")
        self.assertEqual(about.image, "Web Development")

    def test_about_date(self):
        """About are correctly identified"""
        about = About.objects.get(date=test_date)
        self.assertEqual(about.date, test_date)


# # TestimonialsTest
class TestimonialsTest(TestCase):
    def setUp(self):
        Testimonials.objects.create(
            name="Web Development",
            image="Web Development",
            description="Web Development",
            date=test_date,
            main_image="Web Development",
        )
    
    def test_testimonials_name(self):
        """Testimonials are correctly identified"""
        testimonials = Testimonials.objects.get(name="Web Development")
        self.assertEqual(testimonials.name, "Web Development")


    def test_testimonials_image(self):
        """Testimonials are correctly identified"""
        testimonials = Testimonials.objects.get(image="Web Development")
        self.assertEqual(testimonials.image, "Web Development")

    
    def test_testimonials_description(self):
        """Testimonials are correctly identified"""
        testimonials = Testimonials.objects.get(description="Web Development")
        self.assertEqual(testimonials.description, "Web Development")

    
    def test_testimonials_date(self):
        """Testimonials are correctly identified"""
        testimonials = Testimonials.objects.get(date=test_date)
        self.assertEqual(testimonials.date, test_date)


    def test_testimonials_main_image(self):
        """Testimonials are correctly identified"""
        testimonials = Testimonials.objects.get(main_image="Web Development")
        self.assertEqual(testimonials.main_image, "Web Development")





# # NewsTest
class NewsTest(TestCase):
    def setUp(self):
        News.objects.create(
            title="Web Development",
            description="Web Development",
            image="Web Development",
            date=test_date,
        )

    def test_news_title(self):
        """News are correctly identified"""
        news = News.objects.get(title="Web Development")
        self.assertEqual(news.title, "Web Development")

    def test_news_description(self):
        """News are correctly identified"""
        news = News.objects.get(description="Web Development")
        self.assertEqual(news.description, "Web Development")

    def test_news_image(self):
        """News are correctly identified"""
        news = News.objects.get(image="Web Development")
        self.assertEqual(news.image, "Web Development")

    def test_news_date(self):
        """News are correctly identified"""
        news = News.objects.get(date=test_date)
        self.assertEqual(news.date, test_date)


#  ContactTest
class ContactTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="Web Development",
            user_email="Web Development",
            subject="Web Development",
            message="Web Development",
            date=test_date,
        )

    def test_contact_name(self):
        """Contact are correctly identified"""
        contact = Contact.objects.get(name="Web Development")
        self.assertEqual(contact.name, "Web Development")

    def test_contact_email(self):
        """Contact are correctly identified"""
        contact = Contact.objects.get(user_email="Web Development")
        self.assertEqual(contact.user_email, "Web Development")

    def test_contact_subject(self):
        """Contact are correctly identified"""
        contact = Contact.objects.get(subject="Web Development")
        self.assertEqual(contact.subject, "Web Development")

    def test_contact_message(self):
        """Contact are correctly identified"""
        contact = Contact.objects.get(message="Web Development")
        self.assertEqual(contact.message, "Web Development")

    def test_contact_date(self):
        """Contact are correctly identified"""
        contact = Contact.objects.get(date=test_date)
        self.assertEqual(contact.date, test_date)


# # delete all tests
# # python manage.py test bloge
# # python manage.py test bloge.tests
# # python manage.py test bloge.tests.IconTest
# # python manage.py test bloge.tests.ServiceTest
# # python manage.py test bloge.tests.FeatureTest
# # python manage.py test bloge.tests.PropertiesTest
# # python manage.py test bloge.tests.AgentsTest
# # python manage.py test bloge.tests.AboutTest
# # python manage.py test bloge.tests.TestimonialsTest
# # python manage.py test bloge.tests.NewsTest
# # python manage.py test bloge.tests.IconTest.test_icon_class
# # python manage.py test bloge.tests.ServiceTest.test_service_title
# # python manage.py test bloge.tests.ServiceTest.test_service_description
