function createSalesChart(elementId, labels, values) {

    const canvas = document.getElementById(elementId);

    if (!canvas) {
        return;
    }

    if (typeof Chart === "undefined") {
        console.warn("Chart.js is not loaded.");
        return;
    }

    new Chart(canvas, {
        type: "bar",

        data: {
            labels: labels,

            datasets: [
                {
                    label: "Sales",
                    data: values
                }
            ]
        },

        options: {
            responsive: true,

            plugins: {
                legend: {
                    display: true
                }
            }
        }
    });
}