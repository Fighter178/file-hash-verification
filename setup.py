from setuptools import setup, find_packages


setup(
    name='file-hash-verification',
    version='0.1',
    license='MIT',
    author="TheTrueLuckyCoder",
    author_email='unset',
    packages=find_packages(['pyAesCrypt', 'hashlib']),
    keywords='file verification',
    install_requires=[
          'pyAesCrypt',
          'hashlib',
      ],

)
