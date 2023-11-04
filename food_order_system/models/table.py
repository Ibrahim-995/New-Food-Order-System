from odoo import models, fields, api

class table(models.Model):
    _name = 'dsl.table'
    
    name = fields.Char(string='Place Name', required=True)
    # capacity = fields.Integer(string='Capacity', required=True)
    note = fields.Text(string='Note')

