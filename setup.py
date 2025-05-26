from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="rooport",
    version="1.0.0",
    author="ROOPORT Development Team",
    author_email="contact@rooport.dev",
    description="The Ultimate Agentic Coding Tool - AI-enhanced development assistant",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tgf-between-your-legs/rooport",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-asyncio",
            "black",
            "flake8",
            "mypy",
            "isort",
        ],
    },
    entry_points={
        "console_scripts": [
            "rooport=rooport.cli.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "rooport": [
            "config/*.json",
            "config/*.template",
            "data/*.json",
        ],
    },
    keywords="ai, coding, assistant, autonomous, rag, machine-learning, development-tools",
    project_urls={
        "Bug Reports": "https://github.com/tgf-between-your-legs/rooport/issues",
        "Source": "https://github.com/tgf-between-your-legs/rooport",
        "Documentation": "https://github.com/tgf-between-your-legs/rooport/tree/main/docs",
    },
)