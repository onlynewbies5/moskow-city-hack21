# moskow-city-hack21
Командный репозиторий для проекта

# 1. Описание модулей
Отдельные модули представлены, как отдельные тетрадки Jupyter Notebooks.  

*SkillPathBuild.ipnyb* - построение пути прокачки навыков на основании данных клиента и курса  
*VacancyParser.ipnyb* - парсер вакансий с сайта hh.ru, подготовка данных для построения эталонных вакансий, которые используются в модуле SkillPathBuild.ipnyb  


## 2. Модуль SkillPathBuild
На данный момент уровень на который претендует клиент необходимо указывать вручную. 

## 2.1. Основные функции:
* **SkillGraph(skill, all_courses, client)** 
Построение пути прокачки навыка
**Входные данные:**  
*skill* - название навыка
*all_courses* - БД курсов
*client* - информация об разностей между уровнями владения навыком клиентом и требуемым уровнем
**Выходные данные:**
*data* - данные о курсах соответсвующих указанному навыку *skill*
*G* - граф курса
*initial_nodes* - начальные узлы графа
*final_nodes* - конечные узлы графа

* **FinalOutput(client1, vacs_ideal, courses_db, level, threshold, criterion)** 
Построение пути прокачки всех навыков с учетом клиентских требований 
**Входные данные:** 
*client1* - входной файл с данными скиллов клиента  
*vacs_ideal* - лист, содержащий датафреймы идеальных вакансий  
*courses_db* - датафрейм с базой данных курсов  
*level* - уровень, на который претендует клиент  
*threshold* - порог отсечки для курсов (при выборе пути, содержащего разные курсы, отсечка происходит только по суммарной стоимости курсов)   
*criterion* - вспомогательный параметр  
**Выходные данные:** 
*skill_path* - лист датафреймов, где каждый датафрейм  содержит один возможный путь прокачки навыков.
**Особенности:**
Построение пути прокачки навыков происходит исходя из их приоритета. Чем выше приоритет курса (для заданного уровня навыка), тем выше он стоит в списке курсов.

## 3. VacancyParser
При парсинге hh.ru данные вакансий сохраняются в создаваемые папки.


# 4. Замечания: 
Код отформатирован с отступом 4, по умолчанию в Google Colab отступ 2 (его можно менять в настройках). 
Однако, ноутбук запускается в Colab с отступом 4.

**Запуск ноутбуков:** 
Для работы ноутбуков необходимо загрузить папку ProjectN5 в корень Google Drive, 
* **Путь для папки с проектом:** "My Drive/ProjectN5"

* **Монтирование Google диска для загрузки и выгрузки файлов**:
Для запуска ноутбуков нужно правой кнопкой мыши выбрать Открыть в Google Colaboratory
При работе ноутбука понадобиться монтирование доступа к диску, для этого
нужно перейти по предлагаемой при монтировании ссылке и Разрешить доступ к диску.

# 4. Дополнительно
Установка необходимых пакетов для google parser

pip install search-engine-parser - 


