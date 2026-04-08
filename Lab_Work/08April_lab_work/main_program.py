import threed_figures as tf

print("Select Figure")
print("1. Cube")
print("2. Cuboid")
print("3. Cylinder")
print("4. Cone")
print("5. Sphere")

choice = int(input("Enter your choice: "))

print("\nSelect Operation")
print("1. Curved Surface Area")
print("2. Total Surface Area")
print("3. Volume")

operation = int(input("Enter operation: "))


# -------- Cube --------
if choice == 1:
    a = float(input("Enter side: "))

    if operation == 1:
        print("CSA =", tf.cube_csa(a))

    elif operation == 2:
        print("TSA =", tf.cube_tsa(a))

    elif operation == 3:
        print("Volume =", tf.cube_volume(a))


# -------- Cuboid --------
elif choice == 2:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))

    if operation == 1:
        print("CSA =", tf.cuboid_csa(l,b,h))

    elif operation == 2:
        print("TSA =", tf.cuboid_tsa(l,b,h))

    elif operation == 3:
        print("Volume =", tf.cuboid_volume(l,b,h))


# -------- Cylinder --------
elif choice == 3:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))

    if operation == 1:
        print("CSA =", tf.cylinder_csa(r,h))

    elif operation == 2:
        print("TSA =", tf.cylinder_tsa(r,h))

    elif operation == 3:
        print("Volume =", tf.cylinder_volume(r,h))


# -------- Cone --------
elif choice == 4:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    l = float(input("Enter slant height: "))

    if operation == 1:
        print("CSA =", tf.cone_csa(r,l))

    elif operation == 2:
        print("TSA =", tf.cone_tsa(r,l))

    elif operation == 3:
        print("Volume =", tf.cone_volume(r,h))


# -------- Sphere --------
elif choice == 5:
    r = float(input("Enter radius: "))

    if operation == 1:
        print("CSA =", tf.sphere_csa(r))

    elif operation == 3:
        print("Volume =", tf.sphere_volume(r))