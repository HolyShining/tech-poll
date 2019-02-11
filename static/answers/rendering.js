// Render sections component
function render_sections(id, name) {
    let badge = "<span class=\"badge badge-pill bg-light align-text-bottom\">"+page_state.sections_count[name]+"</span>\n";
    if (page_state.sections_count[name] < 1){
        badge = '';
    }
    const element = "<a class=\"nav-link\" href=\"#\" onclick='load_section("+parseInt(id)+")'>\n" +
        "            "+name+"\n" +
        badge +
        "        </a>";
    return element;
}

// Render stages component
function render_stages(id, name){
    let isActive = '';
    if (page_state.answered.includes(id)){
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

// Render questions table component
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
    page_state.questions_here += 1;
    return element;
}

// Render dropdown component
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