from odoo import models, api, fields


class Movie(models.Model):
    _name = "mms.movie"
    _inherit = "mail.thread"
    _description = "Movie List"

    name = fields.Char("Movie Name", tracking=True)
    synopsis = fields.Text("Synopsis", tracking=True)
    actor_ids = fields.Many2many("mms.actor", string="Actors", tracking=True)
    genre_ids = fields.Many2many("mms.genre", string="Genre", tracking=True)
    partner_id = fields.Many2one("res.partner", string="Contact", tracking=True)
    format_id = fields.Many2one("mms.format", string="Format", tracking=True)
    image = fields.Binary(string="Image", attachment=True, help="Select image here")
    trailer_url = fields.Char("Trailer URL", tracking=True)
    status = fields.Selection([("stock", "stock"), ("lost", "lost"), ("loaned", "loaned")], tracking=True)
    loan_request_ids = fields.One2many("mms.loan_request", "movie_id", string="Loan", readonly=True)

    def open_lend_wizard_action(self):
        action = self.env["ir.actions.act_window"]._for_xml_id("mms.mms_lend_wizard_action")
        print("------------------------------------------------")
        return action

class ResPartner(models.Model):
    _inherit = "res.partner"

    in_blacklist = fields.Boolean("In black list", default=False)
    loan_request_ids = fields.One2many("mms.loan_request", "partner_id", string="Loan", readonly=True)

    def add_to_blacklist(self):
        self.in_blacklist = True

class Actor(models.Model):
    _name = "mms.actor"
    _description = "Cast"

    name = fields.Char("Actor name")
    movie_id = fields.Many2one("mms.movie", string="Movie")

class Genre(models.Model):
    _name = "mms.genre"
    _description = "Movie genre"

    name = fields.Char("Genre")
    movie_id = fields.Many2one("mms.movie", string="Movie")

class Format(models.Model):
    _name = "mms.format"
    _description = "Movie format"
    name = fields.Char("Format")

class Lend(models.Model):
    _name = "mms.lend"
    _description = "Loan history"
    _inherit = "mail.thread"

    movie_id = fields.Many2one("mms.movie", string="Movie")
    partner_id = fields.Many2one("res.partner", string="Contact")
    agree_return_date = fields.Datetime(string="Agree return date")
    effective_return_date = fields.Datetime(string="Effective return date")
    status = fields.Selection([
        ("loaned", "Loaned"),
        ("returned", "Returned"),
        ("lost", "Lost"),
    ])

    @api.depends("movie_id", "partner_id")
    def _compute_display_name(self):
        for record in self:
            record.display_name = "{movie} - {contact}".format(
                movie=record.movie_id.name, contact=record.partner_id.name
            )

class LoanRequest(models.Model):
    _name = "mms.loan_request"
    _description = "Loan request"

    movie_id = fields.Many2one("mms.movie", string="Movie", onchange="onchange_movie_id()")
    partner_id = fields.Many2one("res.partner", string="Contact")

    @api.depends("movie_id", "partner_id")
    def _compute_display_name(self):
        for record in self:
            record.display_name = "{movie} - {contact}".format(
                movie=record.movie_id.name, contact=record.partner_id.name
            )


"""
    @api.onchange('movie_id')
    def onchange_movie_id(self):
        if self.movie_id:
            return {'domain': {'movie_id': [('name', '=', self.movie_id.name)]}}"""
"""
    @api.model
    def get_waiting_borrowers(self, movie_id):
        loans = self.search([('movie_id', '=', movie_id)])
        return loans.mapped('partner_id')
"""
