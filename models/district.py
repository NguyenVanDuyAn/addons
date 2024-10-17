from odoo import models, fields
import sys
sys.setrecursionlimit(1500)  # Tăng giới hạn đệ quy

class District(models.Model):
    _name = 'res.country.district'
    _description = 'Districts'

    name = fields.Char(string='District Name', required=True)
    province_id = fields.Many2one('res.country.state', string='Province/City', required=True)
    ward_ids = fields.One2many('res.country.ward', 'district_id', string='Wards')
