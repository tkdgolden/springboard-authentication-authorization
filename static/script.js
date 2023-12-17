document.addEventListener("DOMContentLoaded", () => {
    const updateButton = document.querySelector(".update");
    const fbId = updateButton.dataset.fbid;
    updateButton.parentElement.setAttribute('href', `/feedback/${fbId}/update`);
})