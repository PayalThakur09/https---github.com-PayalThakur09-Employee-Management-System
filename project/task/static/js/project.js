
    // Simulated project data (in a real scenario, fetch this from a server)
    var projects = [
        { title: "Project 1", assignedTo: "John Doe", status: "In Progress", progress: 60, startDate: "10-04-2024", completionDate: "28-05-2024" },
        { title: "Project 2", assignedTo: "Jay Khurana", status: "Completed", progress: 100, startDate: "20-04-2024", completionDate: "05-04-2024" },
        { title: "Project 3", assignedTo: "Jay khurana", status: "Pending", progress: 30, startDate: "25-04-2024", completionDate: "25-06-2024" }
        // Add more project objects as needed
    ];

    $(document).ready(function () {
        // Loop through projects array and create project cards dynamically
        projects.forEach(function (project) {
            var projectCard = `
                <div class="col-md-4">
                    <div class="card project-card">
                        <div class="card-body" >
                            <h5 class="card-title">${project.title}</h5>
                            <p class="card-text">Assigned to: ${project.assignedTo}</p>
                            <p class="card-text">Status: ${project.status}</p>
                            <p class="card-text">Start Date: ${project.startDate}</p>
                            <p class="card-text">Completion Date: ${project.completionDate}</p>
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: ${project.progress}%" aria-valuenow="${project.progress}" aria-valuemin="0" aria-valuemax="100">${project.progress}%</div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
            $('#project-container').append(projectCard);
        });
    });
