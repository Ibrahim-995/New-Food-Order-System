from odoo import models, fields, api
import base64


class food(models.Model):
    _name = 'dsl.food'
    
    name = fields.Char(string='Name', required=True)
    price = fields.Monetary(string='Price', required=True, store=True, currency_field='currency_id')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

