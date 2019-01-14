from behave import given


@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    context.test.assertFalse(hasattr(context.test.client, 'token'))
