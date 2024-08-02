# custom_pos_customer/__manifest__.py

{
    'name': 'Custom Website',
    'version': '15.0.1.0.0',
    'category': 'website',
    'summary': 'Website Form',
    'author': 'Sabah',
    'depends': ['website'],
    'data': [
        'views/website_form_template.xml'

    ],
    'assets': {
        'web.assets_frontend':[
            'custom_website/static/src/js/website_form_validateion.js'
        ]
    },

    'auto-install': False,
    'application': True,
    'license': 'LGPL-3',

}