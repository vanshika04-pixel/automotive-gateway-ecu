with open("adas_camera.txt") as f:
    for line in f:
        cam, obj, dist = line.strip().split(",")
        dist = int(dist)

        if dist < 20:
            print(f"⚠️  ALERT: {obj} detected at {dist}m")
