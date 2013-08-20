from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='tx.tinymce_linguaplone_patch',
      version=version,
      description="Navigate to site root for language neutral content",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='linguaplone tinymce neutral content',
      author='Marek Kralewski',
      author_email='mck@tuxwerk.de',
      url='https://github.com/tuxwerk/tx.tinymce_linguaplone_patch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tx'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
