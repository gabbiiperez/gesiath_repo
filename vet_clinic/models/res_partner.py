from odoo import models, fields, api # type: ignore


class ResPartner(models.Model):
    _inherit="res.partner"

    pet_ids = fields.One2many("vet.clinic.pet", "owner_id", string="Pets")
    pet_count = fields.Integer(string="Pet count", compute="_compute_count_pets")


    @api.depends("pet_ids")
    def _compute_count_pets(self):
        for record in self:
            record.pet_count = len(record.pet_ids)
