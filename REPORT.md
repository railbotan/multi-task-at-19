###########################CHEKER##############################################
Замерьте время синхронной проверки ссылок.
200 секунд на 200 ссылок при синхронной проверке
<p align="center">
  <img src="./result_one/1.1.jpg" title="hover text">
</p>

82 секунды при работе 5 воркеров
<p align="center">
  <img src="./result_one/5_worker.jpg" title="hover text">
  <img src="./result_one/5_worker_result.jpg" title="hover text">
</p>

71 секунда при работе 10 воркеров
<p align="center">
  <img src="./result_one/10_worker.jpg" title="hover text">
  <img src="./result_one/10_worker_result.jpg" title="hover text">
</p>
67 секунды при работе 100 воркеров
<p align="center">
  <img src="./result_one/100_worker.jpg" title="hover text">
  <img src="./result_one/100_worker_result.jpg" title="hover text">
</p>
Загрузка памяти, процессора, сети увеличивается![two_2_worker](https://user-images.githubusercontent.com/75811994/144906205-1b4a3343-07b6-43bd-b9e7-63d8b4be4ef2.jpg)

Время работы уменьшается

###############################################################################


############################MINER##############################################
Замерьте скорость герации на 1 ядре у вас на компьютере.
142 секунды при генерации 3 монет на одном ядре
<p align="center">
  <img src="./result_two/two_one_.jpg" title="hover text">
</p>

81 секунда при генерации 3 монет на двух ядрах
<p align="center">
  <img src="./result_two/two_workers.jpg" title="hover text">
  <img src="./result_two/two_2_worker.jpg" title="hover text">
</p>
31 секунда при генерации 3 монет на четырех логических ядрах
<p align="center">
  <img src="./result_two/two_four.jpg" title="hover text">
  <img src="./result_two/two_2_worker.jpg" title="hover text">
</p>
При увелечении кол-во воркеров, больше чем лог ядер время НЕ уменьшается, случайных характер майнинга монет, конечно тоже имеет вес, и все же, при увелечении воркеров- загрузка процессора увеличивается, время работы уменьшается. Воркеров больше, чем логических ядер не создается, в чем убедились.
<p align="center">
  <img src="./result_two/two_60.jpg" title="hover text">
</p>
###############################################################################
