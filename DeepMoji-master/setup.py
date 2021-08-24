from setuptools import setup

setup(
    name='deepmoji',
    version='1.0',
    packages=['deepmoji'],
    description='DeepMoji library',
    include_package_data=True,
    install_requires=[
        'emoji==0.4.5',
        'h5py>=2.7.1',
        'Keras>=2.1.2',
        'scikit-learn>=0.19.1',
        'text-unidecode==1.0',
    ],
)
