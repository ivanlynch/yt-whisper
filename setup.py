from setuptools import setup, find_packages

setup(
    version="1.0",
    name="sub",
    packages=find_packages(),
    py_modules=["sub"],
    author="Iván Lynch",
    install_requires=[
        'yt-dlp',
        'openai-whisper'
    ],
    description="Crea subtítulos para tus videos",
    entry_points={
        'console_scripts': ['sub = yt_whisper.cli:main'],
    },
    include_package_data=True,
)
