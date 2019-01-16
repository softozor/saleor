from behave import fixture

from saleor.account.models import User


@fixture
def customer(context):
    password = 'H7V6WfOgnkDf68BAR4MN'
    customer = User.objects.create(email='customer@shopozor.ch')
    customer.set_password(password)
    customer.save()
    context.customer = {
        'email': customer.email,
        'password': password
    }
    yield context.customer
    del context.customer
