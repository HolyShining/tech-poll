json_data = null;

// States of objects on the screen
var page_state = {
    all_stages: {},
    section : null,
    page_id : null,
    stage_id : null,
    stages_count : null,
    answered_stages : [],
    answered : [],
    questions_here : 0,
    current_stages : [],
    section_id : 0,
    sections_count : {},
};

// Load data from QuestionsAPI and get all sections
window.fetch($('#get_data').attr("api"))
    .then(function(response){
        return response.json();
    }).then(function(json){
    json_data = json;
    filldata(page_state.section_id);
    for (let section_id = 0; section_id < json_data.sections.length; section_id++) {
        page_state.sections_count[json_data.sections[section_id].name] = json_data.stages.filter(function (obj) {
            return obj.section === json_data.sections[section_id].name;
        }).length;
    }
    updatePage();
});

// Init start data
function filldata(section_id) {
    page_state.section = json_data.sections[section_id].name;
    page_state.page_id = 1;
    for (let i = 0; i < json_data.stages.length; i++) {
        if (json_data.stages[i].section === page_state.section){
            page_state.current_stages.push({name: json_data.stages[i].name});
        }
    }
    page_state.stage_id = page_state.current_stages[page_state.page_id - 1].name;
    page_state.stages_count = page_state.current_stages.length;
}

// Render all data from JSON and add event for filling form
function updatePage(){
    clearData();
    for (number=0; number<json_data.sections.length; number++){
        document.querySelector('#sections').innerHTML +=
            render_sections(number, json_data.sections[number].name);
    }
    for(number=0; number<page_state.current_stages.length; number++){
        document.querySelector('.md-stepper-horizontal').innerHTML +=
            render_stages(number+1, page_state.current_stages[number].name);
    }
    for(number=0; number<json_data.questions.length; number++){
        document.querySelector('#question-holder').innerHTML +=
            render_questions(number,
                json_data.questions[number].name,
                json_data.questions[number].stages,
                json_data.questions[number].hint,
                page_state.stage_id);
    }
    let answer = 0;
    // If form is filled:
    // 1: Push data to session storage
    // 2: Update badge at section nav
    // 3: Check button state
    $("input[name$='_l']").on("change", function(){
        if($("input[name$='_l']").is(":checked") === true){
            answer += 1;
            if(page_state.questions_here === answer){
                $("#"+page_state.page_id+".md-step").addClass('active');
                if(!page_state.answered.includes(page_state.page_id)){
                    page_state.answered.push(page_state.page_id);
                }

                saveAnswers();
                update_sections();

                if (page_state.page_id === page_state.stages_count && page_state.answered.length === page_state.stages_count){
                    $('#finish')
                        .attr('disabled', false)
                        .tooltip('disable');
                }
                if (page_state.answered.length === page_state.current_stages.length){
                    document.querySelector('#next').setAttribute("value", "Next Section");
                    document.querySelector('#next').setAttribute("onclick", "nextSection();");
                }
            }
        }});
    changeButtonState();
}

// Delete all data from screen
function clearData(){
    document.querySelector('#sections').innerHTML = '';
    document.querySelector('#question-holder').innerHTML = '';
    document.querySelector('.md-stepper-horizontal').innerHTML = '';
    page_state.questions_here = 0;
}

// Save user answers in session storage
function saveAnswers() {
    const formData = $('form').serializeArray();
    if (formData.length !== page_state.questions_here*2-1) {
        for (index = 1; index < formData.length; index += 2) {
            try {
                sessionStorage.setItem(formData[index].name, formData[index].value);
                sessionStorage.setItem(formData[index + 1].name, formData[index + 1].value);
                if (!page_state.answered.includes(page_state.page_id)) {
                    page_state.answered.push(page_state.page_id);
                }
            } catch (e) {
                null;
            }
        }
    }
}

// Change button state depends of action on screen
function changeButtonState() {
    if (page_state.page_id === 1){
        $('#previous').attr('disabled', true);
    } else {
        $('#previous').attr('disabled', false);
    }

    if (page_state.page_id === page_state.current_stages.length || page_state.answered.length === page_state.current_stages.length){
        page_state.answered_stages.push(page_state.section_id);
        document.querySelector('#next').setAttribute("value", "Next Section");
        document.querySelector('#next').setAttribute("onclick", "nextSection();");
    } else {
        document.querySelector('#next').setAttribute("value", "Next");
        document.querySelector('#next').setAttribute("onclick", "nextPage();");
    }
    if ((page_state.page_id === page_state.current_stages.length || page_state.answered.length === page_state.current_stages.length) &&
        page_state.section === json_data.sections[json_data.sections.length-1].name){
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