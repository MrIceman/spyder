class Component:
    def __init__(self, name, package=None, **kwargs):
        self.name: str = name
        self.dependencies: [Component] = []
        self.package: str = package
        # describes the instability rating,
        # it's a value between 0 and 1, where 1 means completely
        # unstable and 0 means stable. Stability is defined by
        # |d_out| / |d_out|+|d_in|
        self.instability_rating: float = -1
        self.abstraction_degree: float = -1
        # a bum is a component that depends on this component
        self.bums: [Component] = []
        self.is_abstraction = kwargs.get('is_abstraction', None)

    def __repr__(self):
        return f'{self.name} - Dependencies: {len(self.dependencies)} Bums: {len(self.bums)} Stability: {self.instability_rating} Abstraction Degree: {self.abstraction_degree}' \
               f' abstraction: {self.is_abstraction}'

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)

    def to_dict(self):
        return {
            'name': self.name,
            'package': self.package,
            'is_abstraction': self.is_abstraction,
            'dependencies': [i.name for i in self.dependencies],
            'bums': [i.name for i in self.bums],
            'instability_rating': self.instability_rating,
            'abstraction_degree': self.abstraction_degree
        }
