# -*- coding: utf-8 -*-
# from odoo import http


# class Odooacademy(http.Controller):
#     @http.route('/odooacademy/odooacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odooacademy/odooacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odooacademy.listing', {
#             'root': '/odooacademy/odooacademy',
#             'objects': http.request.env['odooacademy.odooacademy'].search([]),
#         })

#     @http.route('/odooacademy/odooacademy/objects/<model("odooacademy.odooacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odooacademy.object', {
#             'object': obj
#         })
