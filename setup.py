from setuptools import setup


setup(
    name='cldfbench_dplace-datasets-modis',
    py_modules=['cldfbench_dplace-datasets-modis'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'dplace-datasets-modis=cldfbench_modis:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
