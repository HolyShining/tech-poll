// Serialize session storage to JSON file
function submitData() {
    let finalObj = {};
    saveAnswers();

    for (i=0; i<json_data.questions.length; i++){
        if (sessionStorage.getItem(json_data.questions[i].name+'_l') == null){
            sessionStorage.setItem(json_data.questions[i].name+'_l', 'None');
        }
        finalObj[json_data.questions[i].name] = {
            'Like to do': sessionStorage.getItem(json_data.questions[i].name+'_l'),
            'Self-estimate': sessionStorage.getItem(json_data.questions[i].name+'_g'),
        }
    }
    sendDataToServer(finalObj);
}

// Open HTTP request, send JSON and redirect to dashboard
function sendDataToServer(json){
    let http = new XMLHttpRequest();
    let url = $('#get_data').attr("api").match(/.*\/(.*)$/);
    let csrfToken = document.cookie.replace('csrftoken=', '');
    http.open('POST', '/answers/' +url[url.length-1], true);
    http.setRequestHeader('Content-type', 'text');
    http.setRequestHeader('csrfmiddlewaretoken', csrfToken);

    http.send(JSON.stringify(json));
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE && http.status == 200) {
            sessionStorage.clear();
            window.location.href = "/dash/user";
        }
    }
}