var initialLoad = true;
json_data = null;
section = null;
page_id = null;
stage_id = null;
stages_count = null;
answered = [];

window.fetch($('#get_data').attr("api"))
    .then(function(response){
        return response.json();
    }).then(function(json){
    json_data = json;
    filldata();
    push_data(json);
});

$(document).ready(function() {
    initialLoad = false;
});

function filldata() {
    if (sessionStorage.getItem('pageID') && sessionStorage.getItem('stageID')) {
        section = 'Activity';
        page_id = sessionStorage.getItem('pageID');
        stage_id = sessionStorage.getItem('stageID');
    } else {
        section = 'Activity';
        page_id = 1;
        stage_id = json_data.stages[page_id - 1].name;
        stages_count = json_data.stages.length;
    }
}

function load_page(page){
    page_id = page;
    stage_id = json_data.stages[page_id - 1].name;
    push_data(json_data);
}

function push_data(json){
    clearData();
    for(number=0; number<json.stages.length; number++){
        document.querySelector('.md-stepper-horizontal').innerHTML +=
        render_stages(number+1, json.stages[number].name, page_id);
    }
    for(number=0; number<json.questions.length; number++){
        document.querySelector('#question-holder').innerHTML +=
            render_questions(number,
                json.questions[number].name,
                json.questions[number].stages,
                json.questions[number].hint,
                stage_id);
    }
    if (page_id === 1){
        $('#previous').attr('disabled', true);
    } else {
        $('#previous').attr('disabled', false);
    }
}

function render_stages(id, name, current_id){
    const element = "            <div class=\"md-step\">\n" +
        "        <div class=\"md-step-circle\"><span>"+id+"</span></div>\n" +
        "<a href=\"#\" onclick=\"load_page("+id+");\">"+
        "        <div class=\"md-step-title\">"+name+"</div>\n" +
        "    <div class=\"md-step-bar-left\"></div>\n" +
        "    <div class=\"md-step-bar-right\"></div>\n" +
        "</div>\n" +
        "<div class=\"md-step-bar-left\"></div>\n" +
        "<div class=\"md-step-bar-right\"></div>";

    return element;
}

function render_questions(id, name, stage, hint, current_id){
    if (stage != current_id){
        return '';
    }

    const element = "<tr>\n" +
        "                <td data-toggle=\"tooltip\" title=\""+ hint +"\">"+ name +"</td>\n" +
        "                <td><div class=\"btn-group btn-group-toggle\" data-toggle=\"buttons\">\n" +
        "                    <label class=\"btn btn-light "+ (sessionStorage.getItem(name+'_l') === 'Yes' && 'active')  +"\">\n" +
        "                        <input type=\"radio\" name=\""+name+"_l\" value=\"Yes\""+ (sessionStorage.getItem(name+'_l') === 'Yes' && 'checked') +"> l\n" +
        "                    </label>\n" +
        "                    <label class=\"btn btn-light "+ (sessionStorage.getItem(name+'_l') === 'No' && 'active') +"\">\n" +
        "                        <input type=\"radio\" name=\""+name+"_l\" value=\"No\""+ (sessionStorage.getItem(name+'_l') === 'No' && 'checked')  +"> 0\n" +
        "                    </label>\n" +
        "                </div></td>\n" +
        "                <td><div class=\"dropdown\">\n" +
        "                    <select class=\"custom-select\" name=\""+name+"_g\"\">\n" +
        "                        <option class=\"dropdown-item\" value=\"None\""+ (sessionStorage.getItem(name+'_g') === 'None' && 'selected') +">None</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Beginner\""+ (sessionStorage.getItem(name+'_g') === 'Beginner' && 'selected') +">Beginner</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Intermediate\""+ (sessionStorage.getItem(name+'_g') === 'Intermediate' && 'selected') +">Intermediate</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Master\""+ (sessionStorage.getItem(name+'_g') === 'Master' && 'selected') +">Master</option>\n" +
        "                    </select>\n" +
        "                </div></td>\n" +
        "            </tr>";
    return element;
}

function nextPage() {
    const formData = $('form').serializeArray();
    for (index = 1; index < formData.length; index += 2) {
        try {
            sessionStorage.setItem(formData[index].name, formData[index].value);
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
        catch (e) {
            sessionStorage.setItem(formData[index].name, 'None');
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
    }
    answered.push(page_id);
    page_id += 1;
    if (answered.length == stages_count-2){
        document.querySelector('#next').setAttribute("value", "Finish");
        document.querySelector('#next').setAttribute("onclick", "submitData();");
    }
    stage_id = json_data.stages[page_id-1].name;
    push_data(json_data);
}

function previousPage() {
    const formData = $('form').serializeArray();
    for (index = 1; index < formData.length; index += 2) {
        try {
            sessionStorage.setItem(formData[index].name, formData[index].value);
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
        catch (e) {
            sessionStorage.setItem(formData[index].name, 'None');
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
    }
    answered.push(page_id);
    page_id -= 1;
    stage_id = json_data.stages[page_id-1].name;
    push_data(json_data);
}

function submitData() {
    let finalObj = {};
    for (i=0; i<json_data.questions.length; i++){
        if (sessionStorage.getItem(json_data.questions[i].name+'_l') == null){
            sessionStorage.setItem(json_data.questions[i].name+'_l', 'None');
        }
        finalObj[json_data.questions[i].name] = {
            'Like to do': sessionStorage.getItem(json_data.questions[i].name+'_l'),
            'Self-estimate': sessionStorage.getItem(json_data.questions[i].name+'_g'),
        }
    }

    let http = new XMLHttpRequest();
    let url = '/answers/';
    let csrfToken = document.cookie.replace('csrftoken=', '');
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'text');
    http.setRequestHeader('csrfmiddlewaretoken', csrfToken);


    http.send(JSON.stringify(finalObj));
    console.log(JSON.stringify(finalObj));
    window.location.href = "/dash/user";
}

function clearData(){
    document.querySelector('#question-holder').innerHTML = '';
    document.querySelector('.md-stepper-horizontal').innerHTML = '';
}