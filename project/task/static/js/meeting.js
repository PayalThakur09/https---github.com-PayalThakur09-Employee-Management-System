
    // Simulated meeting data (in a real scenario, fetch this from a server)
    var meetings = [
        { title: "Team Meeting", date: "2024-05-11", time: "10:00 AM", place: "Conference Room A", attendees: ["Sahil More", "Jay Khurana", "Shital Shahu,Payal Thakur,Ashok Bhure"], attendeesCount: 5, status: "Done" },
        { title: "Project Discussion", date: "2024-05-25", time: "2:00 PM", place: "Online", attendees: ["Sahil More", "Jay Khurana", "John Doe, Rakesh Sharma"], attendeesCount: 4, status: "Planned" },
        { title: "Client Meeting", date: "2024-05-15", time: "11:00 AM", place: "Client Office", attendees: ["Sahil More", "Jay Khurana", "Payal Thakur,Ashok Bhure"], attendeesCount: 4, status: "Done" }
        // Add more meeting objects as needed
    ];

    $(document).ready(function () {
        // Display meetings
        meetings.forEach(function (meeting) {
            var meetingCard = `
                <div class="card meeting-card">
                    <div class="card-body">
                        <h5 class="card-title">${meeting.title}</h5>
                        <p class="card-text"><strong>Date:</strong> ${meeting.date}</p>
                        <p class="card-text"><strong>Time:</strong> ${meeting.time}</p>
                        <p class="card-text"><strong>Place:</strong> ${meeting.place}</p>
                        <p class="card-text"><strong>Attendees (${meeting.attendeesCount}):</strong> ${meeting.attendees.join(', ')}</p>
                        <p class="card-text"><strong>Status:</strong> ${meeting.status}</p>
                    </div>
                </div>
            `;
            if (meeting.status === 'Done') {
                $('#scheduled-meetings').append(meetingCard);
            } else {
                $('#upcoming-meetings').append(meetingCard);
            }
        });
    });
