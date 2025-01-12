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
        padding=0,
        margin=0
        )

        return bg_gradient

    def main_box():
        return ft.Container(bgcolor=ft.Colors.WHITE, expand=True, margin=24, border_radius=20)

    def logo_header():
        image_logo = ft.Image(src='assets/bot.png', color=ft.Colors.INDIGO_500)
        title_logo = ft.Text('Cronos', font_family='Roboto', size=16, weight=ft.FontWeight.W_500)
        return ft.Container(content=ft.Row([image_logo, title_logo], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER))

    page.add(
        background_gradient()
    )

ft.app(main)