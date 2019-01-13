from django.shortcuts import reverse
from django.test import Client
from django.test.testcases import TestCase

from behave import fixture
import json


# TODO: use the already existing ApiClient of saleor!
class GraphQLTestCase(TestCase):
    def setUp(self):
        self._client = Client()

    def query(self, query: str, op_name: str = None, input: dict = None):
        '''
        Args:
            query (string) - GraphQL query to run
            op_name (string) - If the query is a mutation or named query, you must
                               supply the op_name.  For annon queries ("{ ... }"),
                               should be None (default).
            input (dict) - If provided, the $input variable in GraphQL will be set
                           to this value

        Returns:
            dict, response from graphql endpoint.  The response has the "data" key.
                  It will have the "error" key if any error happened.
        '''

        body = {'query': query}
        if op_name:
            body['operation_name'] = op_name
        if input:
            body['variables'] = {'input': input}
        resp = self._client.post(reverse('api'), json.dumps(body),
                                 content_type='application/json')
        jresp = json.loads(resp.content.decode())
        return jresp

    def assertResponseNoErrors(self, resp: dict, expected: dict):
        '''
        Assert that the resp (as retuened from query) has the data from
        expected
        '''
        self.assertNotIn('errors', resp, 'Response had errors')
        self.assertEqual(resp['data'], expected, 'Response has correct data')


@fixture
def django_test_case(context):
    context.test_case = GraphQLTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    del context.test_case
