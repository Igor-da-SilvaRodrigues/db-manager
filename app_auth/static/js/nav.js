// // Navbar schema's tables dropdown
const nav_schema_buttons = document.getElementsByClassName('schema-button');

Array.from(nav_schema_buttons).forEach((button) => {
    button.addEventListener('click', () => {
        button.innerText = button.innerText === '+' ? '-' : '+';
        button.classList.toggle('active');
        const droplist = document.getElementById(button.getAttribute('related-drop-list-id'));
        droplist.classList.toggle('active');
    });
});

// Navbar table's columns dropdown
const nav_table_buttons = document.getElementsByClassName('table-button');

Array.from(nav_table_buttons).forEach((button) => {
    button.addEventListener('click', () => {
        button.innerText = button.innerText === '+' ? '-' : '+';
        button.classList.toggle('active');
        const droplist = document.getElementById(button.getAttribute('related-drop-list-id'));
        droplist.classList.toggle('active');
    });
});
