from odoo import models, fields

class BlogPost(models.Model):
    _inherit = 'blog.post'

    areas_post = fields.One2many('areas.area', 'blog_id', string = 'Area Post')
