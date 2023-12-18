from odoo import fields , models, api, _

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Record"
    _rec_name = 'name'

    # ref = fields.Char(string="Reference", required=True)
    ref = fields.Char(string="Dr. ID",readonly=True,index=True, copy=False,default=lambda self: _('New'))

    name = fields.Char(string='Name', required = True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female'),('others','Others')], string = "Gender", tracking = True)
    doc_degree = fields.Selection([('mbbs','MBBS'),('bhms','BHMS'),('others','OTHERS')], string="Degree", tracking=True)
    doc_blood_group = fields.Selection([('a+','A+'),('a-','A-'),('b+','B+'),('b-','B-'),('ab+','AB+'),('ab-','AB-'),('o+','O+'),('o-','O-')], string="Blood Group", tracking=True)
    image=fields.Image(string="Image")
    specialist=fields.Char(string="Specialist")


    @api.model
    def create(self, vals_list):
        if vals_list.get('ref', 'New') == 'New':
            vals_list['ref'] = self.env['ir.sequence'].next_by_code('hospital.doctor.sequence') or 'New'
            result = super(HospitalDoctor, self).create(vals_list)
            return result


    def name_get(self):
        res = []
        for rec in self:
            name= f'{rec.ref} - {rec.name}'
            res.append((rec.id,name))
        return res
