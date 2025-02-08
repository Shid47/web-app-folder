document.getElementById("no-button").addEventListener("mouseover", function() {
    let x = Math.random() * (window.innerWidth - 100);
    let y = Math.random() * (window.innerHeight - 50);
    this.style.left = x + "px";
    this.style.top = y + "px";
});
