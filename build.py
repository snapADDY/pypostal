from setuptools import Extension

def build(setup_kwargs: dict):
    setup_kwargs["ext_modules"] = [
        Extension(
            "pylibpostal._expand",
            sources=["pylibpostal/pyexpand.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._parser",
            sources=["pylibpostal/pyparser.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._token_types",
            sources=["pylibpostal/pytokentypes.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._tokenize",
            sources=["pylibpostal/pytokenize.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._normalize",
            sources=["pylibpostal/pynormalize.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._near_dupe",
            sources=["pylibpostal/pyneardupe.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
        Extension(
            "pylibpostal._dedupe",
            sources=["pylibpostal/pydedupe.c", "pylibpostal/pyutils.c"],
            libraries=["postal"],
            include_dirs=["/usr/local/include"],
            library_dirs=["/usr/local/lib"],
            extra_compile_args=["-std=c99"],
        ),
    ]
