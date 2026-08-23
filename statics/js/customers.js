document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("customerSearch");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            const searchValue = this.value.toLowerCase();

            const rows = document.querySelectorAll(
                "#customerTable tbody tr"
            );

            rows.forEach(function (row) {

                const rowText = row.textContent.toLowerCase();

                if (rowText.includes(searchValue)) {
                    row.style.display = "";
                } else {
                    row.style.display = "none";
                }

            });

        });

    }

});