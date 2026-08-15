import sys
import re


# ============================================================
# Ukrainian -> Latin transliteration
# Cabinet of Ministers of Ukraine Resolution No. 55
# ============================================================

def transliterate_text(text):
    """
    Transliterates ordinary Ukrainian text.

    This function knows nothing about .twg syntax.
    It should be applied only to text which is safe to transliterate.
    """

    # Special case: зг -> zgh
    text = text.replace("Зг", "Zgh")
    text = text.replace("зг", "zgh")

    # Positional rules
    text = re.sub(r'\bЄ', 'Ye', text)
    text = re.sub(r'\bє', 'ye', text)

    text = re.sub(r'\bЇ', 'Yi', text)
    text = re.sub(r'\bї', 'yi', text)

    text = re.sub(r'\bЙ', 'Y', text)
    text = re.sub(r'\bй', 'y', text)

    text = re.sub(r'\bЮ', 'Yu', text)
    text = re.sub(r'\bю', 'yu', text)

    text = re.sub(r'\bЯ', 'Ya', text)
    text = re.sub(r'\bя', 'ya', text)

    mapping = {
        'А': 'A', 'а': 'a',
        'Б': 'B', 'б': 'b',
        'В': 'V', 'в': 'v',
        'Г': 'H', 'г': 'h',
        'Ґ': 'G', 'ґ': 'g',
        'Д': 'D', 'д': 'd',
        'Е': 'E', 'е': 'e',
        'Є': 'Ie', 'є': 'ie',
        'Ж': 'Zh', 'ж': 'zh',
        'З': 'Z', 'з': 'z',
        'И': 'Y', 'и': 'y',
        'І': 'I', 'і': 'i',
        'Ї': 'I', 'ї': 'i',
        'Й': 'I', 'й': 'i',
        'К': 'K', 'к': 'k',
        'Л': 'L', 'л': 'l',
        'М': 'M', 'м': 'm',
        'Н': 'N', 'н': 'n',
        'О': 'O', 'о': 'o',
        'П': 'P', 'п': 'p',
        'Р': 'R', 'р': 'r',
        'С': 'S', 'с': 's',
        'Т': 'T', 'т': 't',
        'У': 'U', 'у': 'u',
        'Ф': 'F', 'ф': 'f',
        'Х': 'Kh', 'х': 'kh',
        'Ц': 'Ts', 'ц': 'ts',
        'Ч': 'Ch', 'ч': 'ch',
        'Ш': 'Sh', 'ш': 'sh',
        'Щ': 'Shch', 'щ': 'shch',
        'Ю': 'Iu', 'ю': 'iu',
        'Я': 'Ia', 'я': 'ia',

        'Ь': '',
        'ь': '',
        '’': '',
        "'": '',
    }

    for ukr, lat in mapping.items():
        text = text.replace(ukr, lat)

    return text


# ============================================================
# .twg transliteration
# ============================================================

