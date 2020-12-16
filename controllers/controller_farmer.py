from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

farmer_blueprint = Blueprint('farmer', __name__)

@farmer_blueprint.route('/farmer')
def farmer_home():
    return render_template('farmer/index.jinja') 


@farmer_blueprint.route('/farmer/<day>')
def vegboxes_today(day):

    # sql query to find the id of <day>
    delivery_day_id = repository_customer.get_delivery_day_id(day)

    vegboxes_for_today = repository_customer.select_by_day(delivery_day_id)
    total_vegboxes = repository_customer.total_veg_box_by_day(delivery_day_id)
    return render_template('farmer/dashboard.jinja', todays_vegboxes = vegboxes_for_today, total_vegboxes_for_today = total_vegboxes) 