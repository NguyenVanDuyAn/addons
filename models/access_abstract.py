from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)

class AccessAbstract(models.AbstractModel):
    _name = 'user.access.abstract'
    _description = 'Abstract Model for User Access'

    def _default_value(self, roleName):
        return self.env.user.has_group(
            'parking_odoo.' + roleName)

    def _default_value_role_name_list(self, roleNameList):
        return any(self.env.user.has_group('parking_odoo.' + role) for role in roleNameList)

    user_has_access = fields.Boolean(
        compute='_compute_user_access', default=lambda self: self._default_value("areas_customer"))
    admin_has_access = fields.Boolean(
        compute='_compute_admin_access',  default=lambda self: self._default_value("areas_admin"))
    operator_has_access = fields.Boolean(
        compute='_compute_operator_access',  default=lambda self: self._default_value("areas_employee"))
    sercurity_manager_operator_has_access = fields.Boolean(
        compute='_compute_sercurity_manager_operator_access',  
        default=lambda self: self._default_value_role_name_list(["security_readonly_list", "user_access_manager", "areas_employee"]))
    user_sercurity_manager_has_access = fields.Boolean(
        compute='_compute_user_sercurity_manager_access',  
        default=lambda self: self._default_value_role_name_list(["security_readonly_list", "user_access_manager", "user_access"]))

    @api.depends('user_has_access')
    def _compute_user_access(self):
        for record in self:
            record.user_has_access = record.env.user.has_group(
                'parking_odoo.areas_customer')

    @api.depends('admin_has_access')
    def _compute_admin_access(self):
        for record in self:
            record.admin_has_access = record.env.user.has_group(
                'parking_odoo.areas_admin')

    @api.depends('operator_has_access')
    def _compute_operator_access(self):
        for record in self:
            record.operator_has_access = record.env.user.has_group(
                'parking_odoo.areas_employee')

    @api.depends('sercurity_manager_operator_has_access')
    def _compute_sercurity_manager_operator_access(self):
        for record in self:
            record.sercurity_manager_operator_has_access = any(
                record.env.user.has_group(f'parking_odoo.{group}')
                for group in ['security_readonly_list', 'user_access_manager', 'areas_employee']
            )

    @api.depends('user_sercurity_manager_has_access')
    def _compute_user_sercurity_manager_access(self):
        for record in self:
            record.user_sercurity_manager_has_access = any(
                record.env.user.has_group(f'parking_odoo.{group}')
                for group in ['security_readonly_list', 'user_access_manager', 'areas_customer']
            ) 