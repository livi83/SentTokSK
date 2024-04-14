from setuptools import setup, find_packages

setup(
    name='SentTokSK',
    version='1.0.0',
    description='A sentence tokenizer based on regular expressions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Lívia Kelebercová',
    author_email='livia.kelebercova@gmail.com',
    url='https://github.com/livi83/SentTokSK',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
