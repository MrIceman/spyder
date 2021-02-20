from abc import ABC


class AbstractParser(ABC):

    # TODO add a model like "ComponentMetaInfo"
    def parse(self, file_path: str) -> [(str, str)]:
        """
        parse must return an array of tuples (str, str, bool) where the first element indicates the package name and the second
        one the name of the component, the third parameter indicates whether the component
        is an abstraction or not
        The file_path is the absolute path to the file that needs to be parsed
        """
        pass
