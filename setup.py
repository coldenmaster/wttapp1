from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in wttapp1/__init__.py
from wttapp1 import __version__ as version

setup(
	name="wttapp1",
	version=version,
	description="Library Management System",
	author="Wangtao",
	author_email="15894368@qq.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
