from odoo import models, fields # type: ignore


class ResPartner(models.Model):
    _inherit = "res.partner"

    age = fields.Integer(string="Age", required = True)
    gender = fields.Selection(
        [
            ("female","Female"),
            ("male","Male"),
            ("nonbinary","Non binary"),
            ("nochoiche","I prefer no to say"),
        ],
        string="Gender",
        default="",
    )
