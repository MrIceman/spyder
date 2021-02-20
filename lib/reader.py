from os import listdir
from os.path import isfile, join

from lib.parser.kotlin.kotlin import KotlinParser
from model.component import Component
from lib.config import Config


class DependencyReader:

    def __init__(self, config: Config,
                 root_project_path: str):
        self.config = config
        self.root = root_project_path
        self.bums = dict()
        self.component_map: {str: Component} = {}
        # make this configurable
        self.parser = KotlinParser(config)
        # a cache that holds the abstraction for each read file
        self.abstraction_map: {str: bool} = dict()

    def _init_components(self, dir_path):
        entries = listdir(dir_path)
        for e in entries:
            e_low = e.lower()
            ignore = False
            for i in self.config.ignore_words:
                if i in e_low:
                    ignore = True
            if ignore:
                continue

            if isfile(join(dir_path, e)):
                if self.config.file_extension in e_low:
                    """
                        We have a file we want to look at.
                        1. Get the package path endings
                        2. Get a name set by the package path and the name (without the extension)
                        3. Get all dependencies contained within that file by analysing the source code
                        4. Return a list of components that are within the file
                        5. Look up in the Map if such Component exists already, if not then re-create it and add it
                           else re-use it
                       6.  Add all Components as dependency
                       7. Update Map
                    """
                    package_path = '.'.join(dir_path.replace('/', '.').split('.')[-2::])
                    e_filtered = f'{package_path}.{e.replace(self.config.file_extension, "")}'
                    dependencies, is_abstraction = self.parser.parse(join(dir_path, e))
                    comp = self.component_map.get(e_filtered, None)
                    if comp is None:
                        comp = Component(name=e_filtered,
                                         package=package_path,
                                         is_abstraction=is_abstraction)
                    else:
                        self.component_map[e_filtered].is_abstraction = is_abstraction
                    for dep in dependencies:
                        dep_package_name = dep[0]
                        # it is critical to test that dep_component_name has the same structure as e_filtered
                        dep_component_name = dep[1]
                        self.component_map.setdefault(dep_component_name,
                                                      Component(name=dep_component_name,
                                                                package=dep_package_name))

                        comp.add_dependency(self.component_map[dep_component_name])
                        self.component_map[e_filtered] = comp

            else:
                # it's a dir, we can recursively go through the method again
                self._init_components(join(dir_path, e))

    def analyse(self):
        self._init_components(self.root)
        self._compute_metrics()

    def _compute_metrics(self):
        for k, v in self.component_map.items():
            d_out = len(v.dependencies)
            d_in = 0

            for k1, v1 in self.component_map.items():
                if k1 == k:
                    continue
                for c in v1.dependencies:
                    if k == c.name:
                        d_in += 1
                        v.bums.append(v1)

            try:
                """
                |d_out| / |d_out|+|d_in| where |d_out| is the amount
                of outgoing dependencies and |d_in| the amount of
                in going dependencies
                """
                instability_rating = d_out / (d_out + d_in)
            except ZeroDivisionError:
                instability_rating = 0

            v.instability_rating = instability_rating

            # Compute degree of stability
            ac = 0
            for c in v.dependencies:
                if c.is_abstraction:
                    ac += 1
            try:
                """
                A = AC / TC 
                """
                a = ac / d_out
            except ZeroDivisionError:
                a = 0
            v.abstraction_degree = a

    def get_dependencies(self):
        return sorted(self.component_map.values(),
                      key=lambda k: k.instability_rating)
