import django
from django.test.runner import DiscoverRunner
from behave import use_fixture
import os

from shopozor_tests.features.fixtures import django_test_case

os.environ["DJANGO_SETTINGS_MODULE"] = "shopozor.settings"


def before_all(context):
    print('before setup')
    django.setup()
    print('after setup')
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)
