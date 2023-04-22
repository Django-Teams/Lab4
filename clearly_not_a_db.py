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
            "Молоко": 150,
            "Вершкове масло": 25
        }
    },
    {
        "name": "Картопляний суп",
        "desc": "Традиційно під час приготування картопляного супу слід використовувати селеру, ріпчасту цибулю, часник і цибулю-порей. Всі ці інгредієнти, порізані кубиками або скибочками, додають страві достатньо пікантності, створюючи особливий смак. Тим не менш, стежте за кількістю, ці інгредієнти разом повинні становити не більше, ніж половину використаної картоплі. Додавайте екзотичні інгредієнти в менших пропорціях. Що вважати екзотичним? Все, починаючи з сиру чеддер, каррі і шматочків бекону. Запам'ятайте: використовуйте тільки один екзотичний інгредієнт, інакше отримаєте не очікуваний мікс, а суміш протилежних смаків.",
        "img": "https://d3d173w0vohr0k.cloudfront.net/ua-ua/articles/88dbb6057996de67e1de923e3f288ec1/6a63668fdce2f22495e7fe4ebc22a510.jpg",
        "recipe": {
            "Картопля": 100,
            "Морква": 100
        }
    },
    {
        "name": "Картопля в мундирі",
        "desc": "Картопля в мундирі - улюблений гарнір багатьох українців. Її можна подавати до оселедця, м'яса і багатьох інших самостійних страв. Якщо ви не знали, що означає вираз 'картопля в мундирі', то все просто - це овоч, зварений в шкірці. А колір цієї самої шкірки нагадує військовий мундир.",
        "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTp8pIFRHFd_-yWWvrnh036i9k9_7VV6X5cgQ&usqp=CAU",
        "recipe": {
            "Картопля": 200,
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
    "Морква": {
        "amount": 1000,
        "price": 1
    },
}


current_orders = [
    # [dish, amount],
    [dishes[0], 1]
]