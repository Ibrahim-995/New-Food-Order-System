from odoo import http
from odoo.http import request


class Websitefood(http.Controller):

    @http.route('/foods', type='http', auth="public", website=True)
    def food_list(self, **kw):
        foods = request.env['dsl.food'].sudo().search([])
        return request.render('food_order_system.template_food_web', {'foods': foods})

    @http.route(['/customer/details/<int:food_id>'], type='http', auth="public", website=True)
    def customer_details(self, food_id=None, **kw):
        food = request.env['dsl.food'].sudo().browse(food_id)
        tablename = request.env['dsl.table'].sudo().search([])
        payment_method = request.env['qr.code'].sudo().search([])
        food_name = food.name
        food_price = food.price
        tablename = tablename
        payment_method = payment_method
        return request.render('food_order_system.template_customer_details', {
            'food_name': food_name,
            'food_price': food_price,
            'tablename': tablename,
            'payment_method' : payment_method,
        })

    @http.route('/submit/details/', type='http', auth="public", website=True)
    def submit_details(self, **kw):
        food_name = kw.get('food_name')
        food = request.env['dsl.food'].sudo().search([('name', '=', food_name)], limit=1)

        order_info = {
            'food_name': food.id,
            'food_price': kw.get('food_price'),
            'quantity': kw.get('quantity'),
            'tablename': kw.get('tablename'),
            'notes': kw.get('notes'),
            'c_name': kw.get('c_name'),
            'c_email': kw.get('c_email'),
            'c_phone': kw.get('c_phone'),
            'c_address': kw.get('c_address'),
            'payment_method': kw.get('payment_method'),
        }

        request.env['order.details'].sudo().create(order_info)

        return request.render('food_order_system.thank_you_id', {})




