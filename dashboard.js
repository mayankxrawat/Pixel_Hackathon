const punchLogs = [
    { date: '2025-04-21', in: '09:00', out: '17:00' },
    { date: '2025-04-22', in: '09:10', out: '16:50' },
];

const weeklyHours = 24;  // Example value

const punchList = document.getElementById('punchLogs');
punchLogs.forEach(log => {
    const li = document.createElement('li');
    li.textContent = `${log.date}: In at ${log.in}, Out at ${log.out}`;
    punchList.appendChild(li);
});

document.getElementById('weeklyCompleted').textContent = weeklyHours ;

const dayOfWeek = new Date().getDay();
const required = 35;
const projectedPercent = (weeklyHours / required) * 100;
const shortfallAlert = document.getElementById('shortfallAlert');

if (projectedPercent < 60) {
    shortfallAlert.textContent = "Warning: Less than 60% of required hours completed!";
} else if (projectedPercent <= 100 && projectedPercent >= 60) {
    shortfallAlert.textContent = `Keep going! You're at ${projectedPercent.toFixed(1)}%.`;
} else {
    shortfallAlert.textContent = "Great job! You've met your goal.";
}

function generateCalendar() {
    const calendar = document.getElementById('calendar');
    const today = new Date();
    const year = today.getFullYear();
    const month = today.getMonth();
    const daysInMonth = new Date(year, month + 1, 0).getDate();

    for (let day = 1; day <= daysInMonth; day++) {
        const dateStr = `${year}-${String(month + 1).padStart(2, '0')}-${String(day).padStart(2, '0')}`;
        const entry = punchLogs.find(p => p.date === dateStr);
        const div = document.createElement('div');
        div.className = 'calendar-day';
        div.textContent = day;
        if (entry) {
            div.style.backgroundColor = "#00c0a3"; 
        }
        calendar.appendChild(div); 
    }
}

generateCalendar();
