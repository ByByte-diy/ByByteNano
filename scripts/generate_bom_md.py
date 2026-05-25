import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
XLSX_PATH = ROOT / "hardware" / "bom" / "BOM_ByByte_Nano.xlsx"
OUT_PATH = ROOT / "BOM.md"

CATEGORIES = [
    "Плата, живлення та захист",
    "Пасивні компоненти",
    "Напівпровідники та діоди",
    "Модулі та контролери",
    "Роз'єми, перемикачі та кнопки",
    "Механіка та приводи",
]

# Ukrainian descriptions keyed by BOM row number
DESCRIPTIONS_UK = {
    "1": "Тримач батареї 9V",
    "2": "Li-ion акумулятор 9V (форм-фактор «Крона»), перезаряджуваний",
    "3": "Bluetooth-модуль (HC-02 / HC-05 / HC-06)",
    "4": "Пасивний зумер 5V",
    "5": "Електролітичний конденсатор, низький ESR",
    "6": "Електролітичний конденсатор, низький ESR",
    "7": "Керамічний конденсатор",
    "8": "Керамічний конденсатор (100 нФ)",
    "9": "Керамічний конденсатор",
    "10": "ІЧ-світлодіод",
    "11": "Діод",
    "12": "Діод \u0428\u043e\u0442\u0442\u043a\u0456",
    "13": "Запобіжник (опційно)",
    "14": "Pin-header 1×40, крок 2.54 мм",
    "15": "Гніздовий роз'єм 2×1, 2.54 мм, 90°",
    "16": "Pin-header 1×40, крок 2.54 мм, 90°",
    "17": "Тактова кнопка 6 мм, 4 контакти",
    "18": "Феритова бусина EMI",
    "19": "Фоторезистор",
    "20": "Зелений світлодіод 3 мм",
    "21": "Адресний RGB світлодіод WS2812, 5 мм",
    "22": "DC-мотор N20 з редуктором, 6V",
    "23": "Кріплення N20 (ABS) з гвинтом",
    "24": "NPN-транзистор",
    "25": "ІЧ-фототранзистор",
    "26": "MOSFET-транзистор",
    "27": "Резистор 0.125 W",
    "28": "Резистор 0.125 W",
    "29": "Резистор 0.5 W",
    "30": "Резистор 0.125 W",
    "31": "Резистор 0.125 W",
    "32": "Резистор 0.125 W",
    "33": "Резистор 0.125 W",
    "34": "Повзунковий перемикач, 90°",
    "35": "Arduino Nano (ATmega328)",
    "36": "Гніздовий роз'єм 1×40, 2.54 мм (для Nano)",
    "37": "Модуль драйвера двигунів",
    "38": "DC-DC понижуючий модуль (buck)",
    "39": "Ультразвуковий датчик відстані",
    "40": "Модуль датчиків лінії (5 каналів)",
    "41": "ІЧ-приймач",
    "42": "Модуль ESP32-CAM з камерою 120°",
    "43": "Гніздовий роз'єм 1×8, 2.54 мм (для ESP32-CAM)",
    "44": "Операційний підсилювач",
    "45": "Панелька для DIP-8 мікросхеми",
    "46": "Опорне кулькове колесо (caster) для N20",
    "47": "Колесо N20, Ø44 мм, вал 3 мм",
}

CATEGORY_BY_NO = {
    **{str(i): "Плата, живлення та захист" for i in (1, 2, 5, 6, 12, 13, 18, 38)},
    **{str(i): "Пасивні компоненти" for i in (7, 8, 9, 27, 28, 29, 30, 31, 32, 33)},
    **{str(i): "Напівпровідники та діоди" for i in (10, 11, 20, 21, 24, 25, 26, 44, 45)},
    **{str(i): "Модулі та контролери" for i in (3, 4, 19, 35, 37, 39, 40, 41, 42)},
    **{str(i): "Роз'єми, перемикачі та кнопки" for i in (14, 15, 16, 17, 34, 36, 43)},
    **{str(i): "Механіка та приводи" for i in (22, 23, 46, 47)},
}


def slug(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:40] or "item"


def esc(value: str) -> str:
    return value.replace("|", "\\|")


def img_cell(path: str, alt: str) -> str:
    return f'<img src="{path}" alt="{esc(alt)}" width="80" />'


def load_rows() -> list[tuple[str, str, str, str, str]]:
    import openpyxl

    wb = openpyxl.load_workbook(XLSX_PATH, data_only=True)
    ws = wb.active
    raw = list(ws.iter_rows(min_row=2, values_only=True))
    rows = []
    for row in raw:
        if not row or row[0] is None:
            continue
        rows.append(tuple(str(c) if c is not None else "" for c in row[:5]))
    return rows


def main() -> None:
    rows = load_rows()
    grouped: dict[str, list[tuple[str, str, str, str, str, str]]] = {c: [] for c in CATEGORIES}
    for row in rows:
        no, des, qty, comment, value = row
        uk_desc = DESCRIPTIONS_UK.get(no, comment)
        cat = CATEGORY_BY_NO[no]
        grouped[cat].append((no, des, qty, uk_desc, value, comment))

    lines = [
        "# Специфікація компонентів (BOM)",
        "",
        "**ByByte Nano** — основна плата (`Board1_main`)",
        "",
        "Повний перелік компонентів для збірки робота. Таблиці згруповано за типом деталі.",
        "",
        "> Джерело: експорт BOM від 24.05.2026 · Зображення — [`hardware/bom/img/`](hardware/bom/img/)",
        "",
        "## Як додати зображення",
        "",
        "1. Покладіть файл у `hardware/bom/img/`.",
        "2. Використовуйте ім'я з колонки **Файл** (наприклад, `01_bat1.png`).",
        "3. Рекомендований розмір: **80–128 px** по більшій стороні.",
        "",
        "<!--",
        "Підказка: колонка «Зображення» праворуч у таблиці автоматично підхопить файл,",
        "якщо його ім'я збігається зі значенням у колонці «Файл».",
        "-->",
        "",
        "---",
        "",
    ]

    for cat in CATEGORIES:
        items = grouped[cat]
        if not items:
            continue
        lines.extend(
            [
                f"## {cat}",
                "",
                "| № | Позиція | К-сть | Опис | Номінал / модель | Зображення | Файл |",
                "|:--:|---------|:-----:|------|------------------|:----------:|------|",
            ]
        )
        for no, des, qty, uk_desc, value, _comment in items:
            img_file = f"{int(no):02d}_{slug(des.split(',')[0])}.png"
            img_path = f"hardware/bom/img/{img_file}"
            lines.append(
                f"| {no} | `{esc(des)}` | {qty} | {esc(uk_desc)} | {esc(value)} | "
                f"{img_cell(img_path, uk_desc)} | `{img_file}` |"
            )
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## Підсумок",
            "",
            "| Параметр | Значення |",
            "|----------|----------|",
            f"| Унікальних позицій | {len(rows)} |",
            "| Опційні компоненти | F1 (запобіжник) |",
            "| Bluetooth | HC-02 / HC-05 / HC-06 |",
            "| DC-DC модулі | MH-MINI-361 або HW-613 |",
            "| Контролер | Arduino Nano v3 (ATmega328) |",
            "",
        ]
    )

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
