window.fetch('/api/questions')
    .then(function(response){
        return response.json();
    }).then(function(json){
    push_data(json);
});

function push_data(json){
    console.log(json);
    document.querySelector('#name-course').innerHTML = json.department;
    for(number=0; number<json.questions.length; number++){
        document.querySelector('#questions-course').innerHTML += json.questions[number].name+'<br/>';
    }
    for(number=0; number<json.stages.length; number++){
        document.querySelector('#stages-course').innerHTML += json.stages[number].name+'<br/>';
    }
    for(number=0; number<json.sections.length; number++){
        document.querySelector('#sections-course').innerHTML += json.sections[number].name+'<br/>';
    }
}