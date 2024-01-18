import reflex as rx
from enum import Enum

class CustomAttrs(Enum):
    DATA_TEXT = "datatext"
    
# Constants
MAX_WIDTH = "800px"

# Sizes
STYLESHEETS = [
    #"fonts/fonts.css",
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    "https://fonts.googleapis.com/css2?family=Kalnia:wght@500&family=Pacifico&display=swap",

    ]

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"
    LARGE_ICON = "32px"

class Font(Enum):
    TITLE = "Poppins"
    LOGO = "Comfortaa"
    KALNIA="Kalnia"
    DEFAULT= "Mona Sans"

class FontWeight(Enum):
    LIGHT = "300"
    NORMAL = "500"
    MEDIUM = "600"
    BOLD = "700"

class Color(Enum):
    PRIMARY = "#14A1F0"
    SECONDARY = "#087ec4"
    BACKGROUND = "#0C151D"
    CONTENT = "#171F26"


class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"
    FOOTER = "#A3ABB2"
    BLANCO = "#FFFFFF"
    PURPLE = "rgb(188, 154, 250)"
 # Styles
BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.NORMAL.value,
    rx.Link: {
        "text_decoration": "none",
        "_hover": {
        }
    },
}   

glow_text_style = {
    "position": "relative",
    "cursor": "pointer",
    "_after": {
        "content": f"attr({CustomAttrs.DATA_TEXT.value})",
        "position": "absolute",
        "left": "0",
        "width": "100%",
        "height": "100%",
        "opacity": "60%",
        "filter": "blur(6px)",
        "backface-visibility": "hidden",
        "-webkit-backface-visibility": "hidden",
        "-moz-backface-visibility": "hidden",
        "transform": "translateZ(0)",
        "-webkit-transform": "translateZ(0)",
        "-moz-transform": "translateZ(0)"
    },
    "_hover": {
        "_after": {
            "opacity": "100%"
        }
    }
}

container_style = {
    "padding": Size.MEDIUM.value,
    "border_radius": "1.5rem",
    "background": Color.SECONDARY.value,
    "_hover": {
        "box-shadow": f"0 0 {Size.DEFAULT.value} {Color.SECONDARY.value}"
    }
}