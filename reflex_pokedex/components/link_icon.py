import reflex as rx
from reflex_pokedex.styles.styles import Size


def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=Size.LARGE_ICON.value,
            height=Size.LARGE_ICON.value,
            alt=alt
        ),
        href=url,
        is_external=True
    )