TITLE: Configuring URL Patterns in Django
DESCRIPTION: This code snippet demonstrates how to set up URL patterns in Django, mapping URLs to specific view functions. It includes examples of capturing URL parameters and naming URL patterns.

LANGUAGE: python
CODE:
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

----------------------------------------

TITLE: Creating Django Poll Models
DESCRIPTION: Defines two models Question and Choice with their fields and relationships using Django's Model class. The Question model has text and date fields while Choice has text, votes and a foreign key to Question.

LANGUAGE: python
CODE:
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

----------------------------------------

TITLE: Defining a Basic Django Model
DESCRIPTION: Example of defining a simple Person model with first_name and last_name fields.

LANGUAGE: python
CODE:
from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

----------------------------------------

TITLE: Creating Basic Django View
DESCRIPTION: Implementation of a simple Django view function that returns an HTTP response.

LANGUAGE: python
CODE:
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

----------------------------------------

TITLE: Subclassing Forms in Django
DESCRIPTION: Shows how to create subclasses of forms to inherit and extend fields from parent forms.

LANGUAGE: pycon
CODE:
>>> class ContactFormWithPriority(ContactForm):
...     priority = forms.CharField()
...
>>> f = ContactFormWithPriority(auto_id=False)
>>> print(f)
<div>Subject:<input type="text" name="subject" maxlength="100" required></div>
<div>Message:<textarea name="message" cols="40" rows="10" required></textarea></div>
<div>Sender:<input type="email" name="sender" required></div>
<div>Cc myself:<input type="checkbox" name="cc_myself"></div>
<div>Priority:<input type="text" name="priority" required></div>

----------------------------------------

TITLE: Defining Django Models in Python
DESCRIPTION: Demonstrates how to create database models using Django's ORM. It defines Reporter and Article models with various field types and relationships.

LANGUAGE: python
CODE:
from django.db import models


class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

----------------------------------------

TITLE: Secure Email Sending with Form Validation in Django
DESCRIPTION: This code snippet shows the correct approach to sending an email in Django, using a form to validate and sanitize user input before use.

LANGUAGE: python
CODE:
from django import forms
from django.core.mail import send_mail
from django.http import JsonResponse


class EmailForm(forms.Form):
    email = forms.EmailField()


def my_proof_of_concept(request):
    form = EmailForm(request.GET)
    if form.is_valid():
        send_mail(
            "Email subject",
            "Email body",
            form.cleaned_data["email"],
            ["admin@example.com"],
        )
        return JsonResponse(status=200)
    return JsonResponse(form.errors, status=400)

----------------------------------------

TITLE: Writing a Django View Function
DESCRIPTION: Demonstrates how to write a view function in Django, which retrieves data from the database and renders it using a template.

LANGUAGE: python
CODE:
from django.shortcuts import render

from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {"year": year, "article_list": a_list}
    return render(request, "news/year_archive.html", context)

----------------------------------------

TITLE: Applying CSRF Protection to a Django View Function
DESCRIPTION: Shows how to use the csrf_protect decorator to add CSRF protection to a specific view function. This ensures CSRF validation even if the middleware is not active.

LANGUAGE: python
CODE:
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)

----------------------------------------

TITLE: Loading Django Secret Key from File
DESCRIPTION: Shows how to load Django's SECRET_KEY from a separate file for improved security.

LANGUAGE: python
CODE:
with open("/etc/secret_key.txt") as f:
    SECRET_KEY = f.read().strip()

----------------------------------------

TITLE: Defining Basic Django Views in Python
DESCRIPTION: This snippet shows how to create simple view functions in Django that return HTTP responses. It includes views for displaying question details, results, and handling votes.

LANGUAGE: python
CODE:
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

----------------------------------------

TITLE: Django Password Reset Form Implementation
DESCRIPTION: Reference to PasswordResetForm class that previously exposed user email enumeration vulnerability through unhandled email sending failures.

LANGUAGE: python
CODE:
django.contrib.auth.forms.PasswordResetForm

----------------------------------------

TITLE: Overriding the save() Method
DESCRIPTION: Example of overriding the save() method in a model to add custom behavior.

LANGUAGE: python
CODE:
from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, **kwargs):
        do_something()
        super().save(**kwargs)  # Call the "real" save() method.
        do_something_else()

----------------------------------------

TITLE: Defining a Simple Django Form Class
DESCRIPTION: Creates a basic Django Form class with a single CharField for capturing a user's name.

LANGUAGE: python
CODE:
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

----------------------------------------

TITLE: Processing a Form in a Django View
DESCRIPTION: Demonstrates how to handle form submission, validation, and processing in a Django view function.

LANGUAGE: python
CODE:
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            # Process the data
            return HttpResponseRedirect("/thanks/")
    else:
        form = NameForm()
    return render(request, "name.html", {"form": form})

----------------------------------------

TITLE: Creating Django User Object
DESCRIPTION: Example showing how to create a new Django user programmatically using the create_user helper function.

LANGUAGE: python
CODE:
from django.contrib.auth.models import User
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
user.last_name = "Lennon"
user.save()

