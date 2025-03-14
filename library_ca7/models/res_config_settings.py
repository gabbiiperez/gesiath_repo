from odoo import models, fields # type: ignore


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    api_url = fields.Char(string="Api's URL", config_parameter="library_ca7.api_url")

    