# -*- coding:utf-8 -*-
__version__ = '1.0.0.0'
"""
@brief  :   简介
@details:   详细信息
@author :   zhphuang
@date   :   2020-03-04
"""

from django import template

register = template.Library()


@register.filter(name='format_none')  # 过滤器在模板中使用时的name
def format_none(value):  # 把传递过来的参数arg替换为'~'
    if not value:
        return ''
    return value
