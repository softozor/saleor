from tests.api.conftest import ApiClient
from django.contrib.auth.models import AnonymousUser


def django_ready(context):
    context.test.client = ApiClient(user=AnonymousUser())
    context.django = True
