# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2018 Global Inelegant Technology For Business (<http://git-eg.com>)

{
    'name': 'Egypt - Accounting',
    'license': 'AGPL-3',
    'author': 'GIT , Global Inelegant Technology For Business',
    'website': "https://www.git-eg.com",
    'category': 'Localization',
    'description': """
Egypt accounting chart and localization.
=======================================================

    """,
    'depends': ['base', 'account'],
    'data': [
             'data/account_data.xml',
             'data/l10n_eg_chart_data.xml',
             'data/account_chart_template_data.xml',
    ],
}
