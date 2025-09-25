# Implement a function that normalizes Spanish product names for URLs (slugify):
# - lowercase
# - trim spaces
# - replace spaces and slashes with hyphens
# - keep digits and ASCII letters only, remove others
# - replace accented vowels (áéíóúüñ) -> (aeiouun)
# - collapse multiple hyphens into one

def slugify(name: str) -> str:
    """
    Normalize Spanish product names for URLs (slugify):
    - lowercase
    - trim spaces
    - replace spaces and slashes with hyphens
    - keep digits and ASCII letters only, remove others
    - replace accented vowels (áéíóúüñ) -> (aeiouun)
    - collapse multiple hyphens into one

    >>> slugify("")
    ''
    >>> slugify("  Hola   Mundo  ")
    'hola-mundo'
    >>> slugify("Zapatos Ágiles")
    'zapatos-agiles'
    >>> slugify("Camiseta/Verde Claro")
    'camiseta-verde-claro'
    >>> slugify("Producto 123 + Oferta!")
    'producto-123-oferta'
    """
    if not name:
        return ''
    import re
    s = name.lower().strip()
    # replace accented characters
    trans = str.maketrans({
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u',
        'ñ': 'n'
    })
    s = s.translate(trans)
    # replace spaces and slashes with hyphens
    s = re.sub(r"[ \\\/]+", "-", s)
    # remove non-alphanumeric and hyphens
    s = re.sub(r"[^a-z0-9-]", "", s)
    # collapse multiple hyphens
    s = re.sub(r"-+", "-", s)
    # trim hyphens
    s = s.strip("-")
    return s

if __name__ == "__main__":
    import doctest
    doctest.testmod()
