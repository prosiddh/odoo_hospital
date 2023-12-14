from odoo import fields , models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Record"
    _rec_name = 'gender'

    name = fields.Char(string='Name', required = True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], string = "Gender", tracking = True)
    ref = fields.Char(string="Reference", required=True)

    def name_get(self):
        res = []
        for rec in self:
            name= f'{rec.ref} - {rec.name}'
            res.append((rec.id,name))
        return res
