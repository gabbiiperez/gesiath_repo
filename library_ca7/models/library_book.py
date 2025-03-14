from odoo import models, fields


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "A book from the library"

    name = fields.Char(string="Title", required=True)
    author = fields.Char(string="Author")
    publication_date = fields.Date(string="Publication date")
    pages = fields.Integer(string="Number of pages")
    category = fields.Selection(
        [
            ("fiction","Fiction"),
            ("history","History"),
            ("science","Science"),
        ],
        string="Category",
        default="",
    )
    