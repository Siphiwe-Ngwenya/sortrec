from setuptools import setup, find_packages

setup(
    name='sortrec',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='MY python package for perfoming recursions and sorting',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Siphiwe-Ngwenya/sortrec.git',
    author='Siphiwe Ngwenya',
    author_email='ngwenya87@gmai.com'
)
