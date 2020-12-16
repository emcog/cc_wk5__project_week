from flask import Flask, render_template, request, redirect
from flask import Blueprint
import repositories.repository_customer as repository_customer

farmer_blueprint = Blueprint('farmer', __name__)

@farmer_blueprint.route('/farmer')
def test_farmer():
    return render_template('farmer/index.jinja') 


# @farmer_blueprint.route('/farmer/<day>')
# def vegboxes_to_harvest(day):
#     # take day and convert to int, pass int
#     if day == monday:
#         delivery_day_id = 1
#     elif day == wednesday:
#         delivery_day_id = 2
#     elif day == friday:
#         delivery_day_id = 3

#     vegboxes_for_today = repository_customer.select_by_day(delivery_day_id)
#     return render_template('famer/index.jinja', todays_harvest = vegboxes_for_today) 



# -----> index
# select role (admin, farmer, driver)

# -----> farmer
# select day (mon, wed, fri)
