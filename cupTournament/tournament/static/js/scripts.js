// Toggling dark/light theme mode
const htmlTag = document.getElementById('html');
const toggleTheme = document.getElementById('toggle-theme');
const toggleInput = document.getElementById('toggle-theme');

if (localStorage.getItem('theme') !== null) {
  htmlTag.classList.add('dark');
  toggleInput.checked = true;
} else {
  htmlTag.classList.remove('dark');
  toggleInput.checked = false;
}
toggleTheme.addEventListener('click', function () {
  htmlTag.classList.toggle('dark');
  console.log(htmlTag);
  if (htmlTag.classList.contains('dark')) {
    localStorage.setItem('theme', 'dark');
  } else {
    localStorage.removeItem('theme');
  }
});