class Component:
    def __init__(self, name, package=None):
        self.name: str = name
        self.dependencies: [Component] = []
        self.package: str = package
        # describes the instability rating,
        # it's a value between 0 and 1, where 1 means completely
        # unstable and 0 means stable. Stability is defined by
        # |d_out| / |d_out|+|d_in|
        self.instability_rating: float = -1
        # a bum is a component that depends on this component
        self.bums: [Component] = []

    def __repr__(self):
        return f'{self.name} - Dependencies: {len(self.dependencies)} Bums: {len(self.bums)} Stability: {self.instability_rating}'

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)
