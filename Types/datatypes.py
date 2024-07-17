from colorama import Fore, Back, Style

def print_tutorial():
    tutorial = {
        "int": "Integer type. Examples: 1, 2, -5",
        "float": "Floating point number. Examples: 1.0, -2.3, 3.14",
        "complex": "Complex number. Examples: 1+2j, -3+4j",
        "bool": "Boolean type. Examples: True, False",
        "str": "String type. Examples: 'hello', 'world'",
        "list": "List type. Examples: [1, 2, 3], ['a', 'b', 'c']",
        "tuple": "Tuple type. Examples: (1, 2, 3), ('a', 'b', 'c')",
        "range": "Range type. Examples: range(5), range(1, 10, 2)",
        "dict": "Dictionary type. Examples: {'key': 'value', 'name': 'Alice'}",
        "set": "Set type. Examples: {1, 2, 3}, {'a', 'b', 'c'}",
        "frozenset": "Immutable set type. Examples: frozenset({1, 2, 3})",
        "bytes": "Bytes type. Examples: b'hello', b'world'",
        "bytearray": "Mutable byte array. Examples: bytearray(b'hello')",
        "memoryview": "Memory view type. Examples: memoryview(b'hello')",
        "NoneType": "None type. Example: None",
        "type": "Type type. Example: type(int), type('hello')",
        "object": "Base type for all classes. Example: object()"
    }
    
    for typename, description in tutorial.items():
        print(f"{typename}:\n  {description}\n")

if __name__ == "__main__":
    Fore.LIGHTMAGENTA_EX + Back.BLACK
    print(Fore.LIGHTMAGENTA_EX + "")
    print_tutorial()
    print(Fore.LIGHTCYAN_EX + "")
    print(type("Hello World"))
