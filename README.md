# Команда “Пираты”

### Идея - Галерея завершенных проектов участников хакатонов

- <a href="https://slides.com/serg777/copy-of">Презентация проекта</a>
- <a href="http://hackaton3.magomed487.beget.tech/">Прототип</a>

На сайте хакатоны.рус создать новый раздел «Проекты участников хакатонов». В этом разделе будут завершенные проекты всех участников всех хакатонов, а проекты победителей будут визуально выделяться. Посетители сайта смогут просматривать галерею, фильтруя проекты по категориям, технологическим стекам или другим критериям.

<img src="https://a.radikalfoto.host/2024/05/26/23454354.jpeg" alt="23454354.jpeg" border="0" />


**Стейкхолдеры, на интересы которых влияет идея:**

- Начинающие специалисты без опыта участия в хакатонах.
- Специалисты с опытом участия в хакатонах.
- Владельцы платформы [хакатоны.рус](http://хакатоны.рус)

### Архитектура решения

1. **Ввод данных**

Капитан команды пошагово заполняет информацию о проекте в своем профиле участника хакатона через раздел “Решения”, вкладку “Финальное решение”, в новом блоке “Проект”. Он указывает:

- Цель и функциональность проекта.
- Используемые технологии (в виде тегов для удобного поиска и категоризации).
- Проблемы, с которыми столкнулась команда.
- Достижения, которыми гордится команда.
- Скриншоты и презентации.
- Состав команды и роли.
- Что будет дальше с проектом.
- Планы на будущее по проекту.
- Ссылка на репозиторий GitHub.

2. **Обработка данных — модерация и обратная связь**

После отправки проекты попадают в очередь на модерацию. Модераторы проверяют каждый проект и предоставляют обратную связь в формате комментариев. Команды могут пересмотреть свои работы в течение двух недель на основе этих комментариев, прежде чем получить окончательное одобрение.

3. **Вывод данных**

Одобренные проекты отображаются в разделе «Проекты участников хакатона». Представлены следующие возможности:

- Варианты фильтрации по типу хакатона, стеку технологий и другим критериям.
- Отдельные страницы проектов с подробной информацией о них.
- Специальное выделение проектов победителей.

### Модель IDEF + Swim lane
<img src="https://a.radikalfoto.host/2024/05/26/KOMANDA-PIRATY-KAKATON.jpeg" alt="KOMANDA-PIRATY-KAKATON.jpeg" border="0" />

**Преимущества внедрения:**

- Демонстрация проектов позволит участникам хакатона представить свою работу широкой аудитории, включая потенциальных работодателей.
- Признание усилий участников хакатона повысит их моральный дух и стимулирует дальнейшее участие в будущих хакатонах.
- Специалисты, не имеющие опыта участия в хакатонах, смогут учиться на примерах успешных проектов.
- **Привлечение участников и спонсоров:** Галерея проектов служит подтверждением качества и результативности хакатонов, привлекая больше участников и спонсоров в будущие мероприятия.
