# -*- coding: utf-8 -*-

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(name='closestPointonSurface',
      version='2.0.0',
      ext_modules=[
          CUDAExtension('closestPointonSurface', [
              'closest_point_on_surface_cuda.cpp',
              'closest_point_on_surface.cu',
          ]),
      ],
      cmdclass={'build_ext': BuildExtension})
