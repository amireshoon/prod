from importlib.metadata import entry_points
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prod-amireshoon",
    version="0.0.1",
    author="Amirhossein Meydani",
    author_email="amirhwsin@outlook.com",
    description="Create production package without some files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amireshoon/prod",
    projects_urls={
        "Bug Tracker": "https://github.com/amireshoon/prod/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'prod = prod.prod:version',
        ],
    },
)