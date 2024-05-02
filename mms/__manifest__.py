{
    'name': 'Movie Management System',
    'version': '1.0',
    'depends': ['base'],
    'author': "Ino",
    'category': 'Test',
    'description': """
        Movie Management System
    """,
    # No es necesario cargar ningún archivo CSV de seguridad si no hay definiciones de permisos.
    'data': [
        'security/ir.model.access.csv',
        'views/mms_movie.xml',
        'views/mms_menu.xml'
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
}
