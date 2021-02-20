from lib.analyser import ComponentAnalyser
from lib.config import Config
from lib.reader import DependencyReader

root_project_path = 'Users/.../PATH_TO_YOUR_PROJECT'
reader = DependencyReader(
    config=Config(
        file_extension='.kt',
        ignore_words=['test',
                      'button',
                      'gradle'],
        root_packages=['com.example.company'],
        ignore_packages=['kotlinx']
    ),
    root_project_path=root_project_path)

reader.analyse()

dependencies = reader.get_dependencies()
for i in dependencies:
    print(i)
analyser = ComponentAnalyser(dependencies)


print(len(analyser.get_unstable_components()))