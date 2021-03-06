from conans import ConanFile, CMake
import os


class TestConanPackage(ConanFile):
  settings = "os", "compiler", "build_type", "arch"
  generators = "cmake"

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def test(self):
    os.chdir("bin")
    self.run(".%stest_package" % os.sep)
