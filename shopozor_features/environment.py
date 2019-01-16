from tests.api.conftest import ApiClient
from django.contrib.auth.models import AnonymousUser
from behave import use_fixture
from shopozor_features.fixtures.user_data import customer


def before_all(context):
    use_fixture(customer, context)


def django_ready(context):
    context.test.client = ApiClient(user=AnonymousUser())
    context.django = True
