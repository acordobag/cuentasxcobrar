# -*- coding: utf-8 -*-
{
    'name': "Cuentas por cobrar",

    'summary': """
        """,

    'description': """

    """,

    'author': "Adrian Cordoba",
    'website': "",
    "application": True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web_tree_many2one_clickable'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/view_form_account.xml',
        'views/view_form_payment.xml',
        'views/view_form_customer_inherited.xml',
        'views/view_form_users_inherited.xml',
        'views/view_form_zone.xml',
        'views/view_form_route.xml',
        'views/view_driver_routes.xml',
        'views/view_driver_route_detail.xml',
        'views/cxc_view_main.xml'
    ]
    # only loaded in demonstration mode
}
