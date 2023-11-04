from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    robot_ip = fields.Char('Robot IP Address')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update({
            'robot_ip': self.env['ir.config_parameter'].sudo().get_param('food_order_system.robot_ip', default=''),
        })
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('food_order_system.robot_ip', self.robot_ip)
