from behave import given


@given(u'un utilisateur non identifié sur le Shopozor')
def step_impl(context):
    query = """
        {
            me {
                id
            }
        }
        """

    client = context.test_case()
    client.setUp()
    resp = client.query(query)
    client.assertIsNone(resp['data']['me'])
