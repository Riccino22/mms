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
    @api.model
    def default_get(self, fields):                         
        res = super(LendMovie, self).default_get(fields)  
        return res                                         
    

    def record_lend(self):                      
        self.ensure_one()                                  
        
        self.env['mms.lend'].create({                      
            'movie_id': self.movie_id.id,
            'partner_id': self.partner_id.id
        })
        return {'type': 'ir.actions.act_window_close'}
