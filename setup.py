from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='sg.socialsite',
      version=version,
      description="Configures a Plone 4.1 instance into a SoftwareGuru Social Site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone social website',
      author='Joaquin Rosales',
      author_email='globojorro@gmail.com',
      url='https://github.com/saibatizoku/sg.socialsite',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sg'],
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
