// Load page by selected id
function load_page(page){
    page_state.page_id = page;
    page_state.stage_id = page_state.current_stages[page_state.page_id - 1].name;
    updatePage();
}

// Load section by selected id
function load_section(id){
    page_state.all_stages[page_state.section] = page_state.answered;
    page_state.section = json_data.sections[id].name;

    if (page_state.section in page_state.all_stages){
        page_state.answered = page_state.all_stages[page_state.section];
    } else {
        page_state.answered = [];
    }
    page_state.page_id = 1;
    page_state.current_stages = [];
    for (let i = 0; i < json_data.stages.length; i++) {
        if (json_data.stages[i].section === page_state.section){
            page_state.current_stages.push({name: json_data.stages[i].name});
        }
    }
    page_state.stage_id = page_state.current_stages[page_state.page_id - 1].name;
    page_state.stages_count = page_state.current_stages.length;
    load_page(1);
}

// Update badges at sections nav
function update_sections() {
    page_state.sections_count[page_state.section] -= 1;
    document.querySelector('#sections').innerHTML = '';
    for (number=0; number<json_data.sections.length; number++){
        document.querySelector('#sections').innerHTML +=
            render_sections(number, json_data.sections[number].name);
    }
}
