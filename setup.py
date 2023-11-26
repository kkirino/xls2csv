from setuptools import setup

setup(
    name="xls2csv",
    version="0.0.1",
    description="convert xls files to csv format like xlsx-to-csv conversion with xlsx2csv",
    license="MIT",
    author="kkirino",
    install_requires=["xlrd"],
    entry_points={"console_scripts": ["xls2csv = xls2csv:main"]},
)
