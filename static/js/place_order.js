var Form = document.querySelectorAll(".CartFunctions");

function place_order() {
        var btn = document.getElementById("2");
        btn.addEventListener("click", e => {
            e.preventDefault();

            fetch(`/place_order/`, {
                method: 'GET',
            })

                .then(response => response.json())
                .then(data => {
                    alert(data['message'])
                })

                .catch((error) => {
                    console.error('Error:', error);
                });

        })
}

place_order(Form)
