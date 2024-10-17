from odoo import models, fields
import sys
sys.setrecursionlimit(1500)  # Tăng giới hạn đệ quy

class Province(models.Model):
    _name = 'res.country.state'
    _description = 'Provinces/Cities'

    name = fields.Char(string='Province/City Name', required=True)
    code = fields.Char(string='Province Code')
    country_id = fields.Many2one('res.country', string='Country', required=True)
    district_ids = fields.One2many('res.country.district', 'province_id', string='Districts')
