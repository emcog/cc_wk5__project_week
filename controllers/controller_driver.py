from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

driver_blueprint = Blueprint('driver', __name__)

@driver_blueprint.route('/driver')
def driver_home():
    return render_template('driver/index.jinja') 


@driver_blueprint.route('/farmer/<day>')
def vegboxes_to_deliver(day):
    # take day and convert to int, pass int
    # give me the idea of monday sql queries

    # if day == 'monday':
    #     delivery_day_id = 1
    # elif day == 'wednesday':
    #     delivery_day_id = 2
    # elif day == 'friday':
    #     delivery_day_id = 3

    delivery_day_id = repository_customer.get_delivery_day_id(day)
    # import pdb; pdb.set_trace()

    vegboxes_for_today = repository_customer.select_by_day(delivery_day_id)
    total_vegboxes = repository_customer.total_veg_box_by_day(delivery_day_id)
    return render_template('farmer/dashboard.jinja', todays_harvest = vegboxes_for_today, total_vegboxes_for_today = total_vegboxes) 
