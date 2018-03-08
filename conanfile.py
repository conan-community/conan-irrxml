from conans import ConanFile, CMake, tools
import os


class IrrxmlConan(ConanFile):
    name = "IrrXML"
    version = "1.2"
    license = "Public Domain"
    homepage = "http://www.ambiera.com/irrxml"
    url = "https://github.com/conan-community/conan-irrxml"
    description = "irrXML is a simple and fast open source xml parser for C++"
    exports = ["LICENSE.md", ]
    exports_sources = ["CMakeLists.txt", "IrrXML.cmake", "FindIrrXML.cmake"]
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    source_subfolder = "sources"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = "shared=False", "fPIC=True"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        source_url = "http://prdownloads.sourceforge.net/irrlicht/irrxml-%s.zip?download" % self.version
        tools.get(source_url)
        os.rename("irrxml-%s" % (self.version,), self.source_subfolder)

    def build(self):
        cmake = CMake(self)

        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        if self.settings.os != "Windows":
            cmake.definitions['CMAKE_POSITION_INDEPENDENT_CODE'] = self.options.fPIC

        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        # The library's license is not included in source code download license from homepage
        tools.download(self.homepage + "/license.html", os.path.join("licenses", "license"))
        self.copy(pattern="*license*", dst="licenses", keep_path=False, ignore_case=True)
        self.copy("FindIrrXML.cmake", ".", ".")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
