from conans import ConanFile, CMake, tools
import os


class IrrxmlConan(ConanFile):
    name = "irrxml"
    version = "1.2"
    license = "Public Domain"
    homepage = "http://www.ambiera.com/irrxml/"
    url = "https://github.com/conan-community/conan-irrxml"
    description = "irrXML is a simple and fast open source xml parser for C++"
    exports = ["PUBLIC_DOMAIN_LICENSE.md", "LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    source_subfolder = "sources"

    def source(self):
        source_url = "http://prdownloads.sourceforge.net/irrlicht/irrxml-%s.zip?download" % self.version
        tools.get(source_url)
        os.rename("irrxml-%s" % (self.version,), self.source_subfolder)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy(pattern="*LICENSE*", dst="licenses")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
