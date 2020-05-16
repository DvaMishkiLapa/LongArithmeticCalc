# LongArithmeticCalc

Калькулятор длинной арифметики.

## Запуск программы

Запустить в скомпилированной папке файл ```LongArithmeticCalc.exe``` из папки ```release``` или запустить ```main.py```.

## Конвертация файла ```.ui``` в ```.py``` c помощью ```pyuic5```

Пример:

```sh
pyuic5 main.ui -o ui.py
```

Где ```main.ui``` - путь до изначального файла, а ```ui.py``` - путь для конвертированного файла.

### Запуск Qt designer

Перед запуском стоит проверить, установлен ли он и прописан ли путь до него в PATH.
Или же, если используется ```venv```, активирован ли ```venv``` и установлен ли там Qt designer.
Qt designer содержится в пакете ```pyqt5-tools```

Windows:

```sh
designer.exe
```

Linux:

```sh
designer
```

## Сборка в ```.exe``` файл

Перед запуском стоит проверить, установлен ли ```auto-py-to-exe``` и прописан ли путь до него в PATH.
Или же, если используется ```venv```, активирован ли ```venv``` и установлен ли там Qt designer.
Qt designer содержится в пакете ```auto-py-to-exe```.

Запустить ```auto-py-to-exe```, в меню указать:

- ```Script Location``` - указать файл ```main.py```
- ```Onefile``` - выбрать ```One Directory```
- ```Console Window``` - выбрать ```Window Based (hide the console)```
все остальное оставить как есть. Нажать ```Convert .py to .exe``` и после успешной компиляции нажать ```Open output folder```.
