import django
from django.test.runner import DiscoverRunner
from behave import use_fixture
import os

os.environ["DJANGO_SETTINGS_MODULE"] = "shopozor.settings"


def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()


def after_all(context):
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


def before_scenario(context, scenario):
    from shopozor_tests.features.fixtures import django_test_case
    use_fixture(django_test_case, context)
