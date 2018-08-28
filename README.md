# conan-IrrXML

![conan-irrxml image](/images/conan-irrxml.png)

[ ![Download](https://api.bintray.com/packages/conan-community/conan/IrrXML%3Aconan/images/download.svg?version=1.2%3Astable) ](https://bintray.com/conan-community/conan/IrrXML%3Aconan/1.2%3Astable/link)
[![Build Status](https://travis-ci.org/conan-community/conan-irrxml.svg?branch=stable%2F1.2)](https://travis-ci.org/conan-community/conan-irrxml)
[![Build status](https://ci.appveyor.com/api/projects/status/ktwu9099a1i1ikq8?svg=true)](https://ci.appveyor.com/project/pvicente/conan-irrxml)


[Conan.io](https://conan.io) package for [IrrXML](http://www.ambiera.com/irrxml/) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/IrrXML%3Aconan).

## Basic setup

    $ conan install IrrXML/1.2@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    IrrXML/1.2@conan/stable

    [generators]
    txt
    cmake

## License

[MIT License](LICENSE)