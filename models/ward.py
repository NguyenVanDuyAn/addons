from odoo import models, fields
import sys
sys.setrecursionlimit(1500)  # Tăng giới hạn đệ quy

class Ward(models.Model):
    _name = 'res.country.ward'
    _description = 'Wards'

    name = fields.Char(string='Ward Name', required=True)
    district_id = fields.Many2one('res.country.district', string='District', required=True)
