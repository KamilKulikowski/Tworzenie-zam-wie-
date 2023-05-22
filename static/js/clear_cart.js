var Form = document.querySelectorAll(".CartFunctions");

function clear_cart() {
        var btn = document.getElementById("1");
        btn.addEventListener("click", e => {
            e.preventDefault();

            fetch(`/clear_cart/`, {
                method: 'GET',
            })

                .then(response => response.json())
                .then(data => {
                    alert(data['message'])
                })
                .then(() => {
                    window.location.reload();
                })
                .catch((error) => {
                    console.error('Error:', error);
                });

        })
}

clear_cart(Form)
