from setuptools import setup, find_packages

setup(
    name='quantum_firmware_optimization',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'psutil',
        'py-cpuinfo',
        'pySMART',
        'tensorflow',
        'tensorflow_quantum',
        'cirq',
        'qiskit',
        'pennylane'
    ],
)