----------------------------------------

TITLE: Defining a Model with Enumeration Choices
DESCRIPTION: Example of defining a Runner model with a medal field using enumeration choices.

LANGUAGE: python
CODE:
from django.db import models


class Runner(models.Model):
    MedalType = models.TextChoices("MedalType", "GOLD SILVER BRONZE")
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType, max_length=10)

----------------------------------------

TITLE: Bulk Create for Custom ManyToMany Relationships in Django
DESCRIPTION: Demonstrates using bulk_create() to efficiently insert multiple relationships for a custom ManyToMany through model.

LANGUAGE: python
CODE:
PizzaToppingRelationship = Pizza.toppings.through
PizzaToppingRelationship.objects.bulk_create([
    PizzaToppingRelationship(pizza=my_pizza, topping=pepperoni),
    PizzaToppingRelationship(pizza=your_pizza, topping=pepperoni),
    PizzaToppingRelationship(pizza=your_pizza, topping=mushroom),
], ignore_conflicts=True)

----------------------------------------

TITLE: Implementing a Custom Authentication Backend in Django
DESCRIPTION: This code snippet demonstrates how to create a custom authentication backend that authenticates against settings-defined credentials and creates a superuser on first login.

LANGUAGE: Python
CODE:
from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

class SettingsBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        login_valid = settings.ADMIN_LOGIN == username
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

----------------------------------------

TITLE: Creating a Custom User Model in Django
DESCRIPTION: This code snippet shows how to create a custom User model that uses an email address as the username and includes a required date of birth field.

LANGUAGE: Python
CODE:
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

----------------------------------------

TITLE: Demonstrating XSS Vulnerability in Django Templates
DESCRIPTION: Shows how unsanitized template variables can lead to XSS vulnerabilities when used in style tags without proper quoting. The example demonstrates a case where the template system's automatic escaping may not provide complete protection.

LANGUAGE: text
CODE:
<style class={{ var }}>...</style>

----------------------------------------

TITLE: Retrieving Objects with Django QuerySets
DESCRIPTION: Shows various ways to retrieve objects from the database using QuerySets, including filtering and chaining filters.

LANGUAGE: python
CODE:
>>> Entry.objects.all()
>>> Entry.objects.filter(pub_date__year=2006)
>>> Entry.objects.filter(headline__startswith="What").exclude(
...     pub_date__gte=datetime.date.today()
... ).filter(pub_date__gte=datetime.date(2005, 1, 30))

----------------------------------------

TITLE: Security Fix for ModelBackend.authenticate()
DESCRIPTION: Addresses CVE-2024-39329 involving timing attack vulnerability in authentication that could allow username enumeration for users with unusable passwords.



----------------------------------------

TITLE: Defining a Basic Contact Form in Django
DESCRIPTION: This snippet shows how to create a simple contact form using Django's forms module. It defines a ContactForm class with name and message fields, and includes a method for sending emails.

LANGUAGE: python
CODE:
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass

----------------------------------------

TITLE: Bulk Creation of Entries in Django
DESCRIPTION: Shows how to use bulk_create() method to efficiently create multiple Entry objects with a single database query.

LANGUAGE: python
CODE:
Entry.objects.bulk_create([
    Entry(headline="This is a test"),
    Entry(headline="This is only a test"),
])

----------------------------------------

TITLE: Defining Django Model Classes for a Blog Application
DESCRIPTION: Example model definitions for Blog, Author, and Entry classes, demonstrating relationships and field types.

LANGUAGE: python
CODE:
from datetime import date

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

----------------------------------------

TITLE: Creating Tests for QuestionIndexView in Django
DESCRIPTION: This code snippet defines a test class for the QuestionIndexView. It includes tests for various scenarios such as no questions, past questions, future questions, and multiple questions.

LANGUAGE: Python
CODE:
def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )

----------------------------------------

TITLE: Including CSRF Token in HTML Form (Django Template)
DESCRIPTION: Demonstrates how to include the CSRF token in a POST form for internal URLs using Django's template tag.

LANGUAGE: html
CODE:
<form method="post">{% csrf_token %}

----------------------------------------

TITLE: Creating a Django View with Database Query
DESCRIPTION: This snippet shows how to create a Django view that queries the database and returns the results. It retrieves the latest 5 questions and renders them in a template.

LANGUAGE: python
CODE:
from django.shortcuts import render

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

----------------------------------------

TITLE: Fixing Regular Expression DoS in Django's Truncator.words() Method
DESCRIPTION: A security fix addressing CVE-2024-27351, which resolves a potential regular expression denial-of-service vulnerability in django.utils.text.Truncator.words() method and the truncatewords_html template filter when used with html=True.

LANGUAGE: python
CODE:
django.utils.text.Truncator.words()

----------------------------------------

TITLE: Implementing Asynchronous Class-Based View in Django
DESCRIPTION: Demonstrates how to create an asynchronous class-based view using async def. This example shows an AsyncView that waits for 1 second before returning a response.

LANGUAGE: python
CODE:
import asyncio
from django.http import HttpResponse
from django.views import View


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")

