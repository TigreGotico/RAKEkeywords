import os
import os.path

from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))


def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


def get_version():
    """ Find the version of ovos-core"""
    version = None
    version_file = os.path.join(BASEDIR, 'RAKEkeywords', 'version.py')
    major, minor, build, alpha = (None, None, None, None)
    with open(version_file) as f:
        for line in f:
            if 'VERSION_MAJOR' in line:
                major = line.split('=')[1].strip()
            elif 'VERSION_MINOR' in line:
                minor = line.split('=')[1].strip()
            elif 'VERSION_BUILD' in line:
                build = line.split('=')[1].strip()
            elif 'VERSION_ALPHA' in line:
                alpha = line.split('=')[1].strip()

            if ((major and minor and build and alpha) or
                    '# END_VERSION_BLOCK' in line):
                break
    version = f"{major}.{minor}.{build}"
    if int(alpha):
        version += f"a{alpha}"
    return version


def get_description():
    with open(os.path.join(BASEDIR, "README.md"), "r") as f:
        long_description = f.read()
    return long_description


ENTRY_POINT = f'ovos-rake-keyword-extractor=RAKEkeywords.opm:RakeKeywordExtractor'


setup(
    name='RAKEkeywords',
    version=get_version(),
    packages=['RAKEkeywords'],
    url='https://github.com/OpenJarbas/RAKEkeywords',
    license='Apache2',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='Implementation of RAKE - Rapid Automatic Keyword Extraction',
    long_description=get_description(),
    long_description_content_type="text/markdown",
    entry_points={
        "opm.keywords": ENTRY_POINT
    }
)
