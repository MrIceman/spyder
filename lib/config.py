class Config:

    def __init__(self,
                 file_extension: str,
                 ignore_words,
                 root_packages,
                 ignore_packages
                 ):
        self.file_extension = file_extension
        self.ignore_words = ignore_words
        self.root_packages = root_packages
        self.ignore_packages = ignore_packages
