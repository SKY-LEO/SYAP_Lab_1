# Требуется создать csv-файл «rows_300.csv» со следующими
# столбцами: № - номер по порядку (от 1 до 300); секунда – текущая секунда на
# вашем ПК; микросекунда – текущая миллисекунда на часах. На каждой итерации
# цикла искусственно приостанавливайте скрипт на 0,01 секунды. Для работы с
# файлами подобного текстового формата потребуется встроенная в Python
# библиотека csv

import csv
import datetime
import time


def main():
    with open("rows_300.csv", "w", newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["№", "секунда", "миллисекунда"])
        for i in range(1, 301):
            now_time = datetime.datetime.now()
            second = now_time.second
            millisecond = float(now_time.microsecond/1000)
            writer.writerow([i, second, millisecond])
            time.sleep(0.01)


if __name__ == '__main__':
    main()
