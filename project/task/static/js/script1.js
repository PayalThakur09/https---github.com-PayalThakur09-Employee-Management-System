 // Salary Graph
 var ctx = document.getElementById('salaryGraph').getContext('2d');
 var salaryGraph = new Chart(ctx, {
     type: 'line',
     data: {
         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
         datasets: [{
             label: 'Salary',
             data: [3000, 3500, 4000, 3800, 4200, 4500],
             backgroundColor: 'rgba(52, 152, 219, 0.2)',
             borderColor: 'rgba(52, 152, 219, 1)',
             borderWidth: 2,
             pointBackgroundColor: 'rgba(52, 152, 219, 1)',
             pointRadius: 5,
             pointHoverRadius: 7
         }]
     },
     options: {
         scales: {
             y: {
                 beginAtZero: true
             }
         }
     }
 });