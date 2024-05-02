from odoo import models,api,fields

class Movie(models.Model):
    _name = "mms.movie"
    _description = "Movie List"
    
    name = fields.Char("Movie Name")
    synopsis = fields.Text("Synopsis")