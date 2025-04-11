// Smooth scrolling for navigation links
document.addEventListener('DOMContentLoaded', function () {
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            window.location.href = targetId; // For Django URL navigation
        });
    });

    // Toast notification (for success messages)
    function showToast(message, type = 'success') {
        const toastContainer = document.createElement('div');
        toastContainer.className = `toast align-items-center text-white bg-${type} border-0 position-fixed bottom-0 end-0 m-3`;
        toastContainer.setAttribute('role', 'alert');
        toastContainer.setAttribute('aria-live', 'assertive');
        toastContainer.setAttribute('aria-atomic', 'true');
        toastContainer.innerHTML = `
            <div class="d-flex">
                <div class="toast-body">
                    ${message}
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        `;
        document.body.appendChild(toastContainer);
        const toast = new bootstrap.Toast(toastContainer);
        toast.show();
    }

    // Expose showToast to global scope for use in templates
    window.showToast = showToast;
});