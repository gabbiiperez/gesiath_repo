from odoo import models, api # type: ignore


class ProductTemplateReport(models.AbstractModel):
    _name = "report.customer_info_clase14.product_template_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        products = self.env["product.template"].search([("qty_available", ">", 0)])
        return {
            "docs": products,
        }

