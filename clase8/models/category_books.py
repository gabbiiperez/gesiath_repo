from odoo import models, fields # type: ignore


class CategoryBooks(models.Model):
    _name = "category.books"
    _decription = "Category of books"

    name = fields.Char(string="Name", required = True)
    book_ids = fields.One2many("books", "category_id", string="Books")
