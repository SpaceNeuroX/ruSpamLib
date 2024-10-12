from setuptools import setup, find_packages
from pathlib import Path

readme_path = Path(__file__).parent / 'README.md'
long_description = readme_path.read_text(encoding='utf-8')

setup(
    name='ruSpam',
    version='0.2.9',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    description='A simple spam detection library using a pre-trained model from Hugging Face',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='NeuroSpaceX',
    author_email='totoshkus@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
