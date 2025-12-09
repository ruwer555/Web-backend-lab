function fillFilmList() {
    fetch('/lab7/rest-api/films/')
    .then(function (data) {
        return data.json();
    })
    .then(function (films) {
        let tbody = document.getElementById('film-list');
        tbody.innerHTML = '';
        
        for(let i = 0; i < films.length; i++) {
            let currentId = i;
            let displayTitle = films[i].title_ru; 

            let tr = document.createElement('tr');

            // Русское название
            let tdTitleRus = document.createElement('td');
            tdTitleRus.innerText = films[i].title_ru;

            // Оригинальное название (курсив + скобки)
            let tdTitle = document.createElement('td');
            let originalTitle = films[i].title;
            
            if (originalTitle && originalTitle !== films[i].title_ru) {
                tdTitle.innerHTML = `<i>(${originalTitle})</i>`;
            } else {
                tdTitle.innerHTML = '<span style="color: #ccc;">—</span>'; 
            }

            let tdYear = document.createElement('td');
            tdYear.innerText = films[i].year;

            let tdActions = document.createElement('td');

            let editButton = document.createElement('button');
            editButton.innerText = 'Редактировать';
            editButton.onclick = function() {
                editFilm(currentId);
            }

            let delButton = document.createElement('button');
            delButton.innerText = 'Удалить';
            delButton.className = 'del-btn';
            delButton.onclick = function() {
                deleteFilm(currentId, displayTitle);
            };

            tdActions.append(editButton);
            tdActions.append(delButton);

            tr.append(tdTitleRus);
            tr.append(tdTitle);
            tr.append(tdYear);
            tr.append(tdActions);

            tbody.append(tr);
        }
    });
}

function deleteFilm(currentId, currentTitle) {
    if(!confirm(`Вы точно хотите удалить фильм "${currentTitle}"?`)) {
        return;
    }
    
    fetch(`/lab7/rest-api/films/${currentId}`, {method: 'DELETE'})
    .then(function() {
        fillFilmList();
    });
}

function showModal() {
    document.getElementById('description-error').innerText = '';
    document.querySelector('.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}
    
function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    document.getElementById('description-error').innerText = '';
    showModal();
}

function sendFilm() {
    const id = document.getElementById('id').value;
    const film = {
        title: document.getElementById('title').value,
        title_ru: document.getElementById('title-ru').value,
        year: document.getElementById('year').value,
        description: document.getElementById('description').value
    }

    let url = '/lab7/rest-api/films/';
    let method = 'POST';

    if(id !== '') {
        url = `/lab7/rest-api/films/${id}`;
        method = 'PUT';
    }

    fetch(url, {
        method: method,
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(film)
    })
    .then(function(resp) {
        if(resp.ok) {
            fillFilmList();
            hideModal();
            return {};
        }
        return resp.json();
    })
    .then(function(errors) {
        if(errors && errors.description)
            document.getElementById('description-error').innerText = errors.description;
    });
}

function editFilm(currentId) {
    fetch(`/lab7/rest-api/films/${currentId}`)
    .then(function (data) {
        return data.json();
    })
    .then(function (film) {
        document.getElementById('id').value = currentId;
        document.getElementById('title').value = film.title;
        document.getElementById('title-ru').value = film.title_ru;
        document.getElementById('year').value = film.year;
        document.getElementById('description').value = film.description;
        document.getElementById('description-error').innerText = '';
        showModal();
    });
}

fillFilmList();
