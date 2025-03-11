from odoo import models, fields, api # type: ignore


class TransportShipment(models.Model):
    _name = "transport.shipment"
    _description = "A shipment"

    name = fields.Char(string="Shipment order", required=True)
    state = fields.Selection(
        [
            ("draft","Draft"),
            ("in_progress","In progress"),
            ("done","Done"),
        ],
        string="State",
        default="draft",
    )
    package_qty = fields.Integer(string="Quantity of packages")
    delivery_address = fields.Char(string="Delivery address")
    customer_id = fields.Many2one("res.partner", string="Client data")
    receipt_photo = fields.Binary(string="Photo of the receipt")
    delivered = fields.Boolean(string="Delivered")

    def write(self, vals):
        res = super().write(vals)
        if vals.get("delivered", False):
            if vals.get("delivered") == True:
                self.state="done"
        return res

    def action_in_progress(self):
        self.state = "in_progress"
        self.delivered = False
