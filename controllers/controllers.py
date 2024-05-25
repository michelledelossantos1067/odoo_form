# -*- coding: utf-8 -*-
from odoo import http
from odoo.sql_db import db_connect

class MyModule(http.Controller):
    @http.route('/my_module/my_module/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_module/my_module/objects/', auth='public')
    def list(self, **kw):
        db = http.request.env['ir.config_parameter'].sudo().get_param('db_name')
        with db_connect(user='postgres', password='qawsed', port=5433, host='localhost', database='sistema').cursor() as cr:
            cr.execute("SELECT * FROM my_module_my_module")
            records = cr.fetchall()
        return http.request.render('my_module.listing', {
            'root': '/my_module/my_module',
            'objects': records,
        })

    @http.route('/my_module/my_module/objects/<model("my_module.my_module"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_module.object', {
            'object': obj
        })
