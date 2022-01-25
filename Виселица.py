def game():
    import random
    word_list = ['человек', 'работа', 'вопрос', 'сторона',
    'страна', 'случай', 'голова', 'ребенок', 'система', 'отношение',
    'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история',
    'власть', 'тысяча', 'возможность', 'результат', 'область', 'статья',
    'компания', 'группа', 'развитие', 'процесс', 'условие', 'средство',
    'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие',
    'государство', 'любовь', 'взгляд', 'общество', 'деятельность',
    'организация', 'президент', 'комната', 'порядок', 'момент',
    'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание',
    'смерть', 'программа', 'задача', 'предприятие', 'разговор',
    'правительство', 'производство', 'информация', 'положение',
    'интерес', 'федерация', 'правило', 'управление', 'мужчина',
    'партия', 'сердце', 'движение', 'материал', 'неделя', 'чувство',
    'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные',
    'мнение', 'документ', 'институт', 'проект', 'встреча', 'директор',
    'служба', 'судьба', 'девушка', 'очередь', 'состав', 'количество',
    'событие', 'объект', 'создание', 'значение', 'период', 'искусство',
    'структура', 'пример', 'исследование', 'гражданин', 'начальник',
    'принцип', 'воздух', 'характер', 'борьба', 'использование',
    'размер', 'образование', 'мальчик', 'представитель', 'участие',
    'девочка', 'политика', 'картина', 'доллар', 'территория',
    'изменение', 'направление', 'рисунок', 'течение', 'церковь',
    'население', 'большинство', 'музыка', 'правда', 'свобода', 'память',
    'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
    'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ',
    'журнал', 'руководитель', 'специалист', 'оценка', 'регион',
    'процент', 'родитель', 'требование', 'основание', 'половина',
    'анализ', 'автомобиль', 'экономика', 'литература', 'бумага',
    'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
    'граница', 'модель', 'операция', 'название', 'старик', 'миллион',
    'счастье', 'ребята', 'кабинет', 'магазин', 'пространство', 'знание',
    'защита', 'руководство', 'площадь', 'сознание', 'возраст',
    'участник', 'участок', 'желание', 'доктор', 'председатель',
    'представление', 'солдат', 'художник', 'оружие', 'соответствие',
    'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга',
    'содержание', 'радость', 'безопасность', 'продукт', 'комплекс',
    'бизнес', 'сотрудник', 'предложение', 'технология', 'реформа',
    'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль',
    'продукция', 'техника', 'здание', 'необходимость', 'подготовка',
    'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
    'обстоятельство', 'победа', 'источник', 'звезда', 'сестра',
    'практика', 'проведение', 'карман', 'определение', 'функция',
    'войско', 'комиссия', 'применение', 'капитан', 'работник',
    'обеспечение', 'офицер', 'фамилия', 'предел', 'выборы', 'ученый',
    'бутылка', 'теория', 'разработка', 'личность', 'праздник',
    'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель',
    'множество', 'особенность', 'показатель', 'корабль', 'впечатление',
    'частность', 'детство', 'профессор', 'прошлое', 'командир',
    'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка',
    'заявление', 'попытка', 'сравнение', 'расчет', 'депутат', 'комитет',
    'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
    'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение',
    'станция', 'революция', 'колено', 'министерство', 'стекло',
    'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица',
    'механизм', 'передача', 'способность', 'подход', 'энергия',
    'существование', 'исполнение', 'сожаление', 'заместитель', 'ресурс',
    'рождение', 'администрация', 'стоимость', 'улыбка', 'артист',
    'фигура', 'субъект', 'реакция', 'список', 'фотография', 'журналист',
    'нарушение', 'заседание', 'больница', 'существо', 'свойство',
    'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник',
    'реализация', 'страница', 'формирование', 'житель', 'красота',
    'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
    'университет', 'традиция', 'декабрь', 'ладонь', 'сведение',
    'цветок', 'октябрь', 'занятие', 'сентябрь', 'помещение', 'январь',
    'зритель', 'редакция', 'фактор', 'август', 'известие',
    'зависимость', 'охрана', 'оборудование', 'концерт', 'отделение',
    'расход', 'выставка', 'милиция', 'переход', 'произведение',
    'родина', 'собственность', 'лагерь', 'имущество', 'кровать',
    'аппарат', 'середина', 'клиент', 'отрасль', 'беседа',
    'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение',
    'понимание', 'апрель', 'кодекс', 'настроение', 'должность',
    'преступление', 'лестница', 'установка', 'появление', 'получение',
    'образец', 'главное', 'костюм', 'ценность', 'обязанность',
    'таблица', 'воспоминание', 'лошадь', 'коллега', 'организм',
    'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение',
    'оборона', 'выступление', 'температура', 'перспектива', 'подруга',
    'приказ', 'жертва', 'ресторан', 'километр', 'признак',
    'промышленность', 'американец', 'заключение', 'восток',
    'исключение', 'постановление', 'перевод', 'секретарь', 'польза',
    'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь',
    'русский', 'тишина', 'зарплата', 'подарок', 'тюрьма', 'конкурс',
    'книжка', 'изучение', 'просьба', 'публика', 'сообщение', 'угроза',
    'достижение', 'назначение', 'реклама', 'портрет', 'стакан',
    'творчество', 'телевизор', 'инструмент', 'концепция', 'лейтенант',
    'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
    'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия',
    'палата', 'потребность', 'ноябрь', 'увеличение', 'поездка',
    'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство',
    'вещество', 'категория', 'гостиница', 'издание', 'объединение',
    'темнота', 'человечество', 'колесо', 'опасность', 'разрешение',
    'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат',
    'родственник', 'давление', 'присутствие', 'взаимодействие',
    'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание',
    'оплата', 'разница', 'водитель', 'снижение', 'формула', 'капитал',
    'новость', 'эффект', 'губернатор', 'доклад', 'убийство', 'эксперт',
    'автобус', 'платье', 'общение', 'психология', 'проверка',
    'процедура', 'рабочий', 'ремонт', 'обращение', 'обучение',
    'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
    'признание', 'постель', 'владелец', 'компьютер', 'инженер',
    'старуха', 'ракета', 'вершина', 'выпуск', 'торговля', 'молодежь',
    'корпус', 'недостаток', 'сущность', 'талант', 'эффективность',
    'полоса', 'основное', 'рассмотрение', 'следователь', 'описание',
    'редактор', 'дворец', 'забота', 'столик', 'эксперимент', 'печать',
    'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия',
    'ворота', 'дружба', 'окончание', 'величина', 'записка',
    'инициатива', 'совесть', 'активность', 'кредит', 'господь',
    'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция',
    'металл', 'молоко', 'прокурор', 'транспорт', 'поэзия', 'соединение',
    'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
    'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король',
    'подъезд', 'автомат', 'мальчишка', 'чтение', 'поселок', 'свидетель',
    'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение',
    'статус', 'параметр', 'сказка', 'тенденция', 'дыхание', 'версия',
    'масштаб', 'монастырь', 'хозяйка', 'эксплуатация', 'коммунист',
    'пенсия', 'приятель', 'объяснение', 'производитель', 'философия',
    'мощность', 'обязательство', 'кризис', 'указание', 'яблоко',
    'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
    'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица',
    'обработка', 'чемпионат']

    def get_word():
            return random.choice(word_list)

    def display_hangman(tries):
        stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ___$ZZZZZ$________________$$$$$$$______
                    __$$$$$$$$$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    ____$$_$$_________________$$$$$$$______
                    ___$$___$$________________$$$$$$$______
                    ___$$___$$________________$$$$$$$______
                    ___$$___$$_____________$$$$$$$$$$$$$___
                    $__$$___$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # голова, торс, обе руки, одна нога
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ___$ZZZZZ$________________$$$$$$$______
                    __$$$$$$$$$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    ____$$____________________$$$$$$$______
                    ___$$_____________________$$$$$$$______
                    ___$$_____________________$$$$$$$______
                    ___$$__________________$$$$$$$$$$$$$___
                    $__$$_______$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # голова, торс, обе руки
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ___$ZZZZZ$________________$$$$$$$______
                    __$$$$$$$$$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __$_$$$$$_$_______________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # голова, торс и одна рука
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ___$ZZZZZ_________________$$$$$$$______
                    __$$$$$$$_________________$$$$$$$______
                    __$_$$$$$_________________$$$$$$$______
                    __$_$$$$$_________________$$$$$$$______
                    __$_$$$$$_________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # голова и торс
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____ZZZZZ_________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # голова
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____$$$$$_________________$$$$$$$______
                    _____$$$__________________$$$$$$$______
                    ____ZZZZZ_________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''',
                # начальное состояние
            '''
                    _______________________________________
                    ___$$$$$$$$$$______Я-ВИСЕЛИЦА!_________
                    ___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    ______Z___________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    ____ZZZZZ_________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    __________________________$$$$$$$______
                    _______________________$$$$$$$$$$$$$___
                    $___________$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    _\_________/_______$$$$$$$$$$$$$$$$$$$$$
                    __\_______/________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
                    __________________$$$$$$$$$$$$$$$$$$$$$
            ''']
        return stages[tries]
    def play(word):
        # строка, содержащая символы _ на каждую букву задуманного слова
        word_completion = '_' * len(word)
        guessed = False                    # сигнальная метка
        guessed_letters = []               # список уже названных букв
        guessed_words = []                 # список уже названных слов
        tries = 6                          # количество попыток
        print('Давайте играть в угадайку слов!')
        print(display_hangman(tries))
        print(word_completion)
        while True:
            word_input = input('Введите букву или слово: ').lower()
            if not word_input.isalpha():
                print('Вы ошиблись, попробуйте еще')
                continue
            if word_input in guessed_letters:
                print('Уже было')
                continue
            if len(word_input) > 1:
                if word_input == word:
                    print('Поздравляем, вы угадали слово! Вы победили')
                    break
                else:
                    guessed_words.append(word_input)
                    tries -= 1
                    print(f'Не верно, осталось попыток {tries}')
                    print(display_hangman(tries))
                    print_word(word, guessed_letters)
                    if tries == 0:
                        print(f'Вы не смогли угадать слово: {word}')
                        break
                    continue
            if word_input in word:
                guessed_letters.append(word_input)
                for c in word:
                    if c not in guessed_letters:
                        print('Угадали букву')
                        print_word(word, guessed_letters)
                        guessed = False
                        break
                    guessed = True
                if guessed:
                    print_word(word, guessed_letters)
                    print('Поздравляем, вы угадали слово! Вы победили')
                    break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(f'Не верно, осталось попыток {tries}')
                print(display_hangman(tries))
                print_word(word, guessed_letters)
            if tries == 0:
                print(f'Вы не смогли угадать слово: {word}')
                break

    def print_word(word_, list_):
        for c in word_:
            if c in list_:
                print(c, end=' ')
            else:
                print('_', end=' ')
        print()

    x = get_word()
    play(x)
    print('Хотите сыграть еще раз? Нажмите "д", если да и "н", если нет')
    x = input()
    while x != 'н' and x != 'д':
        print('Вы ввели не правльный символ, попробуйте еще раз')
        x = input()
    if x == 'д':
        game()
    elif x == 'н':
        print('Спасибо за игру')
print('Готовы играть? Нажмите "д", если да и "н", если нет')
a = input()
while a != 'н' and a != 'д':
    print('Вы ввели не правльный символ, попробуйте еще раз')
    a = input()
if a == 'д':
    game()
elif a == 'н':
    print('Приходите в слудующий раз')

