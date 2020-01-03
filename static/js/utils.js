function toggleSidebar() {
    if (document.getElementById("sidebar-toggle").checked) {
        document.getElementById("sidebar").classList.remove('closed');

    } else {
        document.getElementById("sidebar").classList.add('closed');
    }
}