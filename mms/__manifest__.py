{
    'name': 'Movie Management System',
    'version': '1.0',
    'depends': ['base','mail','account'],
    'author': "Ino",
    'category': 'Test',
    'description': """
        Movie Management System
    """,
    # No es necesario cargar ningún archivo CSV de seguridad si no hay definiciones de permisos.
    'data': [
        'security/ir.model.access.csv',
        'views/mms_movie.xml',
        'views/mms_loan_request.xml',
        'views/mms_lend.xml',
        'wizard/mms_lend_wizard.xml',
        'views/mms_actor.xml',
        'views/mms_format.xml',
        'views/mms_genre.xml',
        'views/res_partner.xml',
        'views/mms_menu.xml'
        #'wizard/mms_lend_movie.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': False
}
