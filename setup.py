from setuptools import setup, find_packages

setup(
    name="moduleB",              # Nom officiel du module
    version="1.0.0",             # Sa version (pour le versionning)
    packages=find_packages()    # Auto-détection des sous-packages
)
