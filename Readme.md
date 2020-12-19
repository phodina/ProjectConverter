# Project converter for Embedded Projects

A lot of Embedded Projects use proprietary IDEs and build processes. This make any CI/CD painful. Therefore these simple python scripts allow conversion of existing projects into CMake and corresponding linker file for GCC toolchain. Currently supported are *IAR's ewp* and *ARM's KEIL uvprojx* project formats.

## Module description

- [cmake.py](cmake.py) - Cmake and linker file generation
- [converter.py](converter.py) - Argument parsing
- [ewpproject.py](ewpproject) - Parser for IAR's ewp file format
- [uvprojx.py](uvprojx.py) - Parser for ARM's KEIL uvprojx file format

## Prerequisites

Install `python3` on your system run:
```shell
pip install Jinja2
```

## Usage

Run in output dir.

Convert project from IAR:
```
    python converter.py ewp <path to project root>
```
Convert project from ARM's KEIL:
```
    python converter.py uvprojx <path to project root>
```	

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](semver.org) for versioning.

## Authors

- Petr Hodina - *Initial work*

## License

The project is licensed under the [Apache License v2.0](https://www.apache.org/licenses/LICENSE-2.0) - see the [LICENSE.md](LICENSE.md) file for details.

## TODO
- [ ] Package as python module and publish it
- [ ] Seperate templates into submodule
- [ ] Support generation of Makefile
- [ ] Support additional compilers
- [ ] Test on MAC OSX 
- [ ] Arg to specify build directory
- [ ] Add Tests
