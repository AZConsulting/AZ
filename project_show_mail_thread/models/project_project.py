# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectProject(models.Model):
    _name = 'project.project'
    _inherit = ['project.project', 'mail.activity.mixin', 'rating.mixin']

