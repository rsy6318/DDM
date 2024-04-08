import trimesh
import numpy as np
import gdist
import numba
import torch

def get_deformation_graph_gdist(vertices,gdist_matrix,dist_thres):
    #vertices:      (N,3) torch cuda
    #gdist_matrix:  (N,N) torch cuda
    deformation_nodes=[]
    while vertices.shape[0]>=1:
        gdists=gdist_matrix[0]
        deformation_nodes.append(vertices[0].reshape(1,3))
        keep_index=(gdists>=float(dist_thres))
        vertices=vertices[keep_index]
        gdist_matrix=gdist_matrix[keep_index,:]    
        gdist_matrix=gdist_matrix[:,keep_index]

    deformation_nodes=torch.concat(deformation_nodes,dim=0)
    return deformation_nodes

def calculate_gdist(v,f,dist_thres):
    gdist_matrix=gdist.local_gdist_matrix(v.astype(np.float64),f.astype(np.int32),max_distance = dist_thres*2)
    gdist_matrix=gdist_matrix.toarray()
    gdist_matrix[gdist_matrix==0]=dist_thres*2
    gdist_matrix[np.eye(gdist_matrix.shape[0])==1]=0
    return gdist_matrix

if __name__=='__main__':
    r_ratio=3
    mesh=trimesh.load_mesh('/home/siyuren_21/data1/siyuren_21/p2f_dist/AMA_crane/mesh_0010.obj')
    #graph_nodes=get_deformation_graph(mesh,5)
    #np.savetxt('graph_nodes.xyz',graph_nodes)
    average_edge_length=np.mean(mesh.edges_unique_length)
    dist_thres=float(average_edge_length*r_ratio)

    v=mesh.vertices
    f=mesh.faces

    gdist_matrix=calculate_gdist(v,f,dist_thres)

    deformation_nodes=get_deformation_graph_gdist(torch.from_numpy(v).cuda().float(),
                                                  torch.from_numpy(gdist_matrix).cuda().float(),
                                                  dist_thres)

    np.savetxt('graph_nodes.xyz',deformation_nodes.cpu().numpy())
    
