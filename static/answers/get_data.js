json_data = null;

window.fetch('/api/questions')
    .then(function(response){
        return response.json();
    }).then(function(json){
    push_data(json);
    json_data = json;
});

var initialLoad = true;

$(document).ready(function() {
    console.log('load');
    page_id = 1;
    stage_id = 'Engineering Management';
    initialLoad = false;
});

// if (sessionStorage.getItem('pageID') && sessionStorage.getItem('stageID')) {
//     page_id = sessionStorage.getItem('pageID');
//     stage_id = sessionStorage.getItem('stageID');
// }

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
                stage_id);
    }
}

function render_stages(id, name, current_id){
    let isActive = '';
    if (id<=current_id){
        isActive = "active";
    }
    else{
        isActive = "";
    }
    const element = "            <div class=\"md-step "+isActive+"\">\n" +
        "        <div class=\"md-step-circle\"><span>"+id+"</span></div>\n" +
        "        <div class=\"md-step-title\">"+name+"</div>\n" +
        "    <div class=\"md-step-bar-left\"></div>\n" +
        "    <div class=\"md-step-bar-right\"></div>\n" +
        "</div>\n" +
        "<div class=\"md-step-bar-left\"></div>\n" +
        "<div class=\"md-step-bar-right\"></div>";

    return element;
}

function render_questions(id, name, stage, current_id){
    if (stage != current_id){
        return '';
    }
    const element = "            <tr>\n" +
        "                <td>"+ name +"</td>\n" +
        "                <td><div class=\"btn-group btn-group-toggle\" data-toggle=\"buttons\">\n" +
        "                    <label class=\"btn btn-light\">\n" +
        "                        <input type=\"radio\" name=\""+name+"_l\" value=\"Yes\"> l\n" +
        "                    </label>\n" +
        "                    <label class=\"btn btn-light\">\n" +
        "                        <input type=\"radio\" name=\""+name+"_l\" value=\"No\"> 0\n" +
        "                    </label>\n" +
        "                </div></td>\n" +
        "                <td><div class=\"dropdown\">\n" +
        "                    <select class=\"custom-select\" name=\""+name+"_g\">\n" +
        "                        <option class=\"dropdown-item\" value=\"None\">None</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Beginner\">Beginner</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Intermediate\">Intermediate</option>\n" +
        "                        <option class=\"dropdown-item\" value=\"Master\">Master</option>\n" +
        "                    </select>\n" +
        "                </div></td>\n" +
        "            </tr>";
    return element;
}

function submitted() {
    const formData = $('form').serializeArray();
    console.log(formData);
    for(index=1; index<formData.length; index+=2){
        console.log(formData[index].name, formData[index].value);
        sessionStorage.setItem(formData[index].name, formData[index].value);
        console.log(formData[index+1].name, formData[index+1].value);
        sessionStorage.setItem(formData[index+1].name, formData[index+1].value);
    }
    page_id += 1;
    stage_id = 'Requirements';
    push_data(json_data);
}

function clearData(){
    document.querySelector('#question-holder').innerHTML = '';
    document.querySelector('.md-stepper-horizontal').innerHTML = '';
}
