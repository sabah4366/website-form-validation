from odoo import http
import re
from odoo.http import request
class WebsiteForm(http.Controller):

    @http.route('/website/form', type='http', auth='public', website=True)
    def website_form(self, **kw):
        return http.request.render('custom_website.website_form_template', {})

    @http.route('/create/res/partner', type='http', auth='public', website=True)
    def website_form_submission(self,**kw):
        print('1234444',kw)
        # request.env['res.partner'].sudo().create(kw)
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        phone_pattern = re.compile(r'^\d{10}$')
        email = kw.get('email')
        phone = kw.get('phone')
        phoneChecking = phone_pattern.match(phone)
        emailChecking = email_pattern.match(email)
        if request.httprequest.method == 'POST':
            print('POST METHOD',kw.get('name'))
            error_list = []
            if not kw.get('name'):
                error_list.append('Enter name')
            if not kw.get('email'):
                error_list.append('Enter mail')
            if not kw.get('phone'):
                error_list.append('Enter phone')
            if not emailChecking:
                error_list.append('Enter valid email')
            if not phoneChecking:
                error_list.append('Enter valid phone')
            if not  error_list:
                request.env['res.partner'].sudo().create(kw)
                return request.render('custom_website.website_form_success_template', {})




