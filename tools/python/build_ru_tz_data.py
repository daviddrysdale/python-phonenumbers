# -*- coding: utf-8 -*-
__author__ = 'komatozz'

import csv
import os
import sys

sys.path.insert(0, '../../python')

SYNONYMS = {
    'Республика Кабардино-Балкарская': 'Кабардино-Балкарская Республика',
    'Республика Чеченская': 'Чеченская республика',
    'Чувашская Республика - Чувашия': 'Чувашская республика',
    'Республика Саха /Якутия/': 'Республика Саха (Якутия)',
    'Республика Удмуртская': 'Республика Удмуртия',
    'г. Москва и Московская область': 'г. Москва и Московская обл.',
    'г. Санкт-Петербург и Ленинградская область':  'г. Санкт-Петербург и Ленинградская обл.',
    'Ханты-Мансийский автономный округ - Югра': 'Ханты - Мансийский - Югра АО'
}

TZ_TO_REGION_DATA = {
    'Europe/Bucharest': ['Калининградская обл.', ],
    'Europe/Moscow': ['Республика Адыгея', 'Республика Дагестан', 'Республика Ингушетия',
                      'Кабардино-Балкарская Республика', 'Республика Калмыкия', 'Республика Крым',
                      'Карачаево-Черкесская Республика', 'Республика Карелия', 'Республика Коми',
                      'Республика Марий Эл', 'Республика Мордовия', 'Республика Северная Осетия - Алания',
                      'Республика Татарстан', 'Чеченская республика', 'Чувашская республика', 'Краснодарский край',
                      'Ставропольский край', 'Архангельская обл.', 'Астраханская обл.', 'Брянская обл.',
                      'Белгородская обл.', 'Владимирская обл.', 'Волгоградская обл.', 'Кировская обл.',
                      'Воронежская обл.', 'Ивановская обл.', 'Калужская обл.', 'Вологодская обл.',
                      'Костромская обл.', 'Курская обл.', 'Ленинградская обл.', 'Липецкая обл.',
                      'Московская обл.', 'Мурманская обл.', 'Нижегородская обл.', 'Новгородская обл.',
                      'Орловская обл.', 'Пензенская обл.', 'Псковская обл.', 'Ростовская обл.',
                      'Рязанская обл.', 'Саратовская обл.', 'Смоленская обл.', 'Тамбовская обл.',
                      'Тверская обл.', 'Тульская обл.', 'Ульяновская обл.', 'Ярославская обл.',
                      'Ненецкий автономный округ', 'г. Москва', 'г. Санкт-Петербург', 'г. Москва и Московская обл.',
                      'г. Санкт-Петербург и Ленинградская обл.', 'г. Севастополь',
                      'Архангельская обл. и Ненецкий автономный округ'],
    'Europe/Samara': ['Самарская обл.', 'Республика Удмуртия'],
    'Asia/Yekaterinburg': ['Республика Башкортостан', 'Пермский край', 'Курганская обл.', 'Оренбургская обл.',
                           'Свердловская обл.', 'Тюменская обл.', 'Челябинская обл.',
                           'Ханты - Мансийский - Югра АО', 'Ямало-Ненецкий АО'],
    'Asia/Omsk': ['Республика Алтай', 'Алтайский край', 'Новосибирская обл.', 'Омская обл.',
                  'Томская обл.'],
    'Asia/Krasnoyarsk': ['Республика Тыва', 'Республика Хакасия', 'Красноярский край', 'Кемеровская обл.'],
    'Asia/Irkutsk': ['Республика Бурятия', 'Забайкальский край', 'Иркутская обл.'],
    'Asia/Yakutsk': ['Республика Саха (Якутия)', 'Амурская обл.'],
    'Asia/Vladivostok': ['Республика Саха (Якутия)', 'Приморский край', 'Хабаровский край', 'Магаданская обл.',
                         'Сахалинская обл.', 'Еврейская АО', 'Еврейская автономная обл.'],
    'Asia/Srednekolymsk': ['Республика Саха (Якутия)', 'Сахалинская обл.'],
    'Asia/Kamchatka': ['Камчатский край', 'Чукотский АО']
}

PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'python/phonenumbers/tzdata'))


def write_file(chunk, index, init_file):
    data_file = open('%s/data%d.py' % (PATH, index), 'w')
    data_file.write('data = {\n')
    data_file.writelines(chunk)
    data_file.write('}')
    data_file.close()

    init_file.write('from .data%d import data\n' % index)
    init_file.write('TIMEZONE_DATA.update(data)\n')


def parse_csv(filename):
    """ Parse input csv file """
    reader = csv.reader(open(filename, 'rb'), dialect='excel', delimiter=';')
    chunk = []
    index = 1

    init_file = open(os.path.join(PATH, '__init__.py'), 'w')
    init_file.write('TIMEZONE_DATA = {}\n')
    init_file.write('from .data0 import data\n')
    init_file.write('TIMEZONE_DATA.update(data)\n')

    for i, row in enumerate(reader):
        if i >= 1 and row:
            row = [column.strip().decode('cp1251').encode('utf8') for column in row]
            region = row[-1].split('|')[-1]
            region = SYNONYMS.get(region, region)

            key = '7' + row[0] + row[1].rstrip('0')

            tz = [tz_name for tz_name, regions in TZ_TO_REGION_DATA.items() if region in regions]
            if tz:
                chunk.append('\t"' + key + '": ' + '("' + '", "'.join(tz) + '", ),\n')

            if len(chunk) > 2000:
                write_file(chunk, index, init_file)
                chunk = []
                index += 1
    if chunk:
        write_file(chunk, index, init_file)

    init_file.write('del data\n')
    init_file.write('TIMEZONE_LONGEST_PREFIX = 7\n')
    init_file.close()

if __name__ == "__main__":
    parse_csv(sys.argv[1])