from conan.packager import ConanMultiPackager
import platform

if __name__ == "__main__":
    builder = ConanMultiPackager()
    shared_option = "IrrXML:shared" if platform.system() != "Windows" else None
    builder.add_common_builds(shared_option_name=shared_option, pure_c=False)
    builder.run()
