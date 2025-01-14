from odoo import models, fields


class Librarylibraries(models.Model):
    _name = "library.libraries"
    _description = "Libraries on town"

    name = fields.Char(string="Name", required=True)
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone", size=69)
   