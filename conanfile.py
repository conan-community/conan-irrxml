from conans import ConanFile, CMake, tools
import os


class IrrxmlConan(ConanFile):
    name = "irrxml"
    version = "1.2"
    license = "Public Domain"
    homepage = "http://www.ambiera.com/irrxml"
    url = "https://github.com/conan-community/conan-irrxml"
    description = "irrXML is a simple and fast open source xml parser for C++"
    exports = ["PUBLIC_DOMAIN_LICENSE.md", "LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
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

    def package(self):
        # The library's license is not included in source code download from homepage
        tools.download(self.homepage + "/license.html", os.path.join("licenses", "license"))
        self.copy(pattern="*license*", dst="licenses", keep_path=False, ignore_case=True)
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

        if self.options.shared:
            self.copy("*.dll", src="bin", dst="bin", keep_path=False)
            self.copy("*.so*", dst="lib", keep_path=False)
            self.copy("*.dylib*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
