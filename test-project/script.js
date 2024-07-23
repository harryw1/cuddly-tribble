document.addEventListener('DOMContentLoaded', () => {
    console.log("Sustainability Tracker Page Loaded");

    // Sample data
    const projectData = {
        labels: ['Project A', 'Project B', 'Project C'],
        datasets: [{
            label: 'Sustainability Score',
            data: [85, 78, 92],
            backgroundColor: ['#4caf50', '#ff9800', '#f44336'],
            borderColor: ['#388e3c', '#f57c00', '#d32f2f'],
            borderWidth: 1
        }]
    };

    // Configuration for the chart
    const config = {
        type: 'bar',
        data: projectData,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    // Render the chart
    const ctx = document.getElementById('sustainabilityChart').getContext('2d');
    const sustainabilityChart = new Chart(ctx, config);
});
