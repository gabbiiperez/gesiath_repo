from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = "library.author"
    _description = "An author from a book"

    name = fields.Char(string="Title", required=True)
   