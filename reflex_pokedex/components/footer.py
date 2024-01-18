import reflex as rx
import datetime
import reflex_pokedex.constants as const
from reflex_pokedex.styles.styles import Size, Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo.jpg",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt="Logotipo de HernandezPalo."
        ),
        rx.link(
            rx.box(
                f"© 2023-{datetime.date.today().year} ",
                rx.span("HernandezPalo by Javier Hernandez", color=Color.PRIMARY.value),
                " ."
            ),
            href=const.HERNANDEZPALO_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM EXTREMADURA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )