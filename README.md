## Measuring the Discrepancy between 3D Geometric Models using Directional Distance Fields

[[Arxiv]](https://arxiv.org/abs/2401.09736)

## Installation

```
cd Closest_Point_on_Surface
python set_up.py install
```

## Usage

Here we provide three versions of DirDist, i.e., Point-to-Point, Mesh-to-Mesh, and Mesh-to-Point (in the paper, it is face).

###### Optimize a point cloud according to the reference point cloud

```
from Closest_Point_on_Surface import DirDist_P2P

loss_func=DirDist_P2P()

......
loss=loss_func(src_points,tgt_points)
......
```

###### Optimize a triangle mesh according to the reference triangle mesh

```
from Closest_Point_on_Surface import DirDist_M2M

loss_func=DirDist_M2M()

......
loss=loss_func(src_v,src_f,tgt_v,tgt_f)
......
```

###### Optimize a triangle mesh according to the reference point cloud

```
from Closest_Point_on_Surface import DirDist_M2P

loss_func=DirDist_M2P()

......
loss=loss_func(src_v,src_f,tgt_points)
......
```

## TODO

* [X] Release code.
* [ ] Release examples on the selected applications
  * [ ] Shape Deformation
  * [X] Rigid Registration
  * [X] Non-rigid Registration
  * [ ] Scene Flow Estimation
  * [ ] Human Pose Optimization

## Acknowledgement

We thank the following excellent works including MAC, AMM, NSFP, SCOOP, and MDA for their released codes.

## Citation
```bibtex
@article{ren2024measuring,
  title={Measuring the Discrepancy between 3D Geometric Models using Directional Distance Fields},
  author={Ren, Siyu and Hou, Junhui and Chen, Xiaodong and Xiong, Hongkai and Wang, Wenping},
  journal={arXiv preprint arXiv:2401.09736},
  year={2024}
}
```