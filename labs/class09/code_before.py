"""A class that provides a method to sum all digit characters in a given string."""
class SumDigits:
    def sum_digits(self, text):
        # Convertir a string si es un número
        if isinstance(text, int):
            text = str(text)
        return sum(int(c) for c in text if c.isdigit())
