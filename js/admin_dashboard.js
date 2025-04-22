const facultyData = {
    'MAYANK': { hours: 31 },
    'JAY': { hours: 29 }
};

const selector = document.getElementById('facultySelector');
Object.keys(facultyData).forEach(name => {
    const option = document.createElement('option');
    option.value = name;
    option.textContent = name;
    selector.appendChild(option);
});

selector.addEventListener('change', () => {
    const selected = selector.value;
    const status = facultyData[selected];
    document.getElementById('facultyStatus').textContent =
        `Completed Hours: ${status.hours}`;
});

// Holiday Calendar Logic
const holidays = [];

function addHoliday() {
    const date = document.getElementById('holidayDate').value;
    if (date && !holidays.includes(date)) {
        holidays.push(date);
        const li = document.createElement('li');
        li.textContent = date;
        document.getElementById('holidayList').appendChild(li);
    }
}

// Export CSV
function exportToCSV() {
    const rows = [['Name', 'Completed Hours']];
    for (const name in facultyData) {
        rows.push([name, facultyData[name].hours]);
    }

    let csvContent = "data:text/csv;charset=utf-8," + rows.map(e => e.join(",")).join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "faculty_hours.csv");
    document.body.appendChild(link);
    link.click();
}
