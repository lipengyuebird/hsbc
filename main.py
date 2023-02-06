# venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 1/2/2023 6:55 pm
# @Author  : Perye (Pengyu LI)
# @File    : main.py
# @Software: PyCharm

import os

# set environment variables
os.environ['FLASK_ENV'] = 'prod'
os.environ['FLASK_APP'] = 'hsbc'


from hsbc import app
import api


if __name__ == '__main__':
    app.run(port=5001)
