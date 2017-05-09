# -*- coding: utf-8 -*-
from odoo import http

# class CuentasPorCobrar(http.Controller):
#     @http.route('/cuentas_por_cobrar/cuentas_por_cobrar/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cuentas_por_cobrar/cuentas_por_cobrar/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cuentas_por_cobrar.listing', {
#             'root': '/cuentas_por_cobrar/cuentas_por_cobrar',
#             'objects': http.request.env['cuentas_por_cobrar.cuentas_por_cobrar'].search([]),
#         })

#     @http.route('/cuentas_por_cobrar/cuentas_por_cobrar/objects/<model("cuentas_por_cobrar.cuentas_por_cobrar"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cuentas_por_cobrar.object', {
#             'object': obj
#         })