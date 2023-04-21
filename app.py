from flask import Flask, request, render_template, redirect
from sys import maxsize

# TODO
import clearly_not_a_db as not_db

app = Flask('lab4')

app.jinja_env.filters['zip'] = zip
app.jinja_env.filters['len'] = len


@app.route('/')
def index():
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

@app.route('/item/<int:dish_id>')
def item(dish_id:int):
    ingredients = not_db.ingredients
    
    dish = not_db.dishes[dish_id]
    curr_ingredients = []
    max_dishes = maxsize
    cost_per_dish = 0
    
    for ingredient in dish["recipe"].keys():
        curr_ingredients.append(ingredients[ingredient])
        
        for order in not_db.current_orders:
            # TODO check if works correctly
            if ingredient in order[0]["recipe"].keys():
                # max portions not counting existing orders
                possible_portions = ingredients[ingredient]["amount"] // dish["recipe"][ingredient]
                # sustract amopunt of currently made orders
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

# TODO
@app.route('/add2cart')
def add2cart():
    dish_id = request.args.get("id")
    amount = request.args.get("amount")
    return redirect("/shop")

# TODO
@app.route('/cart')
def cart():
    return render_template("cart.html")


if __name__ == '__main__':
    app.run()