# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class BlueException(Exception):

    MESSAGE = "app异常"
    ERROR_CODE = 500

    def __init__(self, message=None, error_code=None, *args):
        super(BlueException, self).__init__(*args)
        self.error_code = self.ERROR_CODE if error_code is None else error_code
        self.message = self.MESSAGE if message is None else message


class ClientBlueException(BlueException):

    MESSAGE = "客户端请求异常"
    ERROR_CODE = 40000


class ServerBlueException(BlueException):

    MESSAGE = "服务端服务异常"
    ERROR_CODE = 50000


class ResourceNotFound(ClientBlueException):

    MESSAGE = "找不到请求的资源"
    ERROR_CODE = 40400


class ParamValidationError(ClientBlueException):

    MESSAGE = "参数验证失败"
    ERROR_CODE = 40000


class ParamRequired(ClientBlueException):

    MESSAGE = "关键参数缺失"
    ERROR_CODE = 40001


class AccessForbidden(ClientBlueException):

    MESSAGE = "登陆失败"
    ERROR_CODE = 40301


class RequestForbidden(ClientBlueException):

    MESSAGE = "请求拒绝"
    ERROR_CODE = 40320


class ResourceLock(ClientBlueException):

    MESSAGE = "请求资源被锁定"
    ERROR_CODE = 40330


class MethodError(ClientBlueException):

    MESSAGE = "请求方法不支持"
    ERROR_CODE = 40501


class DatabaseError(ServerBlueException):

    MESSAGE = "数据库异常"
    ERROR_CODE = 50110


class ApiNetworkError(ServerBlueException):

    MESSAGE = "网络异常导致远程服务失效"
    ERROR_CODE = 50301


class ApiResultError(ServerBlueException):

    MESSAGE = "远程服务请求结果异常"
    ERROR_CODE = 50302


class ApiNotAcceptable(ServerBlueException):

    MESSAGE = "远程服务返回结果格式异常"
    ERROR_CODE = 50303
