# coding: utf-8
from setuptools import setup

setup(
    name="pyflowdock",
    version="0.3.35",
    packages=["flowdock", "flowdock.helpers"],
    package_dir={"flowdock": "flowdock"},
    scripts=[],
    install_requires=["requests"],
    package_data={"": []},
    author=u"Eugene “Aeron” Glybin",
    author_email="aeron@aeron.cc",
    url="https://github.com/Aeron/PyFlowdock",
    description="Simple Flowdock APIs wrapper with some useful helpers. "
    "Only Push API (Team Inbox and Chat) and Streaming API available at this moment.",
    license="LGPLv3",
    keywords="flowdock api wrapper",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License "
        "(LGPL)",
        "Topic :: Communications",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
