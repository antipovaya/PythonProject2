
import doctest


def redactor(text):
    """Удаляет из тектса все символы, кроме букв латинского алфавита и пробелов
    >>> redactor("hello world")
    "hello, world"
    """

    result = text.lower()
    for el in result:
        if ord(el) != 32:
            if ord(el) < 97 or ord(el) > 122:
                result = result.replace(el, " ")

    return result


if __name__ == "__main__":
    doctest.testmod(verbose=True)
# redactor('hello world')
