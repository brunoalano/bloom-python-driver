import pybloomd
from distutils.core import setup
setup(
  name = 'bloom-python-driver',
  packages = ['bloom-python-driver'],
  version = pybloomd.__version__,
  description = 'Client library to interface with multiple bloomd servers',
  author = 'Armon Dadgar',
  author_email = 'biz@kiip.me',
  maintainer = 'Bruno Alano',
  maintainer_email = 'bruno@neurologic.com.br',
  url="https://github.com/brunoalano/bloom-python-driver",
  download_url = 'https://github.com/brunoalano/bloom-python-driver/tarball/master',
  keywords = ['bloom', 'filter', 'bloomd'],
  py_modules=['pybloomd'],
  classifiers = [],
)
