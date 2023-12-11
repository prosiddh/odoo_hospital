from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Records"

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    is_child = fields.Boolean(string='Is Child ?', tracking=True)
    notes = fields.Text(string="Notes", tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Other')], string="Gender",
                              tracking=True)
    capitalized_name = fields.Char(string='Capitalized Name', compute='_compute_capitalized_name', store=True)
    appointment_date = fields.Date(string="Appointment Date")
    priority = fields.Selection(
        [('low', 'Low'), ('medium', 'Medium'), ('high', 'High')],
        string='Priority',
        help='Select the priority level for the model.'
    )
    ref = fields.Char(string="Reference",readonly=True, copy=False, default=lambda self: _('New'))

    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    multi_doc = fields.Many2many('hospital.doctor', string="Add. Doctor")
    description = fields.Text(string="Any Special Description ?")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('ref', _('New')) == _('New'):
                next_ref = self.env['ir.sequence'].next_by_code('hospital.patient') or _('New')
                print(f"Generated next reference: {next_ref}")
                vals['ref'] = next_ref

        print(f"Values after modification: {vals_list}")
    #         # vals['ref'] = self.env['ir.sequence'].next_by_code(self,'hospital.patient') or '/'
    #         # print(vals['ref'])
        return super(HospitalPatient, self).create(vals_list)

    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("If child then Age has to be recorded !"))

    @api.depends('name')
    def _compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''

    @api.onchange('age')
    def _onchange_age(self):
        pass
        # if self.age <= 10:
        #     self.is_child = True
        # else:
        #     self.is_child = False


    def wizard_appointment(self):
        return {
            'type':'ir.actions.act_window',
            'res_model':'hospital.wizard',
            'name':'Cancel',
            'view_mode':'form',
            'target':'new'
        }

    def redirect_button(self):
        return {
            'type':'ir.actions.act_url',
            'url':'https://www.google.com'
        }

    def show_sales(self):
        return {
            'type':'ir.actions.act_url',
            # 'url':'http://localhost:8015/web#action=36&model=ir.module.module&view_type=kanban&cids=1&menu_id=5'
            'url':'http://localhost:8015/web#action=296&model=sale.order&view_type=list&cids=1&menu_id=178',
            'target':'self',
        }