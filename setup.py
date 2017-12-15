from setuptools import setup

setup(
    name='snipsbabycare',
    version='1.0',
    description='Baby Care skill for Snips',
    author='Joseph Dureau',
    author_email='joseph.dureau@snips.ai',
    url='https://github.com/JDureau/snips-baby-care',
    download_url='',
    license='MIT',
    install_requires=[
        'requests==2.6.0'
    ],
    keywords=['snips'],
    packages=['snipsbabycare'],
    package_data={'snipsbabycare': ['Snipsspec']},
    include_package_data=True,
)
