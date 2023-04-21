const amountElement = document.getElementById("add2cart-amount")

amountElement.addEventListener("change", (event) => {
    const text = `Ціна: ${event.target.value * cost_per_dish}`
    document.getElementById("add2cart-cost").innerHTML = text
})

if (max_dishes <= 0) {
    document.getElementById("add2cart-cost").innerHTML = "Нема в наявності"
    document.getElementById("add2cart-submit").disabled = true
}