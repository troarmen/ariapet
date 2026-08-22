#!/usr/bin/env python3
"""Aplica os tokens de design da ARIA no settings_data.json do Horizon."""
import json, re, sys, shutil

PATH = "/home/troarmen/Downloads/ariapet/theme/config/settings_data.json"
raw = open(PATH, encoding="utf-8").read()

m = re.match(r"^(/\*.*?\*/)", raw, flags=re.S)
header = m.group(1) if m else ""
body = raw[len(header):].strip()
data = json.loads(body)
cur = data["current"]

# ---------------------------------------------------------------- tipografia
# "Serifa de alto contraste em peso regular, títulos contidos e rótulos em
#  caixa alta com espaçamento aberto. O premium vem da contenção."
cur.update({
    "type_heading_font":    "playfair_display_n4",   # serifa, peso REGULAR
    "type_accent_font":     "playfair_display_n4",
    "type_body_font":       "inter_n4",
    "type_subheading_font": "inter_n4",

    "type_size_paragraph":        "16",                # era 14
    "type_line_height_paragraph": "body-loose",

    # escala contida: h1 cai de 56 para 40
    "type_font_h1": "heading", "type_size_h1": "40",
    "type_line_height_h1": "display-tight",
    "type_letter_spacing_h1": "heading-tight",
    "type_case_h1": "none",

    "type_font_h2": "heading", "type_size_h2": "32",   # era 48
    "type_line_height_h2": "display-tight",
    "type_letter_spacing_h2": "heading-tight",
    "type_case_h2": "none",

    "type_font_h3": "heading", "type_size_h3": "24",   # era 32
    "type_line_height_h3": "display-normal",
    "type_letter_spacing_h3": "heading-tight",
    "type_case_h3": "none",

    "type_font_h4": "heading", "type_size_h4": "20",   # era 24
    "type_line_height_h4": "display-normal",

    # h5 e h6 sao os ROTULOS: caixa alta, espacamento aberto
    "type_font_h5": "subheading", "type_size_h5": "12",
    "type_line_height_h5": "display-loose",
    "type_letter_spacing_h5": "heading-loose",
    "type_case_h5": "uppercase",

    "type_font_h6": "subheading", "type_size_h6": "12",
    "type_line_height_h6": "display-loose",
    "type_letter_spacing_h6": "heading-loose",
    "type_case_h6": "uppercase",
})

# ------------------------------------------------------------------- formas
# Editorial premium nao tem canto arredondado.
cur.update({
    "page_width": "normal",                 # era narrow
    "button_border_radius_primary": 0,      # era 14
    "button_border_radius_secondary": 0,    # era 14
    "badge_corner_radius": 0,               # era 100
    "badge_text_transform": "uppercase",
    "card_corner_radius": 0,                # era 4
    "inputs_border_radius": 0,              # era 4
    "popover_border_radius": 0,             # era 14
    "variant_button_radius": 0,             # era 14
    "variant_swatch_radius": 0,             # era 32
    "product_corner_radius": 0,
    "card_hover_effect": "none",
})

# -------------------------------------------------------------------- cores
# "Preto, branco e um unico neutro quente. Nenhuma cor saturada."
INK        = "#141414"   # preto quente, nunca #000 puro
INK_SOFT   = "#141414cf"
BONE_LIGHT = "#F2EDE6"   # o neutro quente
BONE_MID   = "#E3D9CC"
OFF_WHITE  = "#FAF8F5"
NEAR_BLACK = "#1C1A18"


