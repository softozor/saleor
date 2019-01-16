from behave import fixture

from shopozor_features.utils import get_query_from_file


@fixture
def graphql_query(context, queryfile):
    context.query = get_query_from_file(queryfile)
    yield context.query
    del context.query
