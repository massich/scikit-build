"""This module defines custom implementation of ``install_lib`` setuptools
command."""

from setuptools.command.install_lib import install_lib as _install_lib

from . import set_build_base_mixin
from ..utils import new_style

from distutils import log as distutils_log


class install_lib(set_build_base_mixin, new_style(_install_lib)):
    """Custom implementation of ``install_data`` setuptools command."""

    def hide_listing(self):
        return (hasattr(self.distribution, "hide_listing")
                and self.distribution.hide_listing)

    def install(self):
        old_threshold = distutils_log._global_log.threshold
        if self.hide_listing():
            distutils_log.set_verbosity(0)
        outfiles = super(install_lib, self).install()
        distutils_log.set_verbosity(old_threshold)
        if outfiles is not None:
            distutils_log.info("copied %d files" % len(outfiles))
