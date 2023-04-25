from flask import Flask, request, render_template, redirect
from sys import maxsize

import clearly_not_a_db as not_db
import consts

app = Flask('lab4')

# adding functions to the jinja templates
app.jinja_env.filters['zip'] = zip
app.jinja_env.filters['len'] = len


@app.route('/')
def index():
    """!!! does not have its own page !!!"""
    return redirect("/home")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/shop')
def shop():
    return render_template("shop.html",
                           dishes=not_db.dishes,
                           dishes_count=len(not_db.dishes))

@app.route('/shop/item/<int:dish_id>')
def shop_item_dish(dish_id:int):
    ingredients = not_db.ingredients
    
    dish = not_db.dishes[dish_id]
    curr_ingredients = []
    max_dishes = maxsize
    cost_per_dish = 0
    
    # calc each dish's cost
    for ingredient in dish["recipe"].keys():
        curr_ingredients.append(ingredients[ingredient])
        
        # max portions not counting existing orders
        possible_portions = ingredients[ingredient]["amount"] // dish["recipe"][ingredient]
        # sustract amount of currently made orders
        for order in not_db.current_orders:
            if ingredient in order[0]["recipe"].keys():
                possible_portions -= order[1]
        if max_dishes > possible_portions:
            max_dishes = possible_portions
        
        cost_per_dish += dish["recipe"][ingredient] * ingredients[ingredient]["price"]
    
    return render_template("item.html",
                           dish=dish,
                           dish_id=dish_id,
                           ingredients=curr_ingredients,
                           max_dishes=max_dishes,
                           cost_per_dish=cost_per_dish)

@app.route('/shop/item/add')
def shop_item_add():
    """!!! does not have its own page !!!"""
    dish_id = int(request.args.get("id"))
    amount = int(request.args.get("amount"))
    not_db.current_orders.append([not_db.dishes[dish_id], amount])
    return redirect("/shop")

@app.route('/cart')
def cart():
    curr_orders = not_db.current_orders
    ingredients = not_db.ingredients
    total_cost = 0
    # calc total cost
    for order in curr_orders:
        recipe = order[0]["recipe"]
        ingredient_cost = 0
        for k in recipe.keys():
            cost = ingredients[k]["price"]
            amount = recipe[k]
            ingredient_cost += round(amount * cost * consts.NAVAR, 2)
        ingredient_cost *= order[1]
        total_cost += ingredient_cost
        # order[2] = ingredient_cost
        order.append(ingredient_cost)
    return render_template("cart.html",
                           curr_orders=curr_orders,
                           order_count=len(curr_orders),
                           total_cost=round(total_cost, 2))

@app.route('/order/del', methods=["POST"])
def order_del():
    """!!! does not have its own page !!!"""
    id = request.json["value"]
    del not_db.current_orders[id]
    return ""


if __name__ == '__main__':
    app.run()