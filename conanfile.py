from conans import ConanFile, CMake
from conans import tools

class ElfSpyConan(ConanFile):
    name = 'elfspy'
    version = 'master'
    description = 'C++ Testing using spies and fakes for isolation and simulation'
    url = 'https://github.com/Manu343726/elfspy'
    scm = {
      'type': 'git',
      'url': 'https://github.com/Manu343726/elfspy',
      'revision': 'auto'
    }
    settings = 'os', 'arch', 'compiler', 'build_type'

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy('*.h')
        self.copy('*.a', src='src', dst='lib/', keep_path=False)
        self.copy('*.so', src='src', dst='lib/', keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ['elfspy']
