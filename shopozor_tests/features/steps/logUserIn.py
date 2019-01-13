from behave import given


@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    test_case = context.test_case()
    test_case.assertFalse(hasattr(context.client, 'token'))
