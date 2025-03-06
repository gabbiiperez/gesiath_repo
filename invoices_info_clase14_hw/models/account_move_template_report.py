from odoo import models, api # type: ignore


class AccountMoveTemplateReport(models.AbstractModel):
    _name = "report.invoices_info_clase14_hw.invoice_template_report"

    @api.model
    def _get_report_values(self, docids, data=None):
        invoices = self.env["account.move"].browse(docids).filtered(lambda inv: inv.state == "posted")
        return {
            "docs": invoices,
        }
