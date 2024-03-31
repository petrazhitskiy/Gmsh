# gmsh_generate_mesh.py
import gmsh
import sys
import matplotlib.pyplot as plt
import meshio


def union_mesh(output_file, width, height, mesh_size):
    gmsh.initialize()
    gmsh.model.add("union_example")

    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, 1, 1)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, 0.5, 0.4)

    union = gmsh.model.occ.fragment([(2, rectangle)], [(2, circle)], removeTool=False)

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)

    # Синхронизация геометрии
    gmsh.model.geo.synchronize()

    # Генерация сетки для домена (необязательно)
    gmsh.model.mesh.generate(2)  # 2D сетка

    # Отображаем графический интерфейс
    # gmsh.fltk.run()
    gmsh.write(output_file)

    # Визуализация сетки (необязательно)
    #теперь выводится сразу график из matplotlib, а не открываетсяс gmsh
    #gmsh.fltk.run()

    # Creates graphical user interface
    gmsh.finalize()

def diff_mesh(output_file, width, height, mesh_size):
    gmsh.initialize()
    gmsh.model.add("difference_example")

    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, 1, 1)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, 0.4, 0.4)

    difference = gmsh.model.occ.cut([(2, rectangle)], [(2, circle)], removeTool=True)

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)

    gmsh.write(output_file)
    gmsh.finalize()

def intersec_mesh(output_file, width, height, mesh_size):
    gmsh.initialize()
    gmsh.model.add("intersection_example")

    rectangle = gmsh.model.occ.addRectangle(0, 0, 0, 1, 1)
    circle = gmsh.model.occ.addDisk(0.5, 0.5, 0, 0.4, 0.1)

    intersection = gmsh.model.occ.intersect([(2, rectangle)], [(2, circle)])

    gmsh.model.occ.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.write(" intersec_mesh.msh")
    gmsh.fltk.run()
    gmsh.finalize()

if __name__ == "__main__":
    output_file = sys.argv[1]
    width = float(sys.argv[2])
    height = float(sys.argv[3])
    mesh_size = float(sys.argv[4])
    if output_file == "union_mesh6.msh":
        union_mesh(output_file, width,height,mesh_size)
    elif output_file == "diff_mesh6.msh":
        diff_mesh(output_file, width,height,mesh_size)
    elif output_file ==  "intersec_mesh6.msh":
        intersec_mesh(output_file, width,height,mesh_size)