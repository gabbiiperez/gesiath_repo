from odoo import models # type: ignore


class ProductTemplateCron(models.Model):
    _inherit = "product.template"

    def deactivate_products_in_zero(self):
        products_zero = self.env["product.template"].search([
            ("qty_available", "=", 0),
            ("active", "=", True),
        ])
        products_zero.write({"active": False})

