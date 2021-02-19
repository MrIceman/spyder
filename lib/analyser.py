from model.component import Component


class ComponentAnalyser:
    def __init__(self, components: [Component]):
        self.components = components
        self.indexed_components = {i.name: i for i in components}
        self.unstable_components = []

    def get_unstable_components(self):
        """
        Checks unstable dependencies by measuring whether the
        outgoing dependency has a higher stability

        :return:
        """
        if len(self.unstable_components) > 0:
            return self.unstable_components
        print(f'{len(self.components)} components')
        for comp in self.components:
            for dep in comp.dependencies:
                # unfortunately the nested comp dependencies
                # don't have a stability index calculated. Only
                # the indexed ones
                dep_comp = self.indexed_components[dep.name]
                if dep_comp.instability_rating > comp.instability_rating:
                    if comp not in self.unstable_components:
                        self.unstable_components.append(comp)

        return self.unstable_components
