from behave import register_type
import parse


@parse.with_pattern(r'client|administrateur')
def parse_user_type(text):
    return text


register_type(UserType=parse_user_type)


@parse.with_pattern(r'valides|invalides')
def parse_user_credentials_validity(validity):
    return validity == 'valides'


register_type(ValidityType=parse_user_credentials_validity)
