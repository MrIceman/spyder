from abc import ABC


class AbstractParser(ABC):
    """
    parse must return an array of tuples (str, str) where the first element indicates the package name and the second
    one the name of the component.
    The file_path is the absolute path to the file that needs to be parsed
    """

    def parse(self, file_path: str) -> [(str, str)]:
        pass
