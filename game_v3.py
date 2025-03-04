import numpy as np
number = np.random.randint(1,100)

def game_score_v3(number: int=1) -> int:
    """Угадываем рандомно сгенерированное число"""
    
    findings, count = 100, 0 
    while round(findings) != number:
        count += 1
        if findings < number:
           findings += round(100/(count*4))
        else:
            findings -= round(100/(count*2))
    return count

print('Загаданое Число: {} угадано за {} циклов'.format(number, game_score_v3(number)))

"""" Проверка работы функции """