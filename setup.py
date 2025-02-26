from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = """ Create asynchronous and asynchronous task
                    queues that run on a schedule... symantically """

setup(
    name="qmate",
    version=VERSION,
    author="Digital Kelvin",
    author_email="<qmate@digitalkelvin.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[
        "events",
        "tasks",
        "queue",
        "schedules",
        "scheduling",
        "event loops"
    ]
)
