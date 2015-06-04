from setuptools import setup

setup(name='xkcdScraper',
      version='0.1',
      description='Download Comics from xkcd',
      long_description= "A module that can download comics from xkcd",
      classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='xkcdScraper xkcd comics downloader',
      url='http://github.com/sam09/xkcdScraper',
      author='Sam Radhakrishnan',
      author_email='sk09idm@gmail@gmail.com',
      license='MIT',
      packages=['xkcdScraper'],
      install_requires=[
          'beautifulsoup4',
          'requests',
      ],
      scripts=['xkcdScraper.py'],
      include_package_data=True,
      zip_safe=False)
