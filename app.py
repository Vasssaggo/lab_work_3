import cv2
import numpy as np


# Функция обработки событий мыши
def mouse_callback(event, x, y, flags, param):
     if event == cv2.EVENT_LBUTTONDOWN:
          # Параметры батча
          half_batch_size = batch_size // 2

          # Вычисляем границы батча
          start_x = max(x - half_batch_size, 0)
          start_y = max(y - half_batch_size, 0)
          end_x = min(x + half_batch_size, image.shape[1])
          end_y = min(y + half_batch_size, image.shape[0])

          # Получаем батч из изображения
          batch = image[start_y:end_y, start_x:end_x]

          # Вычисляем среднюю интенсивность по каждому каналу
          mean_intensity = batch.mean(axis=(0, 1))

          # Выводим в консоль
          print(f"Координаты точки: x={x}, y={y}")
          print(f"Средняя интенсивность (B, G, R): {mean_intensity}")

          # Отображаем координаты на изображении
          cv2.putText(image, f'({x}, {y})', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

          # Отображаем обновленное изображение
          cv2.imshow('Image', image)


if __name__ == "__main__":
     # Загрузка изображения
     image = cv2.imread('sky.jpeg', cv2.IMREAD_COLOR)
     if image is None:
          print("Ошибка: Не удалось загрузить изображение.")
          exit()

     cv2.namedWindow('Image')

     # Запрос размера батча у пользователя
     while True:
          try:
               batch_size = int(input("Введите размер батча (30-80 пикселей): "))
               if 30 <= batch_size <= 80:
                    break
               else:
                    print("Недопустимый размер батча! Пожалуйста, введите число от 30 до 80.")
          except ValueError:
               print("Пожалуйста, введите корректное целое число.")

     # Привязка функции обработки событий мыши к окну
     cv2.setMouseCallback('Image', mouse_callback)

     # Отображение изображения
     cv2.imshow('Image', image)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

