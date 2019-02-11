// Next page button
function nextPage() {
    saveAnswers();
    page_state.page_id += 1;
    page_state.stage_id = page_state.current_stages[page_state.page_id-1].name;
    updatePage();
}

// Previous page button
function previousPage() {
    saveAnswers();
    answered.push(page_state.page_id);
    page_state.page_id -= 1;
    page_state.stage_id = page_state.current_stages[page_state.page_id-1].name;
    updatePage();
}

// Load next section button
function nextSection() {
    page_state.current_stages = [];
    page_state.answered = [];
    page_state.section_id += 1;
    page_state.all_stages[page_state.section] = page_state.answered;
    page_state.section = json_data.sections[page_state.section_id].name;

    if (page_state.section in page_state.all_stages){
        page_state.answered = page_state.all_stages[page_state.section];
    } else {
        page_state.answered = [];
    }
    console.log(page_state.answered);
    clearData();
    filldata(page_state.section_id);
    updatePage();
}