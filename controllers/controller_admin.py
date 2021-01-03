from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.customer import Customer

import repositories.repository_customer as repository_customer
import repositories.repository_address as repository_address

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin')
def admin_home():
    return render_template('admin/index.jinja') 


# Show all customers
@admin_blueprint.route('/admin/customers', methods=['GET'])
def customers():
    # TODO ensure select_all exists in repo
    customers = repository_customer.select_all()
    # return 'template_name', jinja_list used in the template
    return render_template('admin/customers_all', all_customers = customers)


# Show customers by delivery day
@admin_blueprint.route('/admin/<day>', methods=['GET'])
def customers_by_day(day):
    # query database to find the id of <day>
    day_id = repository_customer.get_delivery_day_id(day)
    # pass day_id to
    customers_today = repository_customer.select_by_day(day_id)
    total_vegboxes = repository_customer.total_veg_box_by_day(day_id)
    return render_template('admin/day_view.jinja')

# Add customer
@admin_blueprint.route('/admin/customers/add')
def add_customer():
    first_name  = request.form['first_name']
    email       = request.form['email']
    address     = repository_address.select(request.form['address_id'])
    customer    = Customer(first_name, email, address)
    repository_customer.save(customer)
    return redirect('/admin/customers/add') 

# Edit customer
@admin_blueprint.route('/admin/customers/<id>', methods=['GET'])
def edit_customer(id):
    customer = repository_customer.select(id)
    addresses = repository_address.select_all_addresses()
    return render_template('admin/edit_customer.jinja', customer = customer, addresses = addresses )

# customer_edit: GET
# customer_delete: GET
# notes_add: POST
# notes_edit: GET
# notes_delete: GET