# moskow-city-hack21
Командный репозиторий для проекта

## Описание модулей
Отдельные модули представлены, как отдельные тетрадки Jupyter Notebooks.  

*SkillPathBuild.ipnyb* - построение пути прокачки навыков на основании данных клиента и курса  
*VacancyParser.ipnyb* - парсер вакансий с сайта hh.ru, подготовка данных для построения эталонных вакансий, которые используются в модуле SkillPathBuild.ipnyb  


### SkillPathBuild
На данный момент уровень на который претендует клиент необходимо указывать вручную
Построение пути развития производится при вызове функции:

**FinalOutput(client1, vacs_ideal, courses_db, level, threshold, criterion)**  

Она возвращает лист датафреймов, где каждый датафрейм  содержит один возможный путь прокачки навыков.
*client1* - входной файл с данными скиллов клиента  
*vacs_ideal* - лист, содержащий датафреймы идеальных вакансий  
*courses_db* - датафрейм с базой данных курсов  
*level* - уровень, на который претендует клиент  
*threshold* - порог отсечки для курсов (при выборе пути, содержащего разные курсы, отсечка происходит только по суммарной стоимости курсов)   
*criterion* - вспомогательный параметр  

# VacancyParser
При парсинге hh.ru данные вакансий сохраняются в создаваемые папки.


# Замечание: 
Код отформатирован с отступом 4, по умолчанию в Google Colab отступ 2 (его можно менять в настройках). 
Однако, ноутбук запускается в Colab с отступом 4.


# Запуск ноутбуков
Для работы ноутбуков необходимо загрузить папку ProjectN5 в корень Google Drive
путь должен быть такой 
"My Drive/ProjectN5"

Далее для запуска ноутбуков нужно правой кнопкой мыши выбрать Открыть в Google Colaboratory

При работе ноутбука понадобиться монтирование доступа к диску, для этого
нужно перейти по предлагаемой при монтировании ссылке и Разрешить доступ к диску.

# Дополнительно
Установка необходимых пакетов для google parser

pip install search-engine-parser - 


