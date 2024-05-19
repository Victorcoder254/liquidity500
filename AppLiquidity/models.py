from django.db import models


class Visitor(models.Model):
    ip_address = models.CharField(max_length=45)
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address


class Website(models.Model):
    retailrush = models.URLField(null=True, blank=True)
    merchant = models.URLField(null=True, blank=True)


class Services(models.Model):
    service_name_1 = models.CharField(max_length=100, null=True, blank=True)
    service_description_1 = models.TextField(null=True, blank=True)
    service_name_2 = models.CharField(max_length=100, null=True, blank=True)
    service_description_2 = models.TextField(null=True, blank=True)
    service_name_3 = models.CharField(max_length=100, null=True, blank=True)
    service_description_3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.service_name_1}, {self.service_name_2}, {self.service_name_3}"


class Liquidation_Steps(models.Model):
    step_1 = models.CharField(max_length=100, null=True, blank=True)
    image_step_1 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_1 = models.TextField(null=True, blank=True)
    step_2 = models.CharField(max_length=100, null=True, blank=True)
    image_step_2 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_2 = models.TextField(null=True, blank=True)
    step_3 = models.CharField(max_length=100, null=True, blank=True)
    image_step_3 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_3 = models.TextField(null=True, blank=True)
    step_4 = models.CharField(max_length=100, null=True, blank=True)
    image_step_4 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_4 = models.TextField(null=True, blank=True)
    step_5 = models.CharField(max_length=100, null=True, blank=True)
    image_step_5 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_5 = models.TextField(null=True, blank=True)
    step_6 = models.CharField(max_length=100, null=True, blank=True)
    image_step_6 = models.ImageField(upload_to="liquidation/", null=True, blank=True)
    desc_step_6 = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.step_1} - {self.date_created}"


class About(models.Model):
    Years_1 = models.CharField(max_length=100, null=True, blank=True)
    Headline1 = models.CharField(max_length=100, null=True, blank=True)
    about1 = models.TextField(null=True, blank=True)
    Years_2 = models.CharField(max_length=100, null=True, blank=True)
    Headline2 = models.CharField(max_length=100, null=True, blank=True)
    about2 = models.TextField(null=True, blank=True)
    Years_3 = models.CharField(max_length=100, null=True, blank=True)
    Headline3 = models.CharField(max_length=100, null=True, blank=True)
    about3 = models.TextField(null=True, blank=True)
    Years_4 = models.CharField(max_length=100, null=True, blank=True)
    Headline4 = models.CharField(max_length=100, null=True, blank=True)
    about4 = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Years_1} - {self.date_created}"


class AmazingTeam(models.Model):
    name1 = models.CharField(max_length=100, null=True, blank=True)
    role1 = models.CharField(max_length=100, null=True, blank=True)
    image1 = models.ImageField(upload_to="Team/", null=True, blank=True)
    twitter1 = models.URLField(max_length=150, null=True, blank=True)
    facebook1 = models.URLField(max_length=150, null=True, blank=True)
    linkeldin = models.URLField(max_length=150, null=True, blank=True)
    name2 = models.CharField(max_length=100, null=True, blank=True)
    role2 = models.CharField(max_length=100, null=True, blank=True)
    image2 = models.ImageField(upload_to="Team/", null=True, blank=True)
    twitter2 = models.URLField(max_length=150, null=True, blank=True)
    facebook2 = models.URLField(max_length=150, null=True, blank=True)
    linkeldin2 = models.URLField(max_length=150, null=True, blank=True)
    name3 = models.CharField(max_length=100, null=True, blank=True)
    role3 = models.CharField(max_length=100, null=True, blank=True)
    image3 = models.ImageField(upload_to="Team/", null=True, blank=True)
    twitter3 = models.URLField(max_length=150, null=True, blank=True)
    facebook3 = models.URLField(max_length=150, null=True, blank=True)
    linkeldin3 = models.URLField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name1} - {self.date_created}"


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date_created}"


class OurSocials(models.Model):
    facebook = models.URLField(max_length=150, null=True, blank=True)
    twitter = models.URLField(max_length=150, null=True, blank=True)
    linkedin = models.URLField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created}"


class PrivacyPolicy(models.Model):
    policy = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created}"


class TermsAndConditions(models.Model):
    terms = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date_created}"


class Copyright(models.Model):
    text = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.date_created}"
