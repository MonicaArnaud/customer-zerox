from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys


class InstallSystemDependencies(install):
    def run(self):
        try:
            subprocess.check_call(
                [sys.executable, "-m", "py_zerox.scripts.pre_install"])
        except subprocess.CalledProcessError as e:
            print(f"Pre-install script failed: {e}", file=sys.stderr)
            sys.exit(1)
        install.run(self)


setup(
    name="custom-zerox",
    cmdclass={
        "install": InstallSystemDependencies,
    },
    version="0.0.8",
    packages=find_packages(where="py_zerox"),  # Specify the root folder
    package_dir={"": "py_zerox"},  # Map root directory
    include_package_data=True,
    description="Custom OCR library with support for custom API endpoints",
    author="Custom Zerox Team",
    author_email="custom@zerox.com",
    url="https://github.com/your-username/custom-zerox",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.11",
)
