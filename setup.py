from distutils.core import setup

setup(
    name='dhnn',
    version='0.1.0',
    description='Discrete Hopfield Network (DHNN) implemented with Python',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    author='Zeroto521',
    author_email='Zeroto521@gmail.com',
    license="MIT",
    py_modules=['dhnn'],
    requires=['numpy'],
    install_requires=['numpy'],
    url='https://github.com/Zeroto521/DHNN',
    download_url='https://github.com/Zeroto521/DHNN/archive/master.zip',
    keywords=[
        'machine learning',
        'neural networks',
        'hopfield', 'DHNN'
    ]
)