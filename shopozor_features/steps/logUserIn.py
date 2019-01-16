from behave import given, when, then
from tests.api.utils import get_graphql_content
from behave import use_fixture
from string import Template

from shopozor_features.fixtures.graphql import graphql_query
from shopozor_features.steps.exceptions import UnknownUserTypeError
import shopozor_features.parsedArgTypes


@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    context.test.assertFalse(hasattr(context.test.client, 'token'))


@when(u'un client s\'identifie en tant qu\'administrateur avec un e-mail et un mot de passe valides')
def step_impl(context):
    use_fixture(graphql_query, context, 'login.graphql')
    variables = {'email': context.customer['email'], 'password': context.customer['password']}
    response = context.test.client.post_graphql(context.query, variables)
    content = get_graphql_content(response)
    context.response = content


@then(u'il obtient un message d\'erreur stipulant que ses identifiants sont incorrects')
def step_impl(context):
    token_data = context.response['data']['login']
    context.test.assertIsNone(token_data['token'])
    context.test.assertEqual(token_data['errors']['message'], 'Wrong credentials')


def is_staff(user_type):
    switch = {
        'client': False,
        'administrateur': True
    }

    try:
        return switch[user_type]
    except KeyError:
        raise UnknownUserTypeError(Template(u'Unknown user type $type').substitute(user_type))


@when(u'un {user_type:UserType} s\'identifie en tant que {pretended_type:UserType} avec un e-mail et un mot de passe invalides')
def step_impl(context, user_type, pretended_type):
    use_fixture(graphql_query, context, 'login.graphql')

    if user_type == 'client':
        variables = {
            'email': context.customer['email'],
            'password': context.customer['password'],
            'isStaff': is_staff(pretended_type)
        }
    elif user_type == 'administrateur':
        variables = {
            'email': context.staff['email'],
            'password': context.staff['password'],
            'isStaff': is_staff(pretended_type)
        }
    else:
        raise UnknownUserTypeError(Template(u'Unknown user type $type').substitute(user_type))

    response = context.test.client.post_graphql(context.query, variables)
    content = get_graphql_content(response)
    context.response = content
