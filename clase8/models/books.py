from odoo import models, fields # type: ignore


class Books(models.Model):
    _name = "books"
    _description = "A Book"

    name = fields.Char(string="Name", required = True)
    author = fields.Char(string="Author")
    price = fields.Float(string="Price")
    category_id = fields.Many2one("category.books", string="Category")
