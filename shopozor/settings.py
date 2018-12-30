from saleor.settings import *

if DEBUG:
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware',
                       'django.middleware.common.CommonMiddleware']
    MIDDLEWARE = CORS_MIDDLEWARE + MIDDLEWARE
    INSTALLED_APPS.append('corsheaders')

INSTALLED_APPS.remove('saleor.graphql')
INSTALLED_APPS.append('shopozor.graphql')

ROOT_URLCONF = 'shopozor.urls'
