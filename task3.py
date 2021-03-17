#пусть здесь будет простой web api на фласке
import flask
api = flask.Flask(__name__)
api.config['DEBUG'] = True

intervals = {
    'lesson': [1594663200, 1594666800],
    'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
    'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
}
#опять же бинарный поиск, ниже поясню принцип работы всей функции appearance
def search(test, src, left, right):
    while left <= right:
        mid = int((left + right) / 2)
        if test[mid] == src:
            return True
        if test[mid] > src:
            right = mid - 1
        else:
            left = mid + 1
    if not right == src:
        return False

@api.route('/', defaults={'intervals': intervals}, methods=['GET'])

def appearance(intervals):
    #ниже много-много переменных, надеюсь, это не критично
    #три переменных для итогового сокращения строк кода
    lesson = intervals['lesson']
    pupil = intervals['pupil']
    tutor = intervals['tutor']
    #генератором делаю список секунд, которые длился урок
    lessontime = [i for i in range(lesson[0], lesson[1] + 1)]
    #переменные для списков секунд, когда присутствовал препод
    tutortime = []
    #присутствовал ученик
    pupiltime = []
    #присутствовал препод на уроке
    tutorlesson = []
    #присутствовали ученик и препод на уроке
    total = []

    # нечетные индексы: 1,3,5 и т.д. - выход, четные - вход
    for i in range(1, len(tutor), 2):
        # + 1 я пишу везде, т.к. в ходе тестирования заметил, что без этого плюса в конечные списки не входят секунды выхода
        # я ведь правильно понимаю, что эти секунды тоже должны учитываться?
        for sec in range(tutor[i - 1], tutor[i] + 1):
            tutortime.append(sec)
    for i in range (1, len(pupil), 2):
        for sec in range(pupil[i - 1], pupil[i] + 1):
            pupiltime.append(sec)
    #каждая секунда, которая пересекается по бинарному поиску, учитывается
    for tutorsec in tutortime:
        if search(lessontime, tutorsec, 0, len(lessontime) - 1) == True:
            tutorlesson.append(tutorsec)
    for pupilsec in pupiltime:
        if search(tutorlesson, pupilsec, 0, len(tutorlesson) - 1) == True:
            total.append(pupilsec)
    #считаем все секунды
    return str(len(total))

print(appearance(intervals))

api.run()