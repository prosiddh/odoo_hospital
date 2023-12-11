from odoo import fields, models

class cancel_appointment(models.TransientModel):
    _name="hospital.wizard"
    _description = "This is Wizard of hospital"

    p_name=fields.Many2one('res.partner')