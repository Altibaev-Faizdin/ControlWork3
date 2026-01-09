import flet as ft
import datetime
import os

HISTORY_FILE = "history.txt"

def main(page: ft.Page):
    page.title = 'My first Flet app'
    page.theme_mode = ft.ThemeMode.LIGHT

    text_hello = ft.Text(value="Привет!", color=ft.Colors.BLUE)

    greeting_history = []

    history_text = ft.Text("История приветствий:")


    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            greeting_history.extend([line.strip() for line in f.readlines() if line.strip()])

        greeting_history[:] = greeting_history[-5:]

        if greeting_history:
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)

    def save_history():
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            for item in greeting_history:
                f.write(item + "\n")

    def on_button_click(e):
        name = name_input.value.strip()
        current_time = datetime.datetime.now().strftime("%Y:%m:%d - %H:%M:%S")

        if name:
            record = f"{current_time} - Здравствуйте, {name}!"
            text_hello.value = record
            text_hello.color = ft.Colors.GREEN
            name_input.value = None

            greeting_history.append(record)
            greeting_history[:] = greeting_history[-5:]

            save_history()
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            text_hello.value = "Пожалуйста, введите имя!"
            text_hello.color = ft.Colors.RED

        page.update()

    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
            theme_button.icon = ft.Icons.LIGHT_MODE
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            theme_button.icon = ft.Icons.DARK_MODE
        page.update()

    elevated_button = ft.ElevatedButton("ОТПРАВИТЬ", icon=ft.Icons.SEND, on_click=on_button_click)
    name_input = ft.TextField(label='Введите ваше имя', on_submit=on_button_click)

    theme_button = ft.IconButton(
        icon=ft.Icons.DARK_MODE,
        tooltip="День / Ночь",
        on_click=toggle_theme
    )

    buttons_row = ft.Row(
        controls=[elevated_button, theme_button],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )
    page.add(text_hello, name_input, buttons_row, history_text)

ft.app(target=main)
