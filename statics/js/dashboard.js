document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".dashboard-card");

    cards.forEach(function (card) {

        card.addEventListener("mouseenter", function () {
            card.style.transform = "translateY(-3px)";
            card.style.transition = "0.2s";
        });

        card.addEventListener("mouseleave", function () {
            card.style.transform = "translateY(0)";
        });

    });

});