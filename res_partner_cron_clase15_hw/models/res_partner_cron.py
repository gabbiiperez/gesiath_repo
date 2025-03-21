from odoo import models # type: ignore
from datetime import datetime
from dateutil.relativedelta import relativedelta


class ResPartnerCron(models.Model):
    _inherit = "res.partner"

    def deactivate_six_months_old_customers(self):
        six_months_ago = datetime.today() - relativedelta(months=6)
        six_months_old_customers = self.env["res.partner"].search([
            ("invoice_ids.invoice_date", "<", six_months_ago),
            ("active", "=", True)
        ])
        six_months_old_customers.write({"active": False})

