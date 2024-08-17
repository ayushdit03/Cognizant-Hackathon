import platform
from setuptools import setup

dependencies = []
if platform.system() == "Windows":
    dependencies.append("pywin32==306")

setup(
    name="your-package-name",
    install_requires=dependencies,
    # other setup options...
)
