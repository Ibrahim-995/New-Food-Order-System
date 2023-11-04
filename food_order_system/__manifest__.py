# -*- coding: utf-8 -*-
{
    'name': "Food Order System",

    'summary': """
        Serve food and take order""",

    'description': """
        Place wise food order system
    """,

    'author': "Ibrahim & Israt",
    'website': "http://www.daffodilvarsity.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Food Business',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'depends': ['website'],

    # always loaded
    'data': [
        'data/ir_sequence.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/order.xml',
        'views/formtemplate.xml',
        'views/thanks.xml',
        'views/table.xml',
        'views/qrcode.xml',
        'views/ip_link.xml',
        'reports/report.xml',
    ],
    'application': True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
