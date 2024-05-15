from odoo import models, fields, api

class LendMovie(models.TransientModel):
    _name = "mms.lend.wizard"
    _description = "Lend Movie Wizard"
    
    name = fields.Char("name")
    movie_id = fields.Many2one("mms.movie", string="Movie")
    partner_id = fields.Many2one("res.partner", string="Contact")
    agree_return_date = fields.Datetime(string="Agree return date")
    effective_return_date = fields.Datetime(string="Effective return date")
    status = fields.Selection([
        ( "loaned" , "Loaned" ),
        ( "returned" , "Returned" ),
        ( "lost" , "Lost" ),
    ])