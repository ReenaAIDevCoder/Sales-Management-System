document.addEventListener("DOMContentLoaded", function () {

    const dealValue = document.getElementById("deal_value");
    const probability = document.getElementById("probability");
    const forecastValue = document.getElementById("forecast_value");

    function calculateForecast() {

        if (!dealValue || !probability || !forecastValue) {
            return;
        }

        const value = parseFloat(dealValue.value) || 0;
        const probabilityValue =
            parseFloat(probability.value) || 0;

        const forecast =
            value * (probabilityValue / 100);

        forecastValue.textContent =
            forecast.toFixed(2);
    }

    if (dealValue) {
        dealValue.addEventListener(
            "input",
            calculateForecast
        );
    }

    if (probability) {
        probability.addEventListener(
            "input",
            calculateForecast
        );
    }

});