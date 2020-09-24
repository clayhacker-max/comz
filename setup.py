from setuptools import *
deskipsi = """
comz python only obfuscator
# How to Install 
$ git clone https://github.com/clayhacker-max
$ cd comz
$ pip2 install .
$ comz --help or comz -h

# compile Standar 
$ comz -i file -c 1 -o outfile

# Parsing
-i : file input
-c : compile script number 1 ~ 26
-e : compile python header
-o : outfile saving
-t : show code obfuscator

"""
# configurasi
setup(
	name="comz",
	version="1.6",
	description="python source code obfuscator. only obfuscator",
	long_description=deskipsi,
	author="Mr.Gaming",
	author_email="clayhackerteam88@gmail.com",
	url="https://github.com/clayhacker-max",
	py_modules = ["comz"],
	keywords=["encode","uno","pvp","obfus"],
	packages = find_packages(),
	include_package_data=True,
	license="MIT",
	zip_safe=False,
	platform="Linux",
	entry_points={'console_scripts': ['comz=comz.only_run:com']}
)