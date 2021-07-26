from setuptools import Extension

def build(setup_kwargs: dict):
    setup_kwargs["ext_modules"] = [
        Extension(
            "addresses._expand",
            sources=["addresses/pyexpand.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._parser",
            sources=["addresses/pyparser.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._token_types",
            sources=["addresses/pytokentypes.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._tokenize",
            sources=["addresses/pytokenize.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._normalize",
            sources=["addresses/pynormalize.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._near_dupe",
            sources=["addresses/pyneardupe.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "addresses._dedupe",
            sources=["addresses/pydedupe.c", "addresses/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
    ]
