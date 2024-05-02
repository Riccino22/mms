from odoo import models,api,fields

class Movie(models.Model):
    _name = "mms.movie"    
    _inherit = 'mail.thread'
    _description = "Movie List"
    
    name = fields.Char("Movie Name", tracking=True)
    synopsis = fields.Text("Synopsis", tracking=True)
    actor_ids = fields.Many2many("mms.actor",string="Actors", tracking=True)
    genre_ids = fields.Many2many("mms.genre",string="Genre", tracking=True)
    contact_id = fields.Many2one("res.partner",string="Contact", tracking=True)
    #message_ids = fields.One2many('mail.message', 'res_id', domain=[('model', '=', 'mms.movie')], string='Messages')

class Actor(models.Model):
    _name = "mms.actor"
    _description = "Cast"
    
    name = fields.Char("Actor name")
    movie_id = fields.Many2one("mms.movie",string="Movie")
    

class Genre(models.Model):
    _name = "mms.genre"
    _description = "Movie genre"
    
    name = fields.Char("Genre")
    movie_id = fields.Many2one("mms.movie",string="Movie")
