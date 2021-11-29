# IO-bound
## Время работы оригинального скрипта
![io original](https://github.com/KyreOn/multi-task-at-19/blob/main/io-bound%20original.jpg)


## Время работы с пятью потоками
![io 5 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/io-bound%205.jpg)


## Время работы с десятью потоками
![io 10 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/io-bound%2010.jpg)


## Время работы со ста потоками
![io 100 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/io-bound%20100.jpg)


## Выводы
Как можно заметить, с увеличением числа потоков
время работы уменьшается, причем нагрузка на 
систему остается примерно на одном уровне.
----
# CPU-bound


## Время работы оригинального скрипта
![cpu original](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%20original.jpg)
Нагрузка на ЦПУ - 30%
---
## Время работы в два процесса
![cpu 2 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%202.jpg)
Нагрузка на ЦПУ - 60%
---
## Время работы в четыре процесса
![cpu 4 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%204.jpg)
Нагрузка на ЦПУ - 100%
---
## Время работы в пять процессов
![cpu 5 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%205.jpg)
Нагрузка на ЦПУ - 100%
---
## Время работы в десять процессов
![cpu 10 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%2010.jpg)
Нагрузка на ЦПУ - 100%
---
## Время работы в шестьдесят процессов
![cpu 60 workers](https://github.com/KyreOn/multi-task-at-19/blob/main/cpu-bound%2060.jpg)
Нагрузка на ЦПУ - 100%
---
## Выводы
По полученным результатам можно сделать вывод, что время работы 
уменьшается с увеличением числа процессов, пока их число не превышает
число ядер у процессора. После того, как число процессов превысит число
ядер, время работы будет находиться примерно на одном уровне, то уменьшаясь,
то увеличиваясь, т.к. при переборе используются случайно сгенерированные 
значения. Также, с увеличением числа процессов увеличивается нагрузка на
процессор.
