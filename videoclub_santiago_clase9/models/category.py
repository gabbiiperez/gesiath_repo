from odoo import models, fields # type: ignore


class Category(models.Model):
    _name = "category"
    _description = "A category"

    name = fields.Char(string="Name", required=True)
    movie_ids = fields.One2many("movie", "category_id", string="Movies")
   