import flet as ft
import datetime
import os

def main(page: ft.Page):
    page.title = "My first Flet app"
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value="Привет!", color=ft.Colors.BLUE)

    name_input = ft.TextField(label="Введите ваше имя")

    # Список истории
    greeting_history = []

    # Загружаем историю из файла, если есть
    if os.path.exists("history.txt"):
        with open("history.txt", "r", encoding="utf-8") as f:
            for line in f.readlines():
                greeting_history.append(line.strip())

    # Текст для отображения истории
    history_text = ft.Column([ft.Text(h) for h in greeting_history])

    def update_history(name):
        # Время и приветствие
        current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")
        greeting = f"{current_time} - Здравствуйте, {name}!"
        greeting_history.append(greeting)

        # Ограничиваем до последних 5
        if len(greeting_history) > 5:
            greeting_history[:] = greeting_history[-5:]

        # Обновляем интерфейс
        history_text.controls.clear()
        for h in greeting_history:
            history_text.controls.append(ft.Text(h))

        # Сохраняем в файл
        with open("history.txt", "w", encoding="utf-8") as f:
            for h in greeting_history:
                f.write(h + "\n")

        page.update()

    def on_button_click(e):
        name = name_input.value.strip()
        if name:
            text_hello.value = f"Здравствуйте, {name}!"
            text_hello.color = ft.Colors.GREEN
            update_history(name)
            name_input.value = ""
        else:
            text_hello.value = "Пожалуйста, введите имя!"
            text_hello.color = ft.Colors.RED
        page.update()

    # Кнопка отправки
    submit_button = ft.ElevatedButton("ОТПРАВИТЬ", on_click=on_button_click)

    page.add(
        text_hello,
        name_input,
        submit_button,
        ft.Text("История последних приветствий:"),
        history_text
    )

ft.app(target=main)
