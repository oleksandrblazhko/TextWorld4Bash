import sys
import re

def transliterate(text):
    """
    Performs Ukrainian to Latin transliteration based on the rules from
    the Resolution of the Cabinet of Ministers of Ukraine No. 55 of January 27, 2010.
    """
    # Special case 'зг' -> 'zgh'
    text = text.replace("Зг", "Zgh").replace("зг", "zgh")

    # Positional rules (at the beginning of a word)
    # Using \b word boundary to match the start of words.
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

    # All other rules (including non-initial positions for the above)
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
        'ь': '',
        '’': '',
        'Ь': '',
    }

    # Apply the main mapping
    for ukr, lat in mapping.items():
        text = text.replace(ukr, lat)

    return text

def main():
    if len(sys.argv) != 3:
        print("Usage: python ua_translit.py <input_file> <output_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            ukrainian_text = f.read()

        transliterated_text = transliterate(ukrainian_text)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(transliterated_text)

        print(f"Successfully transliterated '{input_file_path}' to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: Input file not found at '{input_file_path}'")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
