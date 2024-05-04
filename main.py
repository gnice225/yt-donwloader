import flet as ft
from pytube import YouTube
def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 600

    page.window_resizable = False

    def Download(e):
        text.value = "Downloading..."
        progress_bar = ft.ProgressBar(width=400)
        lv.controls.append(progress_bar)
        page.update()
        try:

            youtubeObject = YouTube(text_input.value)
            text_1.value = f'{youtubeObject.title}'
            text_2.value = f'by {youtubeObject.author}'
            image.src = f'{youtubeObject.thumbnail_url}'
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download()



            text.value = "Download completed!"
            lv.controls.remove(progress_bar)

            page.update()

        except:

            text.value = "Download failed!"
            lv.controls.remove(progress_bar)
            page.update()

    text_1 = ft.Text(f'', font_family='Cascadia Code')
    text_2 = ft.Text(f'', font_family='Cascadia Code')
    image = ft.Image(src='image.jpg') # серая картинка для замены изображения

    text = ft.Text('Waiting for link...', text_align=ft.TextAlign.CENTER, font_family='Cascadia Code')
    text_input = ft.TextField(hint_text="Enter link", shift_enter=True, on_submit=Download,
                              border_radius=10,
                              border_color=ft.colors.PURPLE,
                              focused_border_color=ft.colors.RED,
                              )

    lv = ft.ListView(controls=[text, text_input, text_1, text_2, image], spacing=10, width=500, height=500)

    page.add(
        ft.Row(
            [
                lv,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(target=main)