def transliterate_twg(text):
    """
    Transliterates values of a .twg file.

    The key before ':' is never transliterated.

    Protected:
        #...#
        (...)
        Inform 7 conditional expressions
        Inform 7 list substitutions

    Not protected:
        TextWorld alternatives:

            [слово|слова]
            [Вихід|Виходи]

        These are transliterated.
    """

    def transliterate_value(value):

        protected = []

        # ----------------------------------------------------
        # Private-use Unicode markers
        #
        # U+E000 and U+E001 belong to the Unicode Private Use Area.
        # They are not Ukrainian letters and are not touched by
        # transliterate_text().
        # ----------------------------------------------------

        MARKER_START = "\ue000"
        MARKER_END = "\ue001"

        def protect(match):
            index = len(protected)

            protected.append(match.group(0))

            return (
                MARKER_START
                + str(index)
                + MARKER_END
            )

        # ----------------------------------------------------
        # Protect all syntax in one processing stage
        # ----------------------------------------------------

        pattern = re.compile(
            r"""
            \#[^#]*\#
            |
            \([^()\n]*\)
            |
            \[([^\]\n]*)\]
            """,
            re.VERBOSE
        )

        def protect_match(match):

            fragment = match.group(0)

            # -----------------------------------------------
            # #...#
            # -----------------------------------------------

            if fragment.startswith("#"):
                return protect(match)

            # -----------------------------------------------
            # (...)
            # -----------------------------------------------

            if fragment.startswith("("):
                return protect(match)

            # -----------------------------------------------
            # [...]
            # -----------------------------------------------

            content = match.group(1)

            if content is None:
                return fragment

            lower = content.lower().strip()

            # Inform 7 conditional syntax
            if (
                lower.startswith("if ")
                or lower.startswith("else if ")
                or lower == "else"
                or lower == "otherwise"
                or lower == "end if"
                or lower.startswith("end if")
            ):
                return protect(match)

            # Inform 7 list substitutions
            if (
                "a list of things" in lower
                or "list of things" in lower
                or "is-are a list of things" in lower
                or lower.startswith("a list")
                or lower.startswith("list ")
                or lower.startswith("the list")
            ):
                return protect(match)

            # TextWorld linguistic alternatives:
            #
            # [Вихід|Виходи]
            # [веде|ведуть]
            #
            # These are transliterated.
            return fragment

        # ----------------------------------------------------
        # Protect syntax
        # ----------------------------------------------------

        value = pattern.sub(
            protect_match,
            value
        )

        # ----------------------------------------------------
        # Transliterate everything which is not protected
        # ----------------------------------------------------

        value = transliterate_text(value)

        # ----------------------------------------------------
        # Restore protected fragments
        # ----------------------------------------------------

        for i, original in enumerate(protected):

            marker = (
                MARKER_START
                + str(i)
                + MARKER_END
            )

            if marker not in value:
                raise RuntimeError(
                    f"Protected fragment {i} was lost "
                    f"during transliteration."
                )

            value = value.replace(
                marker,
                original
            )

        # ----------------------------------------------------
        # Safety check
        # ----------------------------------------------------

        if MARKER_START in value or MARKER_END in value:
            raise RuntimeError(
                "Internal protection marker remained "
                "in transliterated text."
            )

        return value

    # ========================================================
    # Process .twg line by line
    # ========================================================

    result = []

    for line in text.splitlines(keepends=True):

        # ----------------------------------------------------
        # Empty line
        # ----------------------------------------------------

        if not line.strip():
            result.append(line)
            continue

        # ----------------------------------------------------
        # Comment
        # ----------------------------------------------------

        if line.lstrip().startswith("#"):
            result.append(line)
            continue

        # ----------------------------------------------------
        # .twg definition
        # ----------------------------------------------------

        if ":" in line:

            key, value = line.split(":", 1)

            # Key is preserved.
            # Only value is transliterated.
            result.append(
                key + ":" + transliterate_value(value)
            )

        else:

            # Lines without ':' are preserved.
            result.append(line)

    return "".join(result)


# ============================================================
# Main
# ============================================================

def main():

    if len(sys.argv) != 3:
        print(
            "Usage: python ua_translit.py "
            "<input_file> <output_file>"
        )
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    try:

        # ----------------------------------------------------
        # Read source
        # ----------------------------------------------------

        with open(
            input_file_path,
            "r",
            encoding="utf-8"
        ) as f:
            source = f.read()

        # ----------------------------------------------------
        # Transliterate
        # ----------------------------------------------------

        result = transliterate_twg(source)

        # ----------------------------------------------------
        # Safety check
        # ----------------------------------------------------

        if "@@PROTECTED_" in result:
            raise RuntimeError(
                "Unexpected @@PROTECTED_N@@ marker "
                "found in output."
            )

        # ----------------------------------------------------
        # Write result
        # ----------------------------------------------------

        with open(
            output_file_path,
            "w",
            encoding="utf-8"
        ) as f:
            f.write(result)

        print(
            f"Successfully transliterated "
            f"'{input_file_path}' to '{output_file_path}'"
        )

    except FileNotFoundError:

        print(
            f"Error: Input file not found at "
            f"'{input_file_path}'"
        )
        sys.exit(1)

    except Exception as e:

        print(
            f"An unexpected error occurred: {e}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()