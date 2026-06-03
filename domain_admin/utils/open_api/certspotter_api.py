# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

import requests

from domain_admin.log import logger

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'


def search(domain, include_subdomains=True, max_pages=10):
    """
    查询 Cert Spotter 证书签发记录
    :param domain: str
    :param include_subdomains: bool
    :return: list
    """
    url = 'https://api.certspotter.com/v1/issuances'

    headers = {
        'User-Agent': USER_AGENT
    }

    rows = []
    after = None

    for _ in range(max_pages):
        params = {
            'domain': domain,
            'include_subdomains': 'true' if include_subdomains else 'false',
            'expand': 'dns_names',
        }

        if after:
            params['after'] = after

        try:
            req = requests.get(url=url, params=params, headers=headers, timeout=8)
        except Exception:
            logger.error('certspotter request failed: %s', domain)
            return rows

        if not req.ok:
            logger.warn('certspotter request not ok: status_code=%s', req.status_code)
            return rows

        try:
            page_rows = req.json()
        except ValueError:
            logger.warn('certspotter response is not json, status_code=%s', req.status_code)
            return rows

        if not page_rows:
            break

        rows.extend(page_rows)

        last_id = page_rows[-1].get('id')
        if not last_id or last_id == after:
            break

        after = last_id

        if len(page_rows) < 100:
            break

    return rows
