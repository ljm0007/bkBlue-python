# -*- coding: utf-8 -*-
from django.conf import settings

class ConfFixture(object):
    BACKEND_TYPE = 'bk_token'
    USER_BACKEND = 'bk_token.backends.TokenBackend'
    LOGIN_REQUIRED_MIDDLEWARE = 'bk_token.middlewares.LoginRequiredMiddleware'
    USER_MODEL = 'bk_token.models.UserProxy'

    CONSOLE_LOGIN_URL = settings.BK_PAAS_HOST
    LOGIN_URL = settings.BK_PAAS_HOST + '/login/'
    LOGIN_PLAIN_URL = settings.BK_PAAS_HOST + '/login/'
    VERIFY_URL = settings.BK_PAAS_INNER_HOST + '/login/accounts/is_login/'
    USER_INFO_URL = settings.BK_PAAS_INNER_HOST + '/login/accounts/get_user/'
    HAS_PLAIN = False
    ADD_CROSS_PREFIX = False
    ADD_APP_CODE = True

    IFRAME_HEIGHT = 490
    IFRAME_WIDTH = 460

    WEIXIN_BACKEND_TYPE = 'null'
    WEIXIN_MIDDLEWARE = 'null.NullMiddleware'
    WEIXIN_BACKEND = 'null.NullBackend'
