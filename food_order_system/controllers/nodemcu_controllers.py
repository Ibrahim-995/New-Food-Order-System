from odoo import http
from odoo.http import request


# class NodeMCUController(http.Controller):
#     @http.route('/api/button1', type='json', auth='public', methods=['POST'])
#     def button1_action(self):
#         node_mcu = request.env['nodemcu.device']
#         node_mcu.button1_action()
#         return {'result': True}

#     @http.route('/api/button2', type='json', auth='public', methods=['POST'])
#     def button2_action(self):
#         node_mcu = request.env['nodemcu.device']
#         node_mcu.button2_action()
#         return {'result': True}

#     @http.route('/api/button3', type='json', auth='public', methods=['POST'])
#     def button3_action(self):
#         node_mcu = request.env['nodemcu.device']
#         node_mcu.button3_action()
#         return {'result': True}
