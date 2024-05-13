from odoo import models, api, fields

class Movie(models.Model):
    _name = "mms.movie"  # Define the model name for movies
    _inherit = 'mail.thread'  # Inherit mail thread functionality
    _description = "Movie List"  # Description for the model
    
    name = fields.Char("Movie Name", tracking=True)  # Field for movie name with tracking enabled
    synopsis = fields.Text("Synopsis", tracking=True)  # Field for movie synopsis with tracking enabled
    actor_ids = fields.Many2many("mms.actor", string="Actors", tracking=True)  # Many-to-many relationship with actors
    genre_ids = fields.Many2many("mms.genre", string="Genre", tracking=True)  # Many-to-many relationship with genres
    partner_id = fields.Many2one("res.partner", string="Contact", tracking=True)  # Many-to-one relationship with contacts
    format_id = fields.Many2one("mms.format", string="Format", tracking=True)  # Many-to-one relationship with formats
    image = fields.Binary(string="Image", attachment=True, help="Select image here")  # Binary field for the movie image
    trailer_url = fields.Char("Trailer URL", tracking=True)  # Field for the movie trailer URL
    status = fields.Selection([
        ( "stock" , "stock" ),
        ( "lost" , "lost" ),
        ( "loaned" , "loaned" )
    ])
    #lend_id = fields.Many2one("mms.lend", string="Lend")  
    loan_request_ids = fields.One2many("mms.loan_request", "movie_id", string='Loan')
    
    def lend_movie(self):
        pass
"""
    loan_request_ids = fields.One2many("mms.loan_request", "movie_id", string='Loan', compute='_compute_loan')

    @api.depends('loan_request_ids')
    def _compute_loan(self):
        for record in self:
            record.loan_request_ids = self.env["mms.loan_request"].search([('movie_id', '=', record.name)])
"""
    
class ResPartnerInherit(models.Model):
    _inherit = "res.partner"
    
    in_blacklist = fields.Boolean("In black list", default=False)
    loan_request_ids = fields.One2many("mms.loan_request", "partner_id", string='Loan')

class Actor(models.Model):
    _name = "mms.actor"  # Define the model name for actors
    _description = "Cast"  # Description for the model
    
    name = fields.Char("Actor name")  # Field for actor name
    movie_id = fields.Many2one("mms.movie", string="Movie")  # Many-to-one relationship with movies

class Genre(models.Model):
    _name = "mms.genre"  # Define the model name for genres
    _description = "Movie genre"  # Description for the model
    
    name = fields.Char("Genre")  # Field for genre name
    movie_id = fields.Many2one("mms.movie", string="Movie")  # Many-to-one relationship with movies

class Format(models.Model):
   _name = "mms.format"  # Specify the internal identifier for the model
   _description = "Movie format"  # Provide a description for the model
   name = fields.Char("Format")  # Define a field to store the format name
   
   
class Lend(models.Model):
    _name = "mms.lend"
    _description = "Loan history"
    _inherit = 'mail.thread'  # Inherit mail thread functionality
    
    movie_id = fields.Many2one("mms.movie", string="Movie")
    partner_id = fields.Many2one("res.partner", string="Contact")
    agree_return_date = fields.Datetime(string="Agree return date")
    effective_return_date = fields.Datetime(string="Effective return date")
    status = fields.Selection([
        ( "loaned" , "Loaned" ),
        ( "returned" , "Returned" ),
        ( "lost" , "Lost" ),
    ])

    @api.depends("movie_id", "partner_id")
    def _compute_display_name(self):
        for record in self:
            record.display_name = "{movie} - {contact}".format(movie=record.movie_id.name, contact=record.partner_id.name)

class LoanRequest(models.Model):
    _name = "mms.loan_request"
    _description = "Loan request"
    
    movie_id = fields.Many2one("mms.movie", string="Movie", onchange="onchange_movie_id()")
    
    #movie_id = fields.Many2one("mms.movie", string="Movie", onchange="onchange_movie_id()")
    partner_id = fields.Many2one("res.partner", string="Contact")
    
    @api.depends("movie_id", "partner_id")
    def _compute_display_name(self):
        for record in self:
            record.display_name = "{movie} - {contact}".format(movie=record.movie_id.name, contact=record.partner_id.name)
 
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