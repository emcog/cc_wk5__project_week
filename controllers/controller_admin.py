from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def test_farmer():
    return render_template('admin/index.jinja') 
