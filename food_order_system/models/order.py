from odoo import api, fields, models, _
import requests


class OrderDetails(models.Model):
    _name = 'order.details'
    _rec_name = 'order_id'


    order_id = fields.Char('Order ID', required=True, readonly=True, copy = False, default=lambda self: self.env['ir.sequence'].next_by_code('order.seq'))    
    food_name = fields.Many2one('dsl.food', string="Food", required=True)
    food_price = fields.Monetary(string='Unit Price',store=True, currency_field='currency_id')
    quantity = fields.Integer(string='Quantity', default=1)
    tablename = fields.Many2one('dsl.table',string='Place')
    date_field = fields.Date(string='Date', default=fields.Date.today)
    notes = fields.Text('Notes')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    total_amount = fields.Monetary(string='Total Amount', compute='_compute_total_amount', currency_field='currency_id', store=True)


    payment_method = fields.Many2one('qr.code')

    ip_link = fields.Many2one('res.config.settings', string='Config Settings')

   



    c_name = fields.Char('Customer Name')
    c_email = fields.Char('Email')
    c_phone = fields.Char('Phone')
    c_address = fields.Char('Address')
    

    # payment_method = fields.Selection([('credit_card', 'Credit Card'), (
    #     'cash', 'Cash'), ('bkash', 'B-Kash'), ('paypal', 'Paypal')], 'Payment Method')

    state = fields.Selection([
            ('draft', 'Draft'),
            ('confirm', 'Confirmed'),
            ('cancel', 'Cancelled'),
            ('done', 'Done'),
        ], default= "draft", string='Status')


 
    @api.depends('food_name.price', 'quantity')
    def _compute_total_amount(self):
        for record in self:
            record.food_price = record.food_name.price
            record.total_amount = record.food_price * record.quantity

    
    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    def action_done(self):
        self.state = 'done'

    def action_save(self):
        pass


    
    # def button1_action(self):
    #     devices = self.env['nodemcu.device'].search([])
    #     for device in devices:
    #         device.status = True
    #     return True

    
    # def button2_action(self):
    #     devices = self.env['nodemcu.device'].search([])
    #     for device in devices:
    #         device.status = True
    #     return True

    
    # def button3_action(self):
    #     devices = self.env['nodemcu.device'].search([])
    #     for device in devices:
    #         device.status = True
    #     return True


    
    
    def action_led1(self):
        response = requests.get('http://192.168.0.111/line1')

    def action_led2(self):
        response = requests.get('http://192.168.0.111/line2')


    def link_action(self):
        for rec in self:
            base_url = 'http://'
            ip_link = rec.ip_link or ''
            if ip_link:
                link = f'{base_url}{ip_link}'
                return {
                    'type': 'ir.actions.act_url',
                    'url': link,
                    'target': 'new',
                }


class QRCode(models.Model):
    _name = 'qr.code'
    _description = 'QR Code'
    _rec_name = "name"

    name = fields.Char(string='Payment Method', required=True)
    o_phone_number = fields.Char(string='Account Number')
    o_image = fields.Binary(string='QR Code', required=True)
    note = fields.Text(string='Add Note')
        
