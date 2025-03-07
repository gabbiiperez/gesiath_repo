from odoo import models, fields # type: ignore


class Course(models.Model):
    _inherit = "course"

    date_start = fields.Date(string="Start date", required=True)