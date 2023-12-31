from odoo import fields, models

class HospitalLab(models.Model):
    _name = "hospital.lab"
    _description = "This is lab for hospital"

    name = fields.Char(string="Name" , required=True)
    user_id = fields.Many2one('res.users',string="Responsible")

class newLab(models.Model):
    _inherit="hospital.lab"

    age_of_lab=fields.Integer(string="Age of Lab")