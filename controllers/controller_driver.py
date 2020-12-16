from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

driver_blueprint = Blueprint('driver', __name__)

@driver_blueprint.route('/driver')
def driver_home():
    return render_template('driver/index.jinja') 


@driver_blueprint.route('/driver/<day>')
def vegboxes_today(day):

    # sql query to find the id of <day>
    delivery_day_id = repository_customer.get_delivery_day_id(day)

    vegboxes_for_today = repository_customer.select_by_day(delivery_day_id)
    total_vegboxes = repository_customer.total_veg_box_by_day(delivery_day_id)
    return render_template('driver/dashboard.jinja', todays_vegboxes = vegboxes_for_today, total_vegboxes_for_today = total_vegboxes) 