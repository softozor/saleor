from behave import given, when
from tests.api.utils import get_graphql_content
from behave import use_fixture

from shopozor_features.fixtures.graphql_queries import login_query


# TODO: make sure that DJANGO_SETTINGS_MODULE=shopozor.settings
@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    context.test.assertFalse(hasattr(context.test.client, 'token'))


@when(u'un client s\'identifie en tant qu\'administrateur avec un e-mail et un mot de passe valides')
def step_impl(context):
    use_fixture(login_query, context)
    variables = {'email': 'laurent.michel@softozor.ch', 'password': 'password'}
    response = context.test.client.post_graphql(context.query, variables)
    content = get_graphql_content(response)
    print("CONTENT = ", content)
    # token_data = content['data']['tokenCreate']
    # assert token_data['token']
    # assert not token_data['errors']
    #
    raise NotImplementedError(u'STEP: When un client s\'identifie en tant qu\'administrateur avec un e-mail et un mot de passe valides')
