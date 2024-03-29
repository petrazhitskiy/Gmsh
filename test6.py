import gmsh

def create_compound_area():
    gmsh.initialize()

    gmsh.model.add("Compound Area")

    rect_width = 200
    rect_height = 100
    circle_radius = 50
    circle_center = (100, 50, 0)

    # Создаем прямоугольник с помощью OpenCASCADE API
    rect = gmsh.model.occ.addRectangle(0, 0, 0, rect_width, rect_height)
    
    # Создаем круг с помощью OpenCASCADE API, уточняя радиусы по X и Y
    circle = gmsh.model.occ.addDisk(circle_center[0], circle_center[1], 0, circle_radius, circle_radius)  # Теперь указываем ry

    # Выполняем операцию вырезания
    cut, _ = gmsh.model.occ.cut([(2, rect)], [(2, circle)], removeObject=True, removeTool=True)

    gmsh.model.occ.synchronize()

    gmsh.model.mesh.generate(2)

    gmsh.fltk.run()

    gmsh.finalize()

if __name__ == "__main__":
    create_compound_area()
