import os 
import subprocess 

baselines = ["gt", "ours", "cache", "tnerf"]

def copy_normals(path, view=None, target_folder = "./images"):
    for b in baselines:
        if b == "gt":
            source = "normals_gt"
            if "captured" in path:
                source = "color_gt"
        else:
            source = "normals_to_use"
            

        source_path = os.path.join(path,b, source, view+".png")
        target_path = os.path.join(target_folder, path.split("/")[-1]+f"_{b}_{view}_normals.png")
        command = f"cp {source_path} {target_path}"
        # print(command)
        subprocess.run(command.split())

if __name__=="__main__":
    # queue = ["statue", "globe", "spheres", "house"]
    queue = ["pots", "peppers", "kitchen", "cornell"]
    captured_folder = "../figures/captured"
    simulated_folder = "../figures/simulation"

    if "statue" in queue:
        copy_normals(f"{captured_folder}/statue", view="0005")
        
    if "globe" in queue:
        copy_normals(f"{captured_folder}/globe", view="0002")
        
    if "spheres" in queue:
        copy_normals(f"{captured_folder}/spheres", view="0005")
    
    if "house" in queue:
        copy_normals(f"{captured_folder}/house", view="0007")
        
    
    if "peppers" in queue:
        copy_normals(f"{simulated_folder}/peppers", view="0026")
        
    if "pots" in queue:
        copy_normals(f"{simulated_folder}/pots", view="0020")
        
    if "cornell" in queue:
        copy_normals(f"{simulated_folder}/cornell", view="0015")
    
    if "kitchen" in queue:
        copy_normals(f"{simulated_folder}/kitchen", view="0031")
        