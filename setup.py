import setuptools
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
__version__ = '0.0.0'
REPO_NAME = 'TextSummerizer-EndToEnd'
AUTHOR_USER_NAME = "kibru9399"
SRC_REPO = 'text_summarizer'
AUTHOR_EMAIL = 'kibrutemesgen15@gmail.com'

setuptools.setup(
    name=SRC_REPO, 
    version=__version__,
    description="A text summarizer using huggingface library.",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL, 
    Long_description=long_description,
    Long_description_conent='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}', 
    project_url = {
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues'
    },
    package_dir={'':"src"}, 
    packages=setuptools.find_packages(where='src')


)


