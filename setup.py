from setuptools import setup, find_packages

setup(
    name='ruSpam',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'torch',
        'transformers'
    ],
    description='A simple spam detection library using a pre-trained model from Hugging Face',
    author='NeuroSpaceX',
    author_email='totoshkus@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
