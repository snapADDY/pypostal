
from distutils.command.build_ext import build_ext
from setuptools import Extension




class ExtensionBuilder(build_ext):
    def build_extensions(self):
        c = self.compiler
        _compile = c._compile

        def c_compile(obj, src, ext, cc_args, extra_postargs, pp_opts):
            cc_args = cc_args + ["-std=c99"] if src.endswith(".c") else cc_args
            return _compile(obj, src, ext, cc_args, extra_postargs, pp_opts)

        c._compile = c_compile
        build_ext.build_extensions(self)



def build(setup_kwargs: dict):
    setup_kwargs.update({"cmdclass": {"build_ext": ExtensionBuilder}, "ext_modules": [Extension('postal._dedupe',
                      sources=['postal/pydedupe.c', 'postal/pyutils.c'],
                      libraries=['postal'],
                      include_dirs=['/usr/local/include'],
                      library_dirs=['/usr/local/lib'],
                      )]})
