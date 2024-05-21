from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="YoloGemma",
    version="0.1.0",
    description="A vision-language model abstraction for object detection and segmentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Adithya S Kolavi",
    packages=find_packages(),
    install_requires=[
        "torch==2.3.0",
        "sentencepiece",
        "tiktoken",
        "accelerate",
        "opencv-python",
        "Pillow",
        "transformers",
        "numpy"
    ],
    entry_points={
        'console_scripts': [
            'download=yolagemma.download_and_quantize:main',
            'main=yolagemma.detect:main',
            'server=yolagemma.server:main',
            'gradio=yolagemma.server:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    license="MIT",
    url="https://github.com/adithya-s-k/YoloGemma",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/YoloGemma/issues",
    },
)
