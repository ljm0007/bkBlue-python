# -*- coding: utf-8 -*-
from django.utils.module_loading import import_string

from blueapps.account.conf import ConfFixture


def load_backend(backend):
    path = 'blueapps.account.components.{backend}'.format(backend=backend)
    return import_string(path)


if hasattr(ConfFixture, 'USER_BACKEND'):
    UserBackend = load_backend(ConfFixture.USER_BACKEND)

if hasattr(ConfFixture, 'WEIXIN_BACKEND'):
    WeixinBackend = load_backend(ConfFixture.WEIXIN_BACKEND)
