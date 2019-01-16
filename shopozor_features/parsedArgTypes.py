from behave import register_type
import parse


@parse.with_pattern(r'client|administrateur')
def parse_user_type(text):
    return text


register_type(UserType=parse_user_type)
