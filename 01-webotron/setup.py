from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Paul Hodge',
    author_email='frpaulh@gmail.com',
    description='webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+'
    packages=['webotron'],
    url='https://github.com/hodgeconsulting/automating-aws-with-python/tree/master/01-webotron/webotron'
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
