const web_server = new WebSocket("ws://127.0.0.1:5678/");
var message;
console.log(web_server);

web_server.onmessage = function(event){
    console.log("[Message received from server]", event.data)
};

function send(){
    message = document.getElementById("test_entry").value;
    try {
        web_server.send(message);
    } catch {

    }
    }
    console.log("Msg sent ", message);