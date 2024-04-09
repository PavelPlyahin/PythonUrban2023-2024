""" Задание:

Разработайте функцию для извлечения информации из HTML-текста (строки Python)
о ссылках на изображения (URL-адресах картинок). Функция должна находить
все ссылки на изображения в форматах JPEG, JPG, PNG или GIF и возвращать их список.

1. Создайте функцию extract_image_links(html_text), которая принимает HTML-текст и извлекает ссылки на изображения.
2. Используйте регулярные выражения для поиска URL-адресов картинок с расширениями .jpg, .jpeg, .png или .gif.
3. Верните список всех найденных ссылок на изображения. """

import re


def extract_image_links(html_text):
    pattern = r'<img[^>]+?src\s*=\s*["\'](?P<url>(?:https?:\/\/)?' \
              r'(?:www\.)?example\.com\/(?:image\d+\.){1}[a-z]{3,4})["\']'
    links = re.findall(pattern, html_text)
    return links


sample_html = ("<img src='https://example.com/image1.jpg'> "
               "<img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")


def print_result(list_links: object) -> object:
    if list_links:
        for urls in list_links:
            print(urls)
    else:
        print('Нет ссылок с картинками в HTML тексте.')


image_links = extract_image_links(sample_html)
print_result(image_links)
