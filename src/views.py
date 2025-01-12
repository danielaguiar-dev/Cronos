import flet as ft

def main(page: ft.Page):
    page.title = "CronosBot v.0.0"
    page.window.width = 500
    page.window.height = 700
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.center()
    page.padding = 0
    
    def background_gradient() -> object:
        bg_gradient = ft.Container(content=ft.Row(
            [
                ft.Column(
                    [
                        logo_header(),
                        main_box()
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER
        ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.Colors.BLUE_50, ft.Colors.INDIGO_50],
        ),
        border_radius=0,
        expand=True,
        padding=32,
        margin=0
        )

        return bg_gradient

    def main_box():
        subtitle = ft.Text('Assistente de Correção Monetária do Banco Central', size='14', color=ft.Colors.GREY_600)
        drop_file_box = ft.Draggable(group='file', content=ft.Container(bgcolor=ft.Colors.GREY_600, expand=True))
        
        btn_select_file = ft.ElevatedButton("Choose files...",
        on_click=lambda _: file_picker.pick_files(allow_multiple=True))

        file_picker = ft.FilePicker()
        page.overlay.append(file_picker)
        page.update()

        return ft.Container(content=ft.Column([subtitle, btn_select_file],
                                              horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                                              bgcolor=ft.Colors.WHITE, 
                                              expand=True, 
                                              margin=24,
                                              padding=16, 
                                              border_radius=20)

    def logo_header():
        image_logo = ft.Image(src=r'src\assets\bot.svg', color=ft.Colors.INDIGO_400, width=60, height=60)
        title_logo = ft.Text('Cronos', font_family='Roboto', size=32, weight=ft.FontWeight.W_700)
        return ft.Container(content=ft.Row([image_logo, title_logo],
                                           spacing=12, 
                                           alignment=ft.MainAxisAlignment.CENTER, 
                                           vertical_alignment=ft.CrossAxisAlignment.CENTER))

    page.add(
        background_gradient()
    )

ft.app(main)