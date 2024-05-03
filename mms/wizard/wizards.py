from odoo import models, fields, api

class LendMovie(models.TransientModel):
    _name = "mms.lend_movie"
    _description = "Lend Movie Wizard"
    
    name = fields.Char("Si")
    
    def abrir_wizard(self):
        return {
            'res_id': self.env.context.get('active_id'),
            'res_model': self.env.context.get('active_model'),
        }
