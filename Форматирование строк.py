# Использование %
team1_num = 5
team2_num = 6
team_all = team1_num + team2_num
print('количество участников в первой команде  "Мастера кода" %d' % (team1_num))
print('количество участников во второй команде "Волшебники данных %d' % (team2_num))
print('количество участников в обеих командах %d' %(team_all))

# Использование format()

score_2 = 42
print('количество задач решённых командой №2 равно', '{}!' .format(score_2))

team1_time = 18015.2
print('"Волшебники данных" решили задачи за, {} секунды' .format(team1_time))

# Использование f-строк:

score_1 = 40
score_2 = 42
score_all = score_1 + score_2
print(f'Команда №1 решила {score_1} задач, Команда №2 решила {score_2} задачи')
print(f'Общее количество выполнено командами {score_all} задачи')

challenge_result = 'Победа команды "Мастера кода"!'
print(f'Результат битвы: {challenge_result}')

tasks_total = 82
time_avg = 350.4
print(f'Сегодня было решенно {tasks_total} задачи в среднем по {time_avg} секунды на задачу!')

