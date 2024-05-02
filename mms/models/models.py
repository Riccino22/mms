from odoo import models, api, fields

class Movie(models.Model):
    _name = "mms.movie"  # Define the model name for movies
    _inherit = 'mail.thread'  # Inherit mail thread functionality
    _description = "Movie List"  # Description for the model
    
    name = fields.Char("Movie Name", tracking=True)  # Field for movie name with tracking enabled
    synopsis = fields.Text("Synopsis", tracking=True)  # Field for movie synopsis with tracking enabled
    actor_ids = fields.Many2many("mms.actor", string="Actors", tracking=True)  # Many-to-many relationship with actors
    genre_ids = fields.Many2many("mms.genre", string="Genre", tracking=True)  # Many-to-many relationship with genres
    contact_id = fields.Many2one("res.partner", string="Contact", tracking=True)  # Many-to-one relationship with contacts
    format_id = fields.Many2one("mms.format", string="Format", tracking=True)  # Many-to-one relationship with formats
    image = fields.Binary(string="Image", attachment=True, help="Select image here")  # Binary field for the movie image
    trailer_url = fields.Char("Trailer URL", tracking=True)  # Field for the movie trailer URL

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
  
