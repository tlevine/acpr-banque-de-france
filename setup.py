from distutils.core import setup

setup(name='acpr',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download ACPR Banque de France - Regafi (Financial Firms Register)',
      url='https://github.com/tlevine/acpr-banque-de-france',
      packages=['picklecache','requests','lxml'],
      install_requires = [],
      tests_require = ['nose'],
      version='0.0.1',
      license='AGPL',
)
