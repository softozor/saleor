from behave import given, when, then
from tests.api.utils import get_graphql_content
from behave import use_fixture

from shopozor_features.fixtures.graphql import graphql_query


# TODO: make sure that DJANGO_SETTINGS_MODULE=shopozor_features.settings
@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    context.test.assertFalse(hasattr(context.test.client, 'token'))


@when(u'un client s\'identifie en tant qu\'administrateur avec un e-mail et un mot de passe valides')
def step_impl(context):
    use_fixture(graphql_query, context, 'loginStaff.graphql')
    variables = {'email': context.customer['email'], 'password': context.customer['password']}
    response = context.test.client.post_graphql(context.query, variables)
    content = get_graphql_content(response)
    context.response = content


@then(u'il obtient un message d\'erreur stipulant que ses identifiants sont incorrects')
def step_impl(context):
    token_data = context.response['data']['loginStaff']
    context.test.assertIsNone(token_data['token'])
    context.test.assertEqual(token_data['errors']['message'], 'Wrong credentials')
