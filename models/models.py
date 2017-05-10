# -*- coding: utf-8 -*-

from odoo import models, fields, api


class route(models.Model):
    _name = 'cxc.route'

    name = fields.Char('RouteName')
    date = fields.Datetime('Fecha de la ruta')
    driver_id = fields.Many2one('res.users', 'Conductor')
    zones = fields.Many2many( 'cxc.route.zone', # modelo relacionado
                                        'cxc_route_relation', # nombre de la tabla de relación
                                        'route_id', # campo para "este" registro
                                        'zone_id', # campo para "otro" registro
                                        string='Zonas')
    route_state = fields.Selection([(1,'Asignada'),(2,'Proceso'),(3,'Terminada')])


class zone(models.Model):
    _name = 'cxc.route.zone'

    name = fields.Char('Nombre de la zona')
    customers = fields.One2many('res.partner','zone_id', 'Clientes')
    #route_id = fields.Many2one('cxc.route', 'Ruta')

class customer(models.Model):
    _inherit = 'res.partner'

    person_id = fields.Char('Cedula')
    zone_id = fields.Many2one('cxc.route.zone','Ruta')
    accounts = fields.One2many('cxc.account', 'customerId', 'Cuentas')

    def userAccounts(self):

        res = {
            'type': 'ir.actions.act_window',
            'name': 'Cuentas de '+ self.name,
            'res_model': 'cxc.account',
            'view_mode': 'tree,form',
            'target': 'current',
            'context': {'custmerId': self.id, 'search_default_customerId':self.id, 'default_customerId':self.id }
        }

        return res


class account(models.Model):
    _name = 'cxc.account'

    name = fields.Char("Descripción")
    initialAmmount = fields.Float('Monto inicial')
    actualAmmount = fields.Float('Saldo', compute='compute_calc_actual_ammount')
    interestRate = fields.Float('Tasa de interes')
    numberOfPayments = fields.Integer('Cantidad de pagos')
    charge = fields.Float('Cuota')
    paymentTerm = fields.Selection([(1,'Semanal'),(2,'Quincenal'),(3,'Mensual pago 15s'),(4,'Mensual pago 30s')],'Forma de pago')
    customerId = fields.Many2one('res.partner','Cliente')
    payments = fields.One2many('cxc.account.payment','accountId','Abonos')
    already_pay = fields.Boolean('Pagada?')

    @api.one
    def compute_calc_actual_ammount(self):
        self.actualAmmount = self.initialAmmount
        for p in self.payments:
            if p.approved:
                self.actualAmmount -= p.ammount


    def create_payment(self):

        view_ref = self.env['ir.model.data'].get_object_reference('cuentas_por_cobrar', 'view_form_cxc_account_payment')
        view_id = view_ref[1] if view_ref else False
        res = {
            'type': 'ir.actions.act_window',
            'name': 'Payment form',
            'res_model': 'cxc.account.payment',
            'view_type': 'form',
            'view_mode': 'form',
            'view_id': view_id,
            'target': 'current',
            'context': {'default_accountId': self.id}
        }

        return res

class payment(models.Model):
    _name = 'cxc.account.payment'

    ammount = fields.Float('Monto')
    approved = fields.Boolean('Aprobado')
    date = fields.Date('Fecha')
    accountId = fields.Many2one('cxc.account','Cuenta')

class driver(models.Model):
    _inherit = 'res.users'

    is_driver = fields.Boolean('Conductor')
    routes = fields.One2many('cxc.route','driver_id','Rutas')

