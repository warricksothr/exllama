from setuptools import setup, Extension
from torch.utils import cpp_extension

setup(
    name="exllama",
    version="0.0.1",
    install_requires=[
        "torch",
    ],
    packages=["exllama"],
    py_modules=["exllama"],
    ext_modules=[
        cpp_extension.CUDAExtension(
            "exllama_ext",
            [
                "exllama_ext/cuda_buffers.cu",
                "exllama_ext/cpu_func/rep_penalty.cpp",
                "exllama_ext/cuda_func/column_remap.cu",
                "exllama_ext/cuda_func/half_matmul.cu",
                "exllama_ext/cuda_func/q4v2_matmul.cu",
                "exllama_ext/cuda_func/q4v2_mlp.cu",
                "exllama_ext/cuda_func/q4v2_recons.cu",
                "exllama_ext/cuda_func/q4v2_sequential.cu",
                "exllama_ext/cuda_func/rms_norm.cu",
                "exllama_ext/cuda_func/rope.cu",
                "exllama_ext/exllama_ext.cpp"
            ],
            extra_compile_args={"nvcc": ["-O3"]},
        ),
    ],
    cmdclass={"build_ext": cpp_extension.BuildExtension},
)
