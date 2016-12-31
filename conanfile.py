from conans import ConanFile
from conans.tools import download, unzip


class BoostProcessConan(ConanFile):
    name = "boost-process"
    version = "0.5.0"
    url = "https://github.com/eliaskousk/boost-process.git"
    license = "MIT"
    author = "Boost Process Authors"
    settings = None  # header only
    requires = "Boost/1.63.0@eliaskousk/stable"
    options = {}
    default_options = []
    exports = "*"

    def build(self):
        del self
        # Do nothing - header only

    def package(self):
        self.copy("*.hpp", dst="include", src="include", keep_path=True)

