import reflex as rx
from reflex_pokedex.styles.styles import Size, Color, TextColor, FontWeight, Font
import reflex_pokedex.styles.styles as  styles

def titulo(text: str, font=Font.DEFAULT, weight=FontWeight.BOLD, size=[Size.DEFAULT.value], color=TextColor.BLANCO) -> rx.Component:
    return rx.text(
        text,
        font_family=font.value,
        font_weight=weight.value,
        font_size=size,
        color=color.value,
        custom_attrs={
            styles.CustomAttrs.DATA_TEXT.value: text,
        },
        style=styles.glow_text_style
    )
