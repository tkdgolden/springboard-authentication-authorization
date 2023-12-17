/* 
 * wait until DOM is loaded to do anything
 */
document.addEventListener("DOMContentLoaded", () => {
    // add correct link to update feedback buttons
    const updateButtons = document.querySelectorAll(".update");
    updateButtons.forEach(function (cv) {
        const fbId = cv.dataset.fbid;
        cv.parentElement.setAttribute('href', `/feedback/${fbId}/update`);
    });

    // add correct link to delete feedback buttons
    const deleteButtons = document.querySelectorAll(".delete");
    deleteButtons.forEach(function (cv) {
        const fbId = cv.dataset.fbid;
        cv.parentElement.setAttribute('href', `/feedback/${fbId}/delete`);
    });
})