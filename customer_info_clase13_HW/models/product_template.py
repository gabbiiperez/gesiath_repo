from odoo import models, fields # type: ignore


class ProductTemplate(models.Model):
    _inherit = "product.template"

    works = fields.Char(string="Works", default="Yes")
