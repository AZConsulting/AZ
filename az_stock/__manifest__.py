# -*- coding: utf-8 -*-
{
    'name': "AZ Stock",
    'summary': """Module For BRC Stock""",
    'author': "AZIT Consultants",
    'company': 'AZIT Consultants',
    'website': "http://az.odoobahrain.com/",
    'category': 'AZ',
    'version': '11.0.2.0.0',
    'depends': ['stock', 'sale_stock'],
    'data': [

        'views/stock_picking_view.xml',
        'report/delivery_slip_inherit.xml'
    ],
    'installable': "True",
}
