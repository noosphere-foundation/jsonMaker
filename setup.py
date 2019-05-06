from setuptools import setup, find_packages
setup(
    name='jsonMaker',  # Required
    version='1.0.4',  # Required
    url='https://github.com/noosphere-tech/jsonMaker',  # Optional
    author='Noosphere Foundation',  # Optional
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),  # Required
    install_requires=['nooCrypto'],  # Optional
)
