import sys, types, os, json
import numpy as np
m=types.ModuleType("ament_index_python"); pk=types.ModuleType("ament_index_python.packages")
pk.get_package_share_directory=lambda n: "/home/user/G1/g1pilot"
m.packages=pk; sys.modules["ament_index_python"]=m; sys.modules["ament_index_python.packages"]=pk
sys.path.insert(0,"/home/user/G1/g1pilot")
from g1pilot.utils.ik_solver import G1IKSolver
from g1pilot.manipulation.arm_geometry import ArmGeometry, HAND_LINK_MIN, _geometry_points
import pinocchio as pin
PKG="/home/user/G1/g1pilot"
out={}
for name,u in [("inspire","g1_29dof_inspire_ftp.urdf"),("haken","g1_29dof_hand_haken.urdf")]:
    ik=G1IKSolver(urdf_path=os.path.join(PKG,"description_files/urdf",u), mesh_dir=os.path.dirname(PKG), debug=False)
    g=ArmGeometry(ik.model, ik.collision_model)
    side="left"; sp=g.spheres[side]
    sel=(sp["link"]>=HAND_LINK_MIN)&np.isin(np.arange(len(sp["r"])),sp["env_idx"])
    # nur wrist_yaw (link 6) und wrist_pitch (5)
    model=ik.model; data=pin.Data(model); q0=pin.neutral(model)
    pin.forwardKinematics(model,data,q0); pin.updateFramePlacements(model,data)
    jids=g.chain[side]["jids"]
    # Kugeln liegen im Frame ihres Kettengelenks; nach wrist_yaw (k=6) umrechnen
    C=[];R=[]
    for c,r,k in zip(sp["c"][sel],sp["r"][sel],sp["link"][sel]):
        T=data.oMi[jids[6]].inverse()*data.oMi[jids[k]]
        C.append(np.array(T.rotation)@c+np.array(T.translation)); R.append(r)
    # Mesh-Punkte der Handgeometrien im wrist_yaw-Frame
    subtree=set(model.subtrees[jids[6]])|set(model.subtrees[jids[5]])
    polys=[]; meshes=[]
    for go in ik.collision_model.geometryObjects:
        if go.parentJoint not in subtree: continue
        pts=_geometry_points(go.geometry)
        if pts is None: continue
        T=data.oMi[jids[6]].inverse()*data.oMi[go.parentJoint]*go.placement
        P=pts@np.array(T.rotation).T+np.array(T.translation)
        tris=[]
        if type(go.geometry).__name__=="Convex":
            g=go.geometry
            tris=[[int(g.polygons(i)[j]) for j in range(3)] for i in range(int(g.num_polygons))]
        polys.append(P.tolist()); meshes.append({"v":P.tolist(),"f":tris})
    out[name]={"c":np.array(C).tolist(),"r":R,"polys":polys,"tcp":sp["tcp"].tolist(),"n":int(sel.sum()),"meshes":meshes}
    print(name,"Kugeln",int(sel.sum()),"Geometrien",len(polys))
json.dump(out,open(sys.argv[1],"w"))
