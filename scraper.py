# venv/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/2/2023 10:03 pm
# @Author  : Perye (Pengyu LI)
# @File    : scraper.py
# @Software: PyCharm
from typing import Dict
import requests
import json
from dateutil import parser

import util.currencies
from extensions import cache


@cache.memoize(timeout=3600)
def scrape_exchange_rate_hkd() -> Dict:
    data = json.loads(requests.get(
        'https://rbwm-api.hsbc.com.hk/digital-pws-tools-investments-eapi-prod-proxy/v1/investments/exchange-rate'
        '?locale=en_HK'
    ).text)['detailRates']
    return {item['ccy']: {
        'telegraphic_transfer_bank_buy': float(item['ttBuyRt']) if item['ttBuyRt'] else None,
        'telegraphic_transfer_bank_sell': float(item['ttSelRt'])if item['ttSelRt'] else None,
        'banknotes_bank_buy': float(item['bankBuyRt'])if item['bankBuyRt'] else None,
        'banknotes_bank_sell': float(item['bankSellRt'])if item['bankSellRt'] else None,
        'last_updated': parser.parse(item['lastUpdateDate']).isoformat()
    } for item in data}


def clear_cache(base_currency: str, currency: str):
    assert base_currency.upper() in util.currencies.allowed_currencies
    assert currency.upper() in util.currencies.allowed_currencies
    cache.delete_memoized(eval('scrape_exchange_rate_' + base_currency.lower()))


