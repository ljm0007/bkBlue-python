# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.module_loading import import_string

from blueapps.account.conf import ConfFixture, AUTH_USER_MODEL


def get_user_model():
    """
    返回平台对应版本 User Proxy Model
    """
    path = 'blueapps.account.components.{model}'.format(
        model=ConfFixture.USER_MODEL)
    return import_string(path)


if AUTH_USER_MODEL == settings.AUTH_USER_MODEL:
    from django.contrib import auth
    auth.get_user_model = get_user_model

default_app_config = 'blueapps.account.apps.AccountConfig'
