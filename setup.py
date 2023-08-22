import sys
from setuptools import setup

if sys.version_info[:3] < (3, 0, 0):
    print("Requires Python 3 to run.")
    sys.exit(1)

setup(
    name="gchat",
    version="1.9.0",
    description="Command-line tool using ChatGPT",
    url="https://github.com/petterobam/GPT-CLI",
    author="petterobam",
    author_email="petterobam@gmail.com",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Natural Language :: English",
        "License :: OSI gchatroved :: MIT License",
        "Programming Language :: Python"
    ],
    keywords="chatgpt cli commandline",
    include_package_data=True,
    packages=["gchat", "gchat.utilities"],
    entry_points={"console_scripts": ["gchat = gchat.gchat:main"]},
    install_requires=["revChatGPT", "pygments"],
    requires=["revChatGPT", "pygments"],
    python_requires=">=3.10",
    license="MIT"
)
