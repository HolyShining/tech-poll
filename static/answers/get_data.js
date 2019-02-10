var initialLoad = true;
all_stages = {};
json_data = null;
section = null;
page_id = null;
stage_id = null;
stages_count = null;
answered_stages = [];
answered = [];
questions_here = 0;
current_stages = [];
section_id = 0;
sections_count={};

window.fetch($('#get_data').attr("api"))
    .then(function(response){
        return response.json();
    }).then(function(json){
    json_data = json;
    filldata(section_id);
    for (let section_id = 0; section_id < json_data.sections.length; section_id++) {
        sections_count[json_data.sections[section_id].name] = json_data.stages.filter(function (obj) {
            return obj.section === json_data.sections[section_id].name;
        }).length;
    }
    push_data(json);
});

$(document).ready(function() {
    initialLoad = false;
});

function filldata(section_id) {
    section = json_data.sections[section_id].name;
    page_id = 1;
    for (let i = 0; i < json_data.stages.length; i++) {
        if (json_data.stages[i].section === section){
            current_stages.push({name: json_data.stages[i].name});
        }
    }
    stage_id = current_stages[page_id - 1].name;
    stages_count = current_stages.length;
}

function load_page(page){
    page_id = page;
    stage_id = current_stages[page_id - 1].name;
    push_data(json_data);
}

function load_section(id){
    console.log(all_stages);
    all_stages[section] = answered;
    section = json_data.sections[id].name;

    if (section in all_stages){
        answered = all_stages[section];
    } else {
        answered = [];
    }
    page_id = 1;
    current_stages = [];
    for (let i = 0; i < json_data.stages.length; i++) {
        if (json_data.stages[i].section === section){
            current_stages.push({name: json_data.stages[i].name});
        }
    }
    stage_id = current_stages[page_id - 1].name;
    stages_count = current_stages.length;
    load_page(1);
}

function push_data(json){
    clearData();
    for (number=0; number<json.sections.length; number++){
        document.querySelector('#sections').innerHTML +=
            render_sections(number, json.sections[number].name);
    }
    for(number=0; number<current_stages.length; number++){
        document.querySelector('.md-stepper-horizontal').innerHTML +=
            render_stages(number+1, current_stages[number].name);
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
                update_sections();
                if (page_id === stages_count && answered.length === stages_count){
                    $('#finish').attr('disabled', false);
                    $('#finish').tooltip('disable');
                }
                console.log(answered.length, current_stages.length);
                if (answered.length === current_stages.length){
                    document.querySelector('#next').setAttribute("value", "Next Section");
                    document.querySelector('#next').setAttribute("onclick", "nextSection();");
                }
            }
        }});
    if (page_id === 1){
        $('#previous').attr('disabled', true);
    } else {
        $('#previous').attr('disabled', false);
    }
    console.log(answered);

    if (page_id === current_stages.length || answered.length === current_stages.length){
        answered_stages.push(section_id);
        document.querySelector('#next').setAttribute("value", "Next Section");
        document.querySelector('#next').setAttribute("onclick", "nextSection();");
    } else {
        document.querySelector('#next').setAttribute("value", "Next");
        document.querySelector('#next').setAttribute("onclick", "nextPage();");
    }
    if ((page_id === current_stages.length || answered.length === current_stages.length) &&
        section === json_data.sections[json_data.sections.length-1].name){
        document.querySelector('#next').setAttribute("value", "Finish");
        document.querySelector('#next').setAttribute("onclick", "submitData();");
        document.querySelector('#next').setAttribute("id", "finish");
        document.querySelector('#finish').setAttribute("data-toggle", "tooltip");
        document.querySelector('#finish').setAttribute("data-placement", "tooltip");
        document.querySelector('#finish').setAttribute("title",
            "Please, fill up all grey sections!");
        $('#finish').attr('disabled', true);
    }
}

function update_sections() {
    sections_count[section] -= 1;
    document.querySelector('#sections').innerHTML = '';
    for (number=0; number<json_data.sections.length; number++){
        document.querySelector('#sections').innerHTML +=
            render_sections(number, json_data.sections[number].name);
    }
}

function getNumberOfStage(section){
    return json_data.stages.filter(function (obj) {
        return obj.section === section
    }).length;
}

function render_sections(id, name) {
    let badge = "<span class=\"badge badge-pill bg-light align-text-bottom\">"+sections_count[name]+"</span>\n";
    if (sections_count[name] < 1){
        badge = '';
    }
    const element = "<a class=\"nav-link\" href=\"#\" onclick='load_section("+parseInt(id)+")'>\n" +
        "            "+name+"\n" +
        badge +
        "        </a>";
    return element;
}


function render_stages(id, name){
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
    stage_id = current_stages[page_id-1].name;
    push_data(json_data);
}

function previousPage() {
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
    answered.push(page_id);
    page_id -= 1;
    stage_id = current_stages[page_id-1].name;
    push_data(json_data);
}

function nextSection() {
    clearData();
    current_stages = [];
    answered = [];
    section_id += 1;
    filldata(section_id);
    push_data(json_data);
}

function submitData() {
    let finalObj = {};
    const formData = $('form').serializeArray();
    for (index = 1; index < formData.length; index += 2) {
        try {
            sessionStorage.setItem(formData[index].name, formData[index].value);
            sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
        }
        catch (e) {
            null;
        }
    }

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
    let url = $('#get_data').attr("api").match(/.*\/(.*)$/);
    let csrfToken = document.cookie.replace('csrftoken=', '');
    http.open('POST', '/answers/' +url[url.length-1], true);
    http.setRequestHeader('Content-type', 'text');
    http.setRequestHeader('csrfmiddlewaretoken', csrfToken);

    console.log(JSON.stringify(finalObj));
    http.send(JSON.stringify(finalObj));
    http.onreadystatechange = function() {
        if (http.readyState == XMLHttpRequest.DONE && http.status == 200) {
            sessionStorage.clear();
            window.location.href = "/dash/user";
        }
    }
}

function clearData(){
    document.querySelector('#sections').innerHTML = '';
    document.querySelector('#question-holder').innerHTML = '';
    document.querySelector('.md-stepper-horizontal').innerHTML = '';
    questions_here = 0;
}