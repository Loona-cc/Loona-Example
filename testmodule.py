from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
import config
module = Blueprint('Module', __name__)
module.hasAdminPage = False
module.moduleDescription = 'A test module'
module.version = '1.0'

@module.route('/test')
def show():
    return 'Test'
