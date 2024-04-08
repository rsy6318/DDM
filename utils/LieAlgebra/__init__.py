import numpy as np
import torch
import torch.nn as nn
from . import sinc, so3, se3


class Reconstruction_point(nn.Module):
    def __init__(self, rotation=None, translation=None,zero_init=False):
        super(Reconstruction_point, self).__init__()
        if zero_init:
            tp = np.random.randn(3)
            tp = tp / np.linalg.norm(tp) * 0
            tp_translation = np.random.randn(3)* 0
            self.parameters_ = nn.Parameter(
                    torch.from_numpy(
                        np.concatenate([0.001 * tp, tp_translation],
                                    0).astype(np.float32)))
    
        else:
            if rotation is None or translation is None:
                tp = np.random.randn(3)
                tp = tp / np.linalg.norm(tp) #* 0
                tp_translation = np.random.randn(3)* 0.001
                self.parameters_ = nn.Parameter(
                    torch.from_numpy(
                        np.concatenate([0.001 * tp, tp_translation],
                                    0).astype(np.float32)))
            else:
                Trans = torch.zeros(4, 4)
                Trans[:3, :3] = rotation.reshape(3, 3)
                Trans[:3, 3] = translation.reshape(3)
                tp = torch.rand(6) * 0.6
                self.parameters_ = nn.Parameter(se3.log(Trans).reshape(-1) + tp)

    def Transform(self):
        return se3.exp3(self.parameters_)

    def forward(self, points, points_neighbors):
        R, T = self.Transform()
        update_points = points @ R + T.reshape(1, 1, 3)
        if points_neighbors is not None:
            points_neighbors = points_neighbors @ R + T.reshape(1, 1, 3)
            points_neighbors=points_neighbors.reshape(-1, 9)

        return update_points.reshape(-1, 3), points_neighbors
