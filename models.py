from odoo import models, fields

class Todo(models.Model):
    _name="proyecto.todo"

    name = fields.Char("Descripcion")
    status = fields.Selection(selection=[("pendiente", "Pendiente"), ("en proceso", "En Proceso"), ("en prueba", "En Prueba"), ("finalizado", "Finalizado")])