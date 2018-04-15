#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: zhaole

import time
import yaml
import os
import util
import shutil
from os.path import join
from pkgbase import Pkgbase
print Pkgbase("s")

BUILD_TYPE = {
    "centos": "rpm",
    "euler": "rpm",
    "ubuntu": "deb"
}

class Multipkg(Pkgbase):

    def __init__(self, directory, cleanup=False, force=False,
                 warn_on_error=False, verbose=False, overrides=False,
                 meta="", platform="euler"):
        """
        :param directory: source code directory
        :param cleanup: If true, clean up the workspace
        :param force: No use
        :param warn_on_error: No use
        :param verbose: print build msg
        :param overrides:
        :param meta: some meta msg
        """
        # super(Multipkg, self).__init__(directory)
        self.directory = directory
        # Get index.yaml info
        if platform == "centos" or platform == "euler":
            self.builder = Centosrpm(directory)
        pass

    def build(self):
        """Build rpm according to Platform"""
        self.builder.build()
        pass

class Indexinfo(object):

    def __init__(self, directory, spec_info_file="index.yaml"):
        """
        :param directory: The path to build
        :param spec_file: File Defined spec info
        """
        spec_info_file_path = join(directory, spec_info_file)
        if not os.path.exists(spec_info_file):
            raise Exception("File %s does not exist" % spec_info_file_path)
        with open(spec_info_file_path, "r+") as fd:
            self.data = yaml.load(fd)
        pass

    def _get_platform(self):
        """
        :return: Get the platform (Centos/Suse...)
        """
        pass

class Pkgbuild(object):

    def __init__(self):
    pass

class Centosrpm(Pkgbuild):
    """ Build RPM on Euler/Centos/Redhat """

    def __init__(self, directory):
        """ initialize """
        # Create Build dir
        self.builddir = join("/tmp", time.time())
        self._create_builddir()
        self.info = Indexinfo(directory)
        self.file_dir = os.path.split(__file__)
        pass

    def _create_builddir(self):
        os.mkdir(self.builddir, 777)
        os.mkdir(join(self.builddir, "BUILD"), 777)
        os.mkdir(join(self.builddir, "BUILDROOT"), 777)
        os.mkdir(join(self.builddir, "RPMS"), 777)
        os.mkdir(join(self.builddir, "SPEC"), 777)
        os.mkdir(join(self.builddir, "SRPMS"), 777)

    def _write_spec(self):
        """ Output info to *.spec """
        specfile = join(self.build(), "spec")
        spec_template = join(self.file_dir, "templates/euler.spec.template")
        shutil.copyfile(spec_template, specfile)

        with open(specfile, "a+") as fd:
            fd.write()
        pass

    def build(self):
        """ Build rpm with rpmbuild ops """
        util.exe_cmd("rpmbuild")
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        shutil.rmtree(self.builddir)
        pass