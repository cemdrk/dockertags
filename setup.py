import setuptools

from src import VERSION


setuptools.setup(
    name="dockertags",
    version=VERSION,
    description="List all tags for a Docker image on a remote registry",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": ["dockertags=src.__main__:main"],
    },
    license="MIT",
    author="cemdrk",
    author_email="cemdrk@github.com",
    url="https://github.com/cemdrk/dockertags",
    project_urls={
        "Bug Tracker": "https://github.com/cemdrk/dockertags/issues",
    },
    packages=[
        "src",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
