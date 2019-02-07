var initialLoad = true;
json_data = null;
section = null;
page_id = null;
stage_id = null;
stages_count = null;
answered = [];
questions_here = 0;

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
            render_stages(number+1, json.stages[number].name, section);
    }
    for(number=0; number<json.questions.length; number++){
        document.querySelector('#question-holder').innerHTML +=
            render_questions(number,
                json.questions[number].name,
                json.questions[number].stages,
                json.questions[number].hint,
                stage_id);
    }
    let answer = 0;
    $("input[name$='_l']").on("change", function(){
        if($("input[name$='_l']").is(":checked") == true){
            answer += 1;
            if(questions_here == answer){
                $("#"+page_id+".md-step").addClass('active');
                if(!answered.includes(page_id)){
                    answered.push(page_id);
                }
                if (page_id === stages_count && answered.length === stages_count){
                    $('#finish').attr('disabled', false);
                    $('#finish').tooltip('disable');
                }
            }
        }});
    if (page_id === 1){
        $('#previous').attr('disabled', true);
    } else {
        $('#previous').attr('disabled', false);
    }
    console.log(render_select('Python'));
}

function render_stages(id, name, current_section){
    if (section !== current_section){
        return '';
    }
    let isActive = '';
    if (answered.includes(id)){
        isActive = 'active';
    }
    const element = "            <div class=\"md-step "+isActive+"\" id=\""+id+"\">\n" +
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
                         render_select(name)+
        "                </div></td>\n" +
        "            </tr>";
    questions_here += 1;
    return element;
}

function render_select(name){
        let element ="                    <select class=\"custom-select\" name=\""+name+"_g\"\">\n";
        let options = '';
        for (grade = 0;grade<json_data.grades.length; grade++){
            options += "<option class=\"dropdown-item\" value=\""+
                json_data.grades[grade].name +
                "\""+ (sessionStorage.getItem(name+'_g') === json_data.grades[grade].name && 'selected') +">" +
                json_data.grades[grade].name +
                "</option>\n";
        }
        let ending = "</select>\n";
        return element + options + ending;
}

function nextPage() {
    const formData = $('form').serializeArray();
    if (formData.length !== questions_here*2-1) {
        for (index = 1; index < formData.length; index += 2) {
            try {
                sessionStorage.setItem(formData[index].name, formData[index].value);
                sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
                if (!answered.includes(page_id)) {
                    answered.push(page_id);
                }
            } catch (e) {
                null;
            }
        }
    }
    page_id += 1;
    if (page_id === stages_count){
        document.querySelector('#next').setAttribute("value", "Finish");
        document.querySelector('#next').setAttribute("onclick", "submitData();");
        document.querySelector('#next').setAttribute("id", "finish");
        document.querySelector('#finish').setAttribute("data-toggle", "tooltip");
        document.querySelector('#finish').setAttribute("data-placement", "tooltip");
        document.querySelector('#finish').setAttribute("title",
            "Please, fill up all grey sections!");
        $('#finish').attr('disabled', true);
    }
    stage_id = json_data.stages[page_id-1].name;
    push_data(json_data);
}

function previousPage() {
    const formData = $('form').serializeArray();
    console.log(formData);
    for (index = 1; index < formData.length; index += 2) {
        try {
            sessionStorage.setItem(formData[index].name, formData[index].value);
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
        catch (e) {
            null;
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
    let url = '/answers/1';
    let csrfToken = document.cookie.replace('csrftoken=', '');
    http.open('POST', url, true);
    http.setRequestHeader('Content-type', 'text');
    http.setRequestHeader('csrfmiddlewaretoken', csrfToken);


    console.log(JSON.stringify(finalObj));
    http.send(JSON.stringify(finalObj));
    // window.location.href = "/dash/user";
}

function clearData(){
    document.querySelector('#question-holder').innerHTML = '';
    document.querySelector('.md-stepper-horizontal').innerHTML = '';
    questions_here = 0;
}