from setuptools import setup,find_packages
setup(
    name="dialogflowpy-webhook",
    version="0.0.1",
    description="A Python module for parsing and creating Dialogflow Requests and Responses",
    url="https://github.com/vishalbala-nps/dialogflowpy-webhook",
    author="Vishal Balasubramanian",
    author_email="vishal.bala.test@gmail.com",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3",
    keywords=["dialogflow","flask","django","fulfillment","webhook","api","python"],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ]
)