import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='intrinsic_hardness',
    version='0.0.1',
    author='Salil Bavdekar',
    author_email='salil.bavdekar@ufl.edu',
    description='Calculate intrinsic hardness of structures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/salil91/intrinsic-hardness',
    project_urls={
        "Bug Tracker": "https://github.com/salil91/intrinsic-hardness/issues"
    },
    license='MIT',
    packages=['intrinsic_hardness'],
    install_requires=['pymatgen', 'click'],
)
