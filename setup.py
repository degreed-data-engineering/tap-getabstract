from setuptools import setup, find_packages


setup(
    name="tap-getabstract",
    version=0.1,
    description="Getabstract for Degreed taps in Meltano",
    author="Degreed",
    author_email="",
    url="https://github.com/degreed-data-engineering/tap-getabstract",
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    classifiers=[],
    zip_safe=False,
)
