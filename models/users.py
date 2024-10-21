from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    user_group_selection = fields.Selection([
        ('customer', 'Customer'),
        ('areas_public', 'Areas Public'),
        ('edit_not_public', 'Edit Not Public')
    ], string="User Group")
