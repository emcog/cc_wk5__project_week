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

    # pass delivery_day_id to
    vegboxes_for_today = repository_customer.select_by_day(delivery_day_id)
    total_vegboxes = repository_customer.total_veg_box_by_day(delivery_day_id)
    return render_template('driver/dashboard.jinja', todays_vegboxes = vegboxes_for_today, total_vegboxes_for_today = total_vegboxes) 


# what is the working sql query which joins delivery with subscription type?

SELECT * 
FROM customers 
JOIN addresses ON customers.address_id=addresses.id
WHERE delivery_day_id = %s AND subscription_id = 1


# what needs to be done to above to make it dynamic?
# static values need to be replaced with dynamic variables from the router


# what does select_by_day do?
# SELECT * FROM customers WHERE delivery_day_id = %s

# need to make subscription_id dynamic therefore:
# query db for subscription id or id's
# could this use a 'does not equal?'