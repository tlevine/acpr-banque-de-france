from distutils.core import setup

setup(name='acpr',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download ACPR Banque de France - Regafi (Financial Firms Register)',
      url='https://github.com/tlevine/acpr-banque-de-france',
      packages=['acpr'],
      install_requires = ['picklecache','requests','lxml'],
      tests_require = ['nose'],
      scripts = ['bin/acpr'],
      version='0.0.2',
      license='AGPL',
)
