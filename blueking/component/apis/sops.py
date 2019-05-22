# -*- coding: utf-8 -*-
from ..base import ComponentAPI


class CollectionsSOPS(object):
    """Collections of SOPS APIS"""

    def __init__(self, client):
        self.client = client

        self.create_periodic_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/create_periodic_task/',
            description=u'创建周期任务'
        )
        self.create_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/create_task/',
            description=u'创建任务'
        )
        self.get_periodic_task_info = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/sops/get_periodic_task_info/',
            description=u'查询周期任务详情'
        )
        self.get_periodic_task_list = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/sops/get_periodic_task_list/',
            description=u'查询周期任务列表'
        )
        self.get_task_status = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/sops/get_task_status/',
            description=u'查询任务或节点状态'
        )
        self.get_template_info = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/sops/get_template_info/',
            description=u'查询单个模板详情'
        )
        self.get_template_list = ComponentAPI(
            client=self.client, method='GET',
            path='/api/c/compapi{bk_api_ver}/sops/get_template_list/',
            description=u'查询模板列表'
        )
        self.modify_constants_for_periodic_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/modify_constants_for_periodic_task/',
            description=u'修改周期任务的全局参数'
        )
        self.modify_cron_for_periodic_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/modify_cron_for_periodic_task/',
            description=u'修改周期任务的调度策略'
        )
        self.operate_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/operate_task/',
            description=u'操作任务'
        )
        self.query_task_count = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/query_task_count/',
            description=u'查询任务分类统计'
        )
        self.set_periodic_task_enabled = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/set_periodic_task_enabled/',
            description=u'设置周期任务是否激活'
        )
        self.start_task = ComponentAPI(
            client=self.client, method='POST',
            path='/api/c/compapi{bk_api_ver}/sops/start_task/',
            description=u'开始任务'
        )