----------------------------------------

TITLE: Defining Models with Relationships
DESCRIPTION: Example of defining Musician and Album models with a foreign key relationship.

LANGUAGE: python
CODE:
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

----------------------------------------

TITLE: Transaction Error Handling in Django
DESCRIPTION: Shows proper error handling pattern with nested atomic blocks for database integrity errors.

LANGUAGE: Python
CODE:
from django.db import IntegrityError, transaction

@transaction.atomic
def viewfunc(request):
    create_parent()

    try:
        with transaction.atomic():
            generate_relationships()
    except IntegrityError:
        handle_exception()

    add_children()

----------------------------------------

TITLE: Defining Multiple Databases in Django Settings
DESCRIPTION: Example of configuring multiple databases in Django's settings.py file, including a default PostgreSQL database and a MySQL database.

LANGUAGE: python
CODE:
DATABASES = {
    "default": {
        "NAME": "app_data",
        "ENGINE": "django.db.backends.postgresql",
        "USER": "postgres_user",
        "PASSWORD": "s3krit",
    },
    "users": {
        "NAME": "user_data",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "priv4te",
    },
}

----------------------------------------

TITLE: Implementing Generic Views in Django
DESCRIPTION: Implementation of generic ListView and DetailView classes for polls application, including custom template names and context object handling.

LANGUAGE: python
CODE:
from django.views import generic

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

----------------------------------------

TITLE: Defining ExclusionConstraint with Expressions in Django
DESCRIPTION: Example of creating an ExclusionConstraint with expressions using RangeOperators. This constraint is typically used to prevent overlapping ranges or values in a database.

LANGUAGE: python
CODE:
expressions = [
    ("timespan", RangeOperators.ADJACENT_TO),
    (F("room"), RangeOperators.EQUAL),
]

----------------------------------------

TITLE: Using sensitive_variables Decorator in Django Views
DESCRIPTION: Demonstration of using the sensitive_variables decorator to prevent sensitive local variables from being included in error reports. This example hides user, password, and credit card information.

LANGUAGE: python
CODE:
from django.views.decorators.debug import sensitive_variables

@sensitive_variables("user", "pw", "cc")
def process_info(user):
    pw = user.pass_word
    cc = user.credit_card_number
    name = user.name
    ...

----------------------------------------

TITLE: Permission Check Example
DESCRIPTION: Example showing how to check user permissions

LANGUAGE: python
CODE:
if user.has_perm('app_label.permission_codename'):
    # User has permission
    pass

if user.has_module_perms('app_label'):
    # User has permission to access app module
    pass

----------------------------------------

TITLE: Creating a ForeignKey with Cross-Application Reference in Django
DESCRIPTION: Shows how to create a ForeignKey relationship that references a model in a different application using the app_label.ModelName syntax.

LANGUAGE: python
CODE:
class Car(models.Model):
    manufacturer = models.ForeignKey(
        "thirdpartyapp.Manufacturer",
        on_delete=models.CASCADE,
    )

----------------------------------------

TITLE: Security Fix - UserAttributeSimilarityValidator DoS Mitigation
DESCRIPTION: Security update addressing CVE-2021-45115 where UserAttributeSimilarityValidator had potential DoS vulnerability with artificially large password inputs. The fix implements length restrictions for comparison values.

LANGUAGE: python
CODE:
UserAttributeSimilarityValidator

----------------------------------------

TITLE: Advanced Querying and Filtering in Django ORM
DESCRIPTION: This snippet demonstrates advanced querying techniques using the Django ORM, including filtering across relationships and using complex lookups.

LANGUAGE: pycon
CODE:
>>> r.article_set.filter(headline__startswith="This")
<QuerySet [<Article: This is a test>]>

>>> Article.objects.filter(reporter__first_name="John")
<QuerySet [<Article: John's second story>, <Article: This is a test>]>

>>> Article.objects.filter(reporter__first_name="John", reporter__last_name="Smith")
<QuerySet [<Article: John's second story>, <Article: This is a test>]>

>>> Article.objects.filter(reporter__in=[1, 2]).distinct()
<QuerySet [<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]>

>>> Reporter.objects.filter(article__headline__startswith="This").distinct()
<QuerySet [<Reporter: John Smith>]>

----------------------------------------

TITLE: User Model Example
DESCRIPTION: Example showing User model basic attributes and usage

LANGUAGE: python
CODE:
from django.contrib.auth.models import User

user = User.objects.create_user(
    username='john',
    email='john@example.com',
    password='secret'
)

user.first_name = 'John'
user.last_name = 'Doe'
user.save()

----------------------------------------

TITLE: Creating a More Complex Django Form
DESCRIPTION: Defines a more comprehensive Django Form class with multiple field types for a contact form.

LANGUAGE: python
CODE:
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

----------------------------------------

TITLE: Installing Django with pip in Python
DESCRIPTION: This command installs the latest version of Django using pip, the Python package installer. It should be run in an activated virtual environment for best practices.

LANGUAGE: bash
CODE:
$ python -m pip install Django