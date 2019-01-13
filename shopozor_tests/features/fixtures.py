from django.test.testcases import TestCase
from django.contrib.auth.models import AnonymousUser

from tests.api.utils import get_graphql_content
from tests.api.conftest import ApiClient

from behave import fixture


class GraphQLTestCase(TestCase):
    @staticmethod
    def getContent(response):
        return get_graphql_content(response)


@fixture
def django_test_case(context):
    context.test_case = GraphQLTestCase
    context.test_case.setUpClass()
    context.client = ApiClient(user=AnonymousUser())
    yield
    context.test_case.tearDownClass()
    del context.test_case
