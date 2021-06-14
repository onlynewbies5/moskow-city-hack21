import pandas as pd
import os
import json

from IPython.core.display import display
from IPython.display import clear_output
from ProjectN5.config_recommendation import *


def VacancyFeatureExtraction(directory):
    files_number = len(os.listdir(directory))
    i = 0
    df = pd.DataFrame(columns=['id', 'name', 'skills'])
    # вспомогательные списки
    id_current = []
    name_current = []
    # experience_current = []
    # position_current = []

    # глобальные списки для навыков соискателя

    # descriptions = [] #описание вакансии
    # experiences = [] #опыт требуемый у соискателя
    # positions = [] #позиция (junior, middle, senior и т.д.)

    # Проходимся по всем файлам в папке vacancies
    for files in os.listdir(directory):
        # for i in range(0,10):

        ids = []  # идентификатор вакансии
        names = []  # наименование вакансии
        skills_name = []  # название ключевого навыка

        # чтение данных
        f_data = open('{}/{}'.format(directory, files), encoding='utf8')
        jsonText = f_data.read()
        f_data.close()

        # перевод данных из JSON
        DataJSON = json.loads(jsonText)

        # Заполняем списки для таблиц
        id = DataJSON['id']
        name = DataJSON['name']
        # descriptions.append(DataJSON['description'])
        # experience = DataJSON['experience']['id']

        for skill in DataJSON['key_skills']:
            ids.append(id)
            names.append(name)
            skills_name.append(skill['name'])

        n_length = len(DataJSON['key_skills'])

        # запись данных в глобальные списки
        ids.extend(id_current)
        names.extend(name_current)
        # experiences.extend(experience_current)
        # positions.extend(position_current)

        # отображение прогресса
        i += 1
        clear_output(wait=True)
        display('Готово {} из {}'.format(i, files_number))

        print('ids length', len(ids))
        print('names length', len(names))
        # print('exp length', len(experiences))
        print('skills length', len(skills_name))

        # создание датафрейма со навыками и данными опыта
        df_skill = pd.DataFrame({'id': ids, 'name': names, 'skills': skills_name})
        df = df.append(df_skill)
        # df.to_csv('/ProjectN5/database/skills_for_specific_vacancy.csv')
    return df

data_da = VacancyFeatureExtraction(PATH + dir_da)
data_ds = VacancyFeatureExtraction(PATH + dir_ds)
data = data_da.append(data_ds)
display(data.shape, data.head(2))
# data.to_csv('/ProjectN5/database/skills_for_prediction_model.csv')