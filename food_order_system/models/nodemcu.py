from odoo import api, fields, models


class NodeMCUDevice(models.Model):
    _name = 'nodemcu.device'
    _description = 'NodeMCU Device'

    name = fields.Char(string='Name')
    status = fields.Boolean(string='Status', default=False)

    # @api.model
    # def button1_action(self):
    #     devices = self.search([])
    #     for device in devices:
    #         device.status = True
    #     return True

    # @api.model
    # def button2_action(self):
    #     devices = self.search([])
    #     for device in devices:
    #         device.status = True
    #     return True

    # @api.model
    # def button3_action(self):
    #     devices = self.search([])
    #     for device in devices:
    #         device.status = True
    #     return True
