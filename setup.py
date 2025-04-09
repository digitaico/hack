from setuptools import setup, find_packages

setup(
    name='bluetooth_dauther',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['pybluez'],
    entry_points={ 'console_scripts':['deauth_speakers=Deauther:SpeakerDeauthorizerRunner.run',], },
    author='DIGITAI',
    author_email='jea.data@gmail.com',
    description='A tool to Deauthenticate loud bluetooth speakers played by anthropomorphic monkeys.',
    long_description=open('README.md').read() if os.path.exists('README.md') else '',
    long_description_content_type='text/markdown',
    url='https://github.com/digitaico/hack',
)
