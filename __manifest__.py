{
    'name': 'Areas in Country',
    'version': '1.0',
    'category': 'Localisation',
    'description': 'Manage areas, provinces, districts, and wards in Vietnam.',
    'author': 'Your Name',
    'depends': ['base', 'web', 'website_blog'],
    'data': [
        'security/areas_security.xml',
       # 'security/security.xml',
        'security/ir.model.access.csv',
        'views/areas_views.xml',
        'views/areas_template.xml',
        # 'views/assets.xml',
        # 'controllers/controllers.py',
        #'security/areas_record_rules.xml',
    ],
    'installable': True,
    'application': True,
    'icon': '/areas_in_country/static/description/icon.png',
    'assets': {
       'web.assets_backend': [
        # 'areas_in_country/static/src/js/*.js',
    ],
    'web.assets_frontend': [
        # 'areas_in_country/static/src/xml/*.xml',
    ],
    },
}

# Thông tin trên top của blog, nút public, cmt code