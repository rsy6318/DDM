#include <torch/extension.h>
#include <vector>

std::vector<torch::Tensor> closestPointonSurface_cuda_forward(
    torch::Tensor points,
    torch::Tensor f1,
    torch::Tensor f2,
    torch::Tensor f3
);

std::vector<torch::Tensor> closestPointonSurface_forward(
    torch::Tensor points,
    torch::Tensor f1,
    torch::Tensor f2,
    torch::Tensor f3
    ) 
{
    return closestPointonSurface_cuda_forward(points,f1,f2,f3);
}

//int closest_point_on_surface_backward()
//{
//    return 0;
//}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) 
{
  m.def("forward", &closestPointonSurface_forward, "forward (CUDA)");
  //m.def("backward", &closest_point_on_surface_backward, "backward (CUDA)");
}