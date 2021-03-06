import re

from lib.config import Config
from lib.parser.parser import AbstractParser


class KotlinParser(AbstractParser):

    def __init__(self, config: Config):
        self.config = config

    def parse(self, file_path) -> ([(str, str)], bool):
        """
        :param file_path: the file path to the source code
        :return: returns an array of tuples of (package_name, component_name)
        """
        with open(file_path, "r") as f:
            data = f.read()
            return self._parse_dependencies(data)

    def _parse_dependencies(self, raw_code) -> ([(str, str)], bool):
        import_pattern = r'(?<=import.).*'
        dependencies = []
        res = re.findall(import_pattern, raw_code)
        for i in res:
            dependency_str: str = i
            pieces = dependency_str.split('.')
            package = '.'.join(pieces[0:-1])
            is_contained = False
            if self.config.root_packages is not None:
                for j in self.config.root_packages:
                    if j in package:
                        is_contained = True
                if not is_contained:
                    continue
            if package in self.config.ignore_packages:
                continue
                # ignore lower case dependencies as they're most likely extensions
            if pieces[-1].islower():
                continue
            dependency_name = f'.'.join(pieces[-3::])
            dependencies.append((package, dependency_name))
        return dependencies, self.is_abstraction(raw_code)

    def is_abstraction(self, raw_code: str) -> bool:
        regex = '^(public\s|internal\s|)interface|^(abstract)'
        result = re.findall(regex, raw_code, re.MULTILINE)
        return len(result) > 0
