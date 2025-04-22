const monthYearElement = document.getElementById('month-year');
const daysElement = document.querySelector('.calendar-days');
const prevMonthButton = document.getElementById('prev-month');
const nextMonthButton = document.getElementById('next-month');

let currentDate = new Date();

const monthNames = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
];

function renderCalendar(year, month) {
    // Set header
    monthYearElement.textContent = `${monthNames[month]} ${year}`;

    // Clear previous days
    daysElement.innerHTML = '';

    const firstDayOfMonth = new Date(year, month, 1).getDay(); // 0=Sun, 1=Mon, ...
    const daysInMonth = new Date(year, month + 1, 0).getDate();
    const today = new Date();
    const todayDateString = `${today.getFullYear()}-${today.getMonth()}-${today.getDate()}`;

    // Add empty cells for days before the 1st of the month
    for (let i = 0; i < firstDayOfMonth; i++) {
        const emptyCell = document.createElement('div');
        emptyCell.classList.add('empty');
        daysElement.appendChild(emptyCell);
    }

    // Add day cells
    for (let day = 1; day <= daysInMonth; day++) {
        const dayCell = document.createElement('div');
        dayCell.textContent = day;

        const currentDateString = `${year}-${month}-${day}`;
        if (currentDateString === todayDateString) {
            dayCell.classList.add('today');
        }

        daysElement.appendChild(dayCell);
    }
}

// Event Listeners
prevMonthButton.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar(currentDate.getFullYear(), currentDate.getMonth());
});

nextMonthButton.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar(currentDate.getFullYear(), currentDate.getMonth());
});

// Initial Render
renderCalendar(currentDate.getFullYear(), currentDate.getMonth());

console.log("Calendar script executed and initialized!");