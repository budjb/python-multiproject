from setuptools import setup

setup(
    name="demo_libs",
    version="1.0",
    packages=["demo_clients"],
    package_dir={"": "src/main"},
    install_requires=["requests"],
)
