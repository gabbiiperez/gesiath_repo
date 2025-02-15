from odoo import models, fields, api # type: ignore
from odoo.exceptions import ValidationError # type: ignore


class VetClinicPet(models.Model):
    _name = "vet.clinic.pet"
    _description = "A pet in the clinic"

    name = fields.Char(string="Name", required=True)
    owner_id = fields.Many2one("res.partner", string="Owners")
    age = fields.Integer(string="Age in whole years")
    species = fields.Selection(
        [
            ("dog","Dog"),
            ("cat","Cat"),
            ("bird","Bird"),
            ("lizard","Lizard"),
            ("other","Other"),
        ],
        string="Species",
        default="",
    )
    age_category = fields.Char(string="Age category", compute="_compute_age_category")

    @api.constrains("age")
    def _check_minimum_age(self):
        for record in self:
            if record.age <= 0:
                raise ValidationError("The minimum age for a pet is 0.")
            
    @api.depends("age")
    def _compute_age_category(self):
        for record in self:
            if record.age < 2:
                record.age_category = "Puppy"
            elif 2 <= record.age <= 8:
                record.age_category = "Adult"
            else:
                record.age_category = "Senior"
                