def light(bg):
    return {
        "background": bg,
        "foreground_heading": INK,
        "foreground": INK_SOFT,
        "primary": INK_SOFT,
        "primary_hover": INK,
        "border": "#1414141f",
        "shadow": INK,
        "primary_button_background": INK,
        "primary_button_text": "#ffffff",
        "primary_button_border": INK,
        "primary_button_hover_background": "#3a3632",
        "primary_button_hover_text": "#ffffff",
        "primary_button_hover_border": "#3a3632",
        "secondary_button_background": "rgba(0,0,0,0)",
        "secondary_button_text": INK,
        "secondary_button_border": INK,
        "secondary_button_hover_background": INK,
        "secondary_button_hover_text": "#ffffff",
        "secondary_button_hover_border": INK,
        "input_background": "rgba(0,0,0,0)",
        "input_text_color": INK,
        "input_border_color": "#14141440",
        "input_hover_background": "#14141408",
        "variant_background_color": "rgba(0,0,0,0)",
        "variant_text_color": INK,
        "variant_border_color": "#14141440",
        "variant_hover_background_color": "#14141410",
        "variant_hover_text_color": INK,
        "variant_hover_border_color": INK,
        "selected_variant_background_color": INK,
        "selected_variant_text_color": "#ffffff",
        "selected_variant_border_color": INK,
        "selected_variant_hover_background_color": "#3a3632",
        "selected_variant_hover_text_color": "#ffffff",
        "selected_variant_hover_border_color": "#3a3632",
    }


def dark(bg):
    return {
        "background": bg,
        "foreground_heading": "#ffffff",
        "foreground": "#ffffffd6",
        "primary": "#ffffffd6",
        "primary_hover": "#ffffff",
        "border": "#ffffff26",
        "shadow": "#000000",
        "primary_button_background": "#ffffff",
        "primary_button_text": INK,
        "primary_button_border": "#ffffff",
        "primary_button_hover_background": BONE_LIGHT,
        "primary_button_hover_text": INK,
        "primary_button_hover_border": BONE_LIGHT,
        "secondary_button_background": "rgba(0,0,0,0)",
        "secondary_button_text": "#ffffff",
        "secondary_button_border": "#ffffff",
        "secondary_button_hover_background": "#ffffff",
        "secondary_button_hover_text": INK,
        "secondary_button_hover_border": "#ffffff",
        "input_background": "rgba(0,0,0,0)",
        "input_text_color": "#ffffff",
        "input_border_color": "#ffffff59",
        "input_hover_background": "#ffffff0f",
        "variant_background_color": "rgba(0,0,0,0)",
        "variant_text_color": "#ffffff",
        "variant_border_color": "#ffffff59",
        "variant_hover_background_color": "#ffffff1a",
        "variant_hover_text_color": "#ffffff",
        "variant_hover_border_color": "#ffffff",
        "selected_variant_background_color": "#ffffff",
        "selected_variant_text_color": INK,
        "selected_variant_border_color": "#ffffff",
        "selected_variant_hover_background_color": BONE_LIGHT,
        "selected_variant_hover_text_color": INK,
        "selected_variant_hover_border_color": BONE_LIGHT,
    }


palette = {
    "scheme-1": light("#ffffff"),      # branco — padrao
    "scheme-2": light(BONE_LIGHT),     # neutro quente claro
    "scheme-3": light(BONE_MID),       # neutro quente medio (era verde #eef1ea)
    "scheme-4": light(OFF_WHITE),      # off-white quente (era azul #e1edf5)
    "scheme-5": dark(NEAR_BLACK),      # preto quente (era #333333)
}

for name, settings in palette.items():
    if name in cur["color_schemes"]:
        cur["color_schemes"][name]["settings"].update(settings)

# scheme-6 e o transparente usado como overlay do hero: texto claro sobre foto
for name in ("scheme-6",):
    if name in cur["color_schemes"]:
        s = dark("rgba(0,0,0,0)")
        cur["color_schemes"][name]["settings"].update(s)


# esquema customizado remanescente: fundo transparente com tinta preta pura
for name in list(cur["color_schemes"]):
    if name.startswith("scheme-") and len(name) > 12:
        sc = cur["color_schemes"][name]["settings"]
        sc.update(light("rgba(0,0,0,0)"))

shutil.copy(PATH, "/home/troarmen/Downloads/ariapet/ops/settings_data.original.json")
out = header + json.dumps(data, indent=2, ensure_ascii=False) + "\n"
open(PATH, "w", encoding="utf-8").write(out)
print("tokens aplicados; backup no scratchpad")
