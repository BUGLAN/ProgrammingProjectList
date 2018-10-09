#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    text-operation.diary
    --------------------

    访客留言簿/日志——允许人们添加评论或者日记，可以设置开启/关闭评论，
    并且可以记录下每一条目的时间。也可以做成喊话器。
    :copyright: (c) 2018-10-07 by buglan
"""
from flask import Flask
from config import config

app = Flask(__name__)


def create_app(config=config['base']):
    app.config.from_object(config)
    return app
