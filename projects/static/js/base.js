const projects__filter = document.querySelector('.projects .projects__filter');
const checkbox_inputs = document.querySelectorAll('.projects .item__checkbox_input');

if(projects__filter){
    projects__filter.addEventListener('click', (ev)=>{
        if(ev.target.classList.contains('item__checkbox_input')){
            let categories = {};
            for(let inp of checkbox_inputs){
                let checked_input = false;
                if(inp.checked){
                    checked_input = true;
                }
                categories[String(inp.dataset.setId)] = {'id': String(inp.dataset.setId), 'checked': checked_input,}
            }
            const projects__content = document.querySelector('.projects .projects__content');
            const projects_load = document.querySelector('.projects .projects__load');
            projects_load.style.display = 'block';
            projects__content.innerHTML = '';
            fetch('/filter_fetch/',{
                method: 'POST',
                headers: {'X-CSRFToken': csrf_token},
                mode: 'same-origin',
                body: JSON.stringify(categories),
            })
            .then(response => response.json())
            .then(result => {
                let template_projects = ``;
                for(let proj of result['projects']){
                    let winner = '<div></div>';
                    if(proj['winner'] === 1 || proj['winner'] === 2 || proj['winner'] === 3){
                        winner = '<img src="/static/images/winner.png" alt="Победитель" class="winner_image">';
                    }
                    let tpl_proj = `
                        <a class="card" href="${proj['url']}">
                            ${winner}         
                            <img src="${proj['photo']}" alt="${proj['name']}" class="card__image">
                            <h3 class="card__title">${proj['name']}</h3>
                            <p class="card__description">
                                ${proj['description']} ...
                            </p>
                            <p class="card__team">${proj['name_team']}</p>
                        </a>
                    `;
                    template_projects += tpl_proj;
                }
                projects_load.style.display = 'none';
                projects__content.innerHTML = template_projects;
            })
            .catch(error => console.log(error))
        }
    })
}

const gamburger_icon = document.querySelector('.header .gamburger-icon');
const close_icon = document.querySelector('.header .close-icon');
const header_content = document.querySelector('.header__content');
const overlay_header = document.querySelector('.header .overlay');


gamburger_icon.addEventListener('click', ()=>{
    header_content.classList.add('header__content_transition');
    header_content.classList.remove('header__content_transition_out');
    overlay_header.style.display = 'block';
})

close_icon.addEventListener('click', ()=>{
    overlay_header.style.display = 'none';
    header_content.classList.remove('header__content_transition');
    header_content.classList.add('header__content_transition_out');
})