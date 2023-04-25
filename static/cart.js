const eXes = Array.from(document.getElementsByClassName("order-del"))
eXes.forEach(X => {
    X.addEventListener("click", () => {
        $.ajax({
            url: `${window.location.origin}/order/del`,
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({
                "value": parseInt(X.id)
            }),
            success: () => {
                window.location.href = `${window.location.origin}/shop`
            }
        })
    })
})