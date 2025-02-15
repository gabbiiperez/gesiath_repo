from odoo import models, fields # type: ignore


class VetClinicAppointment(models.Model):
    _name = "vet.clinic.appointment"
    _description = "Appointment to the clinic for a pet"

    name = fields.Char(string="Name of the owner and the pet", required=True)
    pet_id = fields.Many2one("vet.clinic.pet", string="Pets")
    appointment_date = fields.Date(string="Date of the appointment", required=True)
    description = fields.Text(string="Description for the appointment")
    