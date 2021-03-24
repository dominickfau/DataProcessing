import re
import base64
import hashlib

def amendSpacesToString(inputString):
    """Takes a PascalCase string and adds spaces just before each capital letter.

    Args:
        inputString (str): PascalCase string to add spaces to.

    Returns:
        str: Input string with spaces added just before each capital letter.
    """
    words = re.findall("[A-Z][a-z]*", inputString.strip())
    stringList = []
    for word in words:
        stringList.append(word)
    return " ".join(stringList).strip()

def hashPassword(pwd):
    """Hashes password string using this method, Base64.encode(MD5.hash(password))
    Decoded with UTF-8.

    Args:
        pwd (str): Plain text string of the password to hash.

    Returns:
        str: The hashed password string.
    """
    return base64.b64encode(hashlib.md5(pwd.encode()).digest()).decode('utf-8')

def isEven(number):
    """Test if the given number is even.

    Args:
        number (int): Number to test.

    Returns:
        bool: Returns True if even and False otherwise.
    """
    if number % 2:
        return False
    else:
        return True