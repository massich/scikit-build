
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

from .. import cmaker


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        try:
            if not self.build_base or self.build_base == 'build':
                self.build_base = cmaker.SETUPTOOLS_INSTALL_DIR
        except AttributeError:
            pass
        _bdist_wheel.finalize_options(self)
