// Live Time & Date
function updateTime() {
    var now = new Date();
    var time = now.toLocaleTimeString();
    var date = now.toDateString();
    document.getElementById('liveClock').innerHTML = time + '<br>' + date;
}
updateTime();
setInterval(updateTime, 1000);