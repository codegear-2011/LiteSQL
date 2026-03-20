from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = Path("/storage/emulated/0/python/LiteSQL/README.md").read_text(encoding="utf-8")

setup(
    name='litesql',  # 🔥 project name (unique হওয়া ভালো)
    version='0.1.0',  # version ঠিকভাবে দাও
    packages=find_packages(),

    install_requires=[],

    entry_points={
        'console_scripts': [
            'litesql=litesql.main:main',  # ����MAIN MAGIC
        ],
    },

    author='CODE GEAR P.V.T L.T.D',
    author_email='duttaarin11@outlook.com',

    description='LiteSQL CLI database tool',
    long_description=long_description,
    long_description_content_type='text/markdown',

    license='MIT',

    project_urls={
        'Source': 'https://github.com/codegear-2011/litesql'
    },
)