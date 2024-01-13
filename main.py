from flet import *
import flet as ft

# ---------------------------------------------------- MAIN --------------------------------------------------------- #


def main(page: ft.Page):
    page.title = "Test"
    page.theme_mode = ft.ThemeMode.DARK  # The default theme mode
    page.go("/welcome")

    def route_change(e) -> None:
        page.views.clear()

        if page.route == ("/welcome"):
            page.views.append(welcome(page))

        # Other routes and their respective layout

        page.update()

    page.on_route_change = route_change
    page.go(page.route)


# --------------------------------------------------- LAYOUTS ------------------------------------------------------- #


def welcome(page: ft.Page):
    welcomeContent = ft.Column(
        controls=[
            Row(
                controls=[ft.Image(src=LOGO, error_content=Text("Logo", italic=True))],
                width=200,
                height=200,
            ),
            Row(height=30),
            Row(
                controls=[
                    Text(
                        " WELCOME TO",
                        color=BlackORWhiteText(page.theme_mode),
                        weight=FontWeight.W_600,
                        size=24,
                        font_family="Calibri",
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(
                controls=[
                    Text(
                        "HELPING HANDS",
                        color=BlackORWhiteText(page.theme_mode),
                        weight=FontWeight.W_700,
                        size=35,
                        font_family="Calibri",
                    )
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            Row(height=15),
            Row(
                spacing=25,
                controls=[
                    OutlinedButton(
                        "Login",
                        on_click=lambda _: page.go("/login"),
                        style=OutlinedButtonStyle(page.theme_mode),
                    ),
                    OutlinedButton(
                        "Register",
                        on_click=lambda _: page.go("/register"),
                        style=OutlinedButtonStyle(page.theme_mode),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    ctrl = Container(
        expand=True,
        content=welcomeContent,
        margin=-10,
        gradient=RadialGradientStyle(page.theme_mode),
    )

    return View(
        route="/welcome",
        padding=10,
        spacing=25,
        controls=[SafeArea(ctrl, expand=True)],
        vertical_alignment=MainAxisAlignment.CENTER,
        horizontal_alignment=CrossAxisAlignment.CENTER,
    )


# ---------------------------------------------------- STYLES -------------------------------------------------------- #

LOGO = f"https://raw.githubusercontent.com/Paco-Rubio/HAssets/main/Helping%20Hands.png"
BUTTONTEXTCOLOR = "BLACK"
BUTTONBGCOLOR = ft.colors.with_opacity(1, ft.colors.WHITE)
BUTTONOVERLAYCOLOR = ft.colors.with_opacity(0.1, ft.colors.BLACK)


def BlackORWhiteText(theme):
    if theme == "DARK":
        return ft.colors.WHITE
    else:
        return ft.colors.BLACK


def OutlinedButtonStyle(theme):
    if theme == "DARK":
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            side=ft.BorderSide(1.5, color="#ffffff"),
            color=BUTTONTEXTCOLOR,
            bgcolor=BUTTONBGCOLOR,
            overlay_color=BUTTONOVERLAYCOLOR,
        )
    else:
        return ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=20),
            side=ft.BorderSide(1.5, color="#000000"),
            color=BUTTONTEXTCOLOR,
            bgcolor=BUTTONBGCOLOR,
            overlay_color=BUTTONOVERLAYCOLOR,
        )


def RadialGradientStyle(theme):
    if theme == "DARK":
        return ft.RadialGradient(
            center=ft.Alignment(0, -1.25),
            radius=1.4,
            colors=[
                "#3A8096",
                "#050A10",
            ],
        )
    else:
        return ft.RadialGradient(
            center=ft.Alignment(0, -1.25),
            radius=1.4,
            colors=[
                # "#3A8096",
                "#E0E3E7",
            ],
        )


ft.app(main)
