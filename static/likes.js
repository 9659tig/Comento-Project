function sendRequest(content_id) {
    var httpRequest = new XMLHttpRequest();

    httpRequest.onreadystatechange = function() {
        if (httpRequest.readyState == XMLHttpRequest.DONE && httpRequest.status == 200) {
            document.getElementById("text").innerHTML = httpRequest.responseText;
        }
    };
    httpRequest.open('GET', "/like/" + content_id + "/", true);
    httpRequest.send();
}