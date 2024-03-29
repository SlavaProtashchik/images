# Описание работы

Для просто ты запуска и возможности запустить на любом компьютере с установленным Docker в проекте
используется [Dockerfile](./Dockerfile) в котором описана установка всех необходимых библиотек и зависимостей.

Для простоты запуска используется docker compose

Для того чтобы запустить скрипты по генерации изображений достаточно выполнить в папке с проектом

```
docker compose up
```

Все изображения, находящиеся в папке images, обработаются скриптами, согласно заданий, и полученные изображения попадут
в папку [images/output](images/output)

# Задания

Для реализации всех заданий используется библиотека OpenCV (cv2)

Это библиотека алгоритмов компьютерного зрения и обработки изображений с открытым исходным кодом.
Она включает в себя больше четырехсот функций, которые охватывают все основные области компьютерного зрения.
В данном случае, мы используем ее для загрузки изображения, применения пороговой сегментации и сохранения результата в
файл.

## Преобразование Хафа

Файл алгоритма: [hough_transform.py](hough_transform.py)

В приведенном коде реализовано преобразование Хафа для обнаружения окружностей на изображении.

1. Сначала загружается изображение по заданному пути с использованием функции `cv2.imread()`.

2. Затем изображение преобразуется в оттенки серого с помощью функции `cv2.cvtColor()`, что позволяет упростить
   последующую обработку.

3. Чтобы уменьшить шумы, применяется медианное размытие функцией `cv2.medianBlur()`.

4. Далее, применяется преобразование Хафа для окружностей с помощью функции `cv2.HoughCircles()`. Здесь `dp=1` указывает
   на обратное соотношение разрешения аккумулятора и изображения, `minDist=120` - минимальное расстояние между центрами
   обнаруженных окружностей, `param1=50` и `param2=30` - пороговые значения для обнаружения кривых, `minRadius`
   и `maxRadius=0` означают, что окружности любого радиуса могут быть обнаружены.

5. Если окружности найдены, то центры окружностей и внешние границы окружностей отмечаются на исходном изображении.

6. По окончанию обработки измененное изображение записывается в файл.

В целом, преобразование Хафа удачно справляется с поставленной задачей поиска окружностей на изображении. Это
обусловлено тем, что окружности являются достаточно простыми геометрическими формами и хорошо заметны на рассматриваемых
изображениях. Вместе с тем, следует учесть, что точность обнаружения может существенно зависеть от правильности выбора
параметров преобразования Хафа.

## Морфологический анализ изображений

Файл алгоритма: [morphology.py](morphology.py)

Подробное описание [тут](https://habr.com/ru/articles/565378/)

Приведенный алгоритм демонстрирует применение различных морфологических операций к изображению.

1. Сначала изображение загружается с помощью функции `cv.imread()`.
2. Затем инициализируются четыре структурирующих элемента определенной формы и размера, которые будут использованы в
   морфологических операциях.
3. Итак, применяем следующие морфологические операции к изображению для каждого из структурирующих элементов:

- Эрозия (`cv.erode()`): Эта операция удаляет пиксели на границе объектов на изображении. В результате объекты
  становятся меньше.
- Дилатация (`cv.dilate()`): Эта операция добавляет пиксели к границе объектов. Объекты становятся больше.
- Открытие (`cv.morphologyEx(..., cv.MORPH_OPEN, ...)`)): Это последовательность эрозии и дилатации. Позволяет убрать
  шум и мелкие объекты.
- Закрытие (`cv.morphologyEx(..., cv.MORPH_CLOSE, ...)`) : Это последовательность дилатации и эрозии, что позволяет
  закрыть малые отверстия.
- Blackhat (`cv.morphologyEx(..., cv.MORPH_BLACKHAT, ...)`) : Это разность между закрытием изображения и исходным
  изображением.
- Градиент (`cv.morphologyEx(..., cv.MORPH_GRADIENT, ...)`) : Это разность между дилатацией и эрозией изображения.

4. Каждый из результатов сохраняется в файл, путь до которого формируется с помощью вспомогательной
   функции `file_output_path()`.

Таким образом, в приведенном коде демонстрируется применение ключевых операций морфологического анализа изображений -
эрозии, дилатации, открытия, закрытия, операции Blackhat и вычисления морфологического градиента. Можно наблюдать, как
каждая из этих операций меняет изначальное изображение, и анализировать, какая операция лучше всего подходит для решения
определенных задач (например, удаление шума, увеличение контраста на границах объектов и т.д.).

## Сегментация изображения

Файл алгоритма: [segment.py](segment.py)

Описание алгоритма:

В рамках данной задачи используется пороговая сегментация - один из самых простых методов обработки изображений,
часто используемый как первоначальный этап в более сложных алгоритмах.

В первую очередь, изображение 'image.jpg' загружается в память с использованием функции `cv2.imread`,
с параметром 0 для конвертации в оттенки серого. Существенно, что подобная сегментация применима только
для одноканальных изображений.

Далее, применяется функция `cv2.threshold`, которая проходит по большинству пикселей изображения и сравнивает
их значения с заданным порогом - в данном случае, 127. Если значение пикселя превышает порог, оно заменяется на
максимальное значение (255 - белый цвет); если меньше, то на минимальное (0 - черный цвет).

Выбор порога может существенно влиять на результаты сегментации: слишком низкое значение может привести к большому
количеству ложных срабатываний (слишком много пикселей заменяется на белый), в то время как слишком высокое значение
может пропустить некоторые сегменты. В данном случае выбор значения 127 обоснован тем, что это серединное значение
диапазона оттенков серого (от 0 до 255).

Результат работы алгоритма отображается c параллельной визуализацией исходного и обработанного изображений. По
результатам видно, что алгоритм успешно выделяет основные структуры на изображении. Однако, в случае наличия шумов или
более сложных структур, возможно потребуется использовать более сложные методы сегментации.