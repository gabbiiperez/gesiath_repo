from odoo import models, fields # type: ignore


class Actor(models.Model):
    _name = "actor"
    _description = "An actor"

    name = fields.Char(string="Full name", required=True)
    movie_ids = fields.Many2many("movie", string="Movies")
   