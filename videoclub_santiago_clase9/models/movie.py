from odoo import models, fields # type: ignore


class Movie(models.Model):
    _name = "movie"
    _description = "A movie"

    name = fields.Char(string="Title", required=True)
    director = fields.Char(string="Director")
    release_date = fields.Date(string="Release date")
    duration = fields.Integer(string="Duration")
    category_id = fields.Many2one("category", string="Categories")
    actors_ids = fields.Many2many("actor", string="Actors")
    