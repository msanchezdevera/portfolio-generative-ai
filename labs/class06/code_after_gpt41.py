def slugify(name: str) -> str:
    """
    Normalize Spanish product names for URLs (slugify):
    - Lowercase
    - Trim spaces
    - Replace spaces and slashes with hyphens
    - Keep digits and ASCII letters only, remove others
    - Replace accented vowels (áéíóúüñ) -> (aeiouun)
    - Collapse multiple hyphens into one
    - Return the slug; empty input -> empty string.

    >>> slugify('  Café con Leche  ')
    'cafe-con-leche'
    >>> slugify('Queso/Ñoño 123')
    'queso-nono-123'
    >>> slugify('Mermelada   de   Fresa')
    'mermelada-de-fresa'
    >>> slugify('Té verde 2022/2023')
    'te-verde-20222023'
    >>> slugify('')
    ''
    """
    import re
    if not name:
        return ''
    # Lowercase and trim
    name = name.strip().lower()
    # Replace accented vowels and ñ/ü
    accents = str.maketrans('áéíóúüñ', 'aeiouun')
    name = name.translate(accents)
    # Replace spaces and slashes with hyphens
    name = re.sub(r'[\s/]+', '-', name)
    # Remove all except ASCII letters, digits, and hyphens
    name = re.sub(r'[^a-z0-9-]', '', name)
    # Collapse multiple hyphens
    name = re.sub(r'-{2,}', '-', name)
    # Remove leading/trailing hyphens
    return name.strip('-')
