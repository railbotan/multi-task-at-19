# Отчет
## Задача IO Bound
### Синхронный проход по 100 ссылкам
![](screens/io_sync.png)

### Ассинхронный проход по 100 ссылкам
* 5 воркеров
![](screens/io_async_5.png)
![](screens/io_async_5_disp.png)
* 10 воркевор
![](screens/io_async_10.png)
![](screens/io_async_10_disp.png)
* 50 воркеров
![](screens/io_async_50.png)
![](screens/io_async_50_disp.png)

Наглядно можно увидеть, что скрость работы программы увеличивается 
с увеличением количества потоков

## Задача CPU Bound
### Синхронный поиск одной монеты
![](screens/cpu_sync.png)
![](screens/cpu_sync_disp.png)
### Асинхронный поиск 3 монет
* 2 воркера
![](screens/cpu_async_2.png)
![](screens/cpu_async_2_disp.png)
* 4 воркера
![](screens/cpu_async_4.png)
![](screens/cpu_async_4_disp.png)
* 50 воркеров
![](screens/cpu_async_50.png)
![](screens/cpu_async_50_disp.png)

С увеличением количества процессов, скорость работы программы так же увеличивается, 
но только до тех пор пока не превышает количество логических ядер компьютера, 
в противном случае, скрость работы может даже ухудшиться.
