from behave import fixture

from shopozor_features.utils import get_query_from_file


@fixture
def login_query(context):
    context.query = get_query_from_file('login.graphql')
    yield context.query
    del context.query
