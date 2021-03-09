from distutils.core import setup

setup(
    name='oe-build-env',
    version='0.0.1',
    packages=['oe_build_env'],
    package_dir={'': 'src/lib'},
    url='',
    license='MIT',
    author='Jim Broadus',
    author_email='jbroadus@gmail.com',
    description='',
    scripts=['src/bin/builder-bash']
)
