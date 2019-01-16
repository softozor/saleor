from behave import given, then, when
from behave import use_fixture

from shopozor_features.fixtures.graphql import graphql_query
from tests.api.utils import get_graphql_content

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
    return switch[user_type]


def user_type_to_query_variables(user_type, is_staff_user, context):
    switch = {
        'client': dict(email=context.customer['email'], password=context.customer['password'], isStaff=is_staff_user),
        'administrateur': dict(email=context.staff['email'], password=context.staff['password'], isStaff=is_staff_user)
    }
    return switch[user_type]


@when(
    u'un {user_type:UserType} s\'identifie en tant que {pretended_type:UserType} avec un e-mail et un mot de passe invalides')
def step_impl(context, user_type, pretended_type):
    use_fixture(graphql_query, context, 'login.graphql')
    variables = user_type_to_query_variables(user_type, is_staff(pretended_type), context)
    response = context.test.client.post_graphql(context.query, variables)
    content = get_graphql_content(response)
    context.response = content
