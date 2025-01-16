from odoo import models, fields


class Movie(models.Model):
    _name = "movie"
    _description = "A movie"

    name = fields.Char(string="Title", required=True)
    director = fields.Char(string="Director")
    release_date = fields.Date(string="Release date")
    duration = fields.Integer(string="Duration")
    gender = fields.Selection(
        [
            ("action","Action"),
            ("comedy","Comedy"),
            ("drama","Drama"),
            ("scifi","Sci-Fi"),
            ("spaceopera","Space Opera"),
        ],
        string="Gender",
        default="",
    )
    