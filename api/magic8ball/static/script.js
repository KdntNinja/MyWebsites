document.querySelector("form").addEventListener("submit", function(e) {
    e.preventDefault();
    let elem = document.getElementById("myBar");
    let width = 0;
    let id = setInterval(frame, 10);

    function frame() {
        if (width >= 100) {
            clearInterval(id);
            e.target.submit();
        } else {
            width++;
            elem.style.width = width + "%";
        }
    }
});