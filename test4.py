import gmsh

# Инициализация Gmsh
gmsh.initialize()

# Создание точек
p1 = gmsh.model.geo.addPoint(0, 0, 0)
p2 = gmsh.model.geo.addPoint(1, 0, 0)
p3 = gmsh.model.geo.addPoint(1, 1, 0)
p4 = gmsh.model.geo.addPoint(0, 1, 0)

# Создание линий
l1 = gmsh.model.geo.addLine(p1, p2)
l2 = gmsh.model.geo.addLine(p2, p3)
l3 = gmsh.model.geo.addLine(p3, p4)
l4 = gmsh.model.geo.addLine(p4, p1)

# Создание контурной петли из линий
curveLoop = gmsh.model.geo.addCurveLoop([l1, l2, l3, l4])

# Использование контурной петли для создания плоской поверхности
planeSurface = gmsh.model.geo.addPlaneSurface([curveLoop])

# Синхронизация геометрии
gmsh.model.geo.synchronize()

# Генерация сетки для домена (необязательно)
gmsh.model.mesh.generate(2)  # 2D сетка

# Визуализация сетки (необязательно)
gmsh.fltk.run()

# Завершение работы с Gmsh
gmsh.finalize()
