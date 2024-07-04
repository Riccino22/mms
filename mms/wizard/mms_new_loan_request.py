from odoo import models, fields , api

class NewLoanReq(models.TransientModel):
    _name = 'mms.new_loan_request'
    partner_id = fields.Many2one("res.partner", string="Contact")
    movie_id = fields.Many2one("mms.movie", string="Movie")
    
    def add_to_waitlist(self):
        self.ensure_one()
        
        self.env["mms.loan_request"].create(
            {"movie_id": self.movie_id.id, "partner_id": self.partner_id.id}
        )
        return {"type": "ir.actions.act_window_close"}