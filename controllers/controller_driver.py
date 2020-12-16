from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

driver_blueprint = Blueprint('driver', __name__)

@farmer_blueprint.route('/driver')
def test_farmer():
    return render_template('driver/index.jinja') 
