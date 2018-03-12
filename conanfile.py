from conans import ConanFile, CMake, tools
import os


class IrrXMLConan(ConanFile):
    name = "IrrXML"
    version = "1.2"
    license = "ZLIB"
    homepage = "http://www.ambiera.com/irrxml"
    url = "https://github.com/conan-community/conan-irrxml"
    description = "irrXML is a simple and fast open source xml parser for C++"
    exports = ["LICENSE.md", ]
    exports_sources = ["CMakeLists.txt", "IrrXML.cmake", "FindIrrXML.cmake", "patches/*"]
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

    def configure(self):
        if self.settings.os == "Windows" and self.options.shared:
            raise Exception("%s doesn't build with shared=True in Windows" % self.name)

    def source(self):
        source_url = "http://prdownloads.sourceforge.net/irrlicht/irrxml-%s.zip" % self.version
        tools.get(source_url)
        os.rename("irrxml-%s" % (self.version,), self.source_subfolder)
        # VS in debug need a patch removing original workaround
        tools.patch(patch_file="patches/irrtypes_debug_vs.patch")

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
