dishes = (
    # example
    # {
    #     "name": str,
    #     "desc": str,
    #     "img": str,   !!! height >= width !!!
    #     "recipe": {
    #         "ingredient": amount:int,
    #     }
    # },
    {
        "name": "Картопляне пюре",
        "desc": "Швидко, назвіть щось краще за неймовірно кремове та вершкове картопляне пюре, яке просто тане у роті! Скоріш за все, у вас не вийде. Але і не треба, якщо можна просто насолоджуватися цим чудовим смаком. Картоплю пюре ми готуємо на гарнір до святкового столу чи на вечерю у звичайний день, додаємо масло чи сметану, вершки чи молоко, і все це дуже смачно. Ця страва знайома з дитинства чи не кожному з нас. Давайте раз і назавжди навчимося готувати картопляне пюре ідеально!",
        "img": "https://twokooksinthekitchen.com/wp-content/uploads/2020/12/mashed-potatoes.jpg",
        "recipe": {
            "Картопля": 100,
            "Молоко": 150
        }
    },
)


ingredients = {
    # example
    # "name": {
    #     "amount": int,
    #     "price": int
    # },
    "Картопля": {
        "amount": 1000,
        "price": 1
    },
    "Молоко": {
        "amount": 1000,
        "price": 1
    },
    "Вершкове масло": {
        "amount": 1000,
        "price": 1
    },
}


current_orders = [
    # [dish, amount],
    
]