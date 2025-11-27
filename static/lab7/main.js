function fillFilmList() {
    console.log('Функция вызвана');
    
    fetch('/lab7/rest-api/films/')
    .then(function (data) {
        console.log('Ответ получен');
        return data.json();
    })
    .then(function (films) {
        console.log('Фильмы:', films); // ← посмотри что здесь
        console.log('Количество фильмов:', films.length);
        
        let tbody = document.getElementById('film-list');
        console.log('tbody:', tbody); // ← убедись что элемент найден
        
        tbody.innerHTML = '';
        
        for(let i = 0; i < films.length; i++) {
            console.log('Добавляем фильм:', films[i].title); // ← смотри в консоли
            
            let tr = document.createElement('tr');

            let tdTitle = document.createElement('td');
            let tdTitleRus = document.createElement('td');
            let tdYear = document.createElement('td');
            let tdActions = document.createElement('td');

            // Заполняем данные
            tdTitle.innerText = films[i].title == films[i].title_ru ? '' : films[i].title;
            tdTitleRus.innerText = films[i].title_ru;
            tdYear.innerText = films[i].year;

            // Добавляем ячейки в строку
            tr.appendChild(tdTitle);
            tr.appendChild(tdTitleRus);
            tr.appendChild(tdYear);
            tr.appendChild(tdActions);

            // Добавляем строку в таблицу
            tbody.appendChild(tr);

            // Кнопки
            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';

            // Добавляем кнопки в ячейку действий
            tdActions.appendChild(editButton);
            tdActions.appendChild(delButton);
        }
        console.log('Таблица заполнена');
    })
    .catch(function(error) {
        console.error('Ошибка:', error);
    });
}

