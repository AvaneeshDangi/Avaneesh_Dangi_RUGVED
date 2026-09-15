import math
import matplotlib.pyplot as plt


x = 0.0
y = 0.0
theta = 0.0


dt = 0.01


trajectory = [(x, y, theta)]

print("Enter velocity commands:")
print("v omega duration")
print("Example: 1 0.5 4")
print("Enter done to finish")



while True:

    command = input("Command: ")

    if command.lower() == "done":
        break

    parts = command.split()

    v = float(parts[0])
    omega = float(parts[1])
    duration = float(parts[2])


    print(
        f"Before: "
        f"x = {x:.2f}, "
        f"y = {y:.2f}, "
        f"theta = {math.degrees(theta):.2f}°"
    )


    steps = int(duration / dt)


    for i in range(steps):

        x = x + v * math.cos(theta) * dt
        y = y + v * math.sin(theta) * dt
        theta = theta + omega * dt


        trajectory.append((x, y, theta))


    print(
        f"After:  "
        f"x = {x:.2f}, "
        f"y = {y:.2f}, "
        f"theta = {math.degrees(theta):.2f}°"
    )



x_values = [point[0] for point in trajectory]
y_values = [point[1] for point in trajectory]



plt.figure(figsize=(8, 6))

plt.plot(
    x_values,
    y_values,
    linewidth=2,
    label="Robot Trajectory"
)


plt.scatter(
    x_values[0],
    y_values[0],
    s=100,
    marker="o",
    label="Start"
)


plt.scatter(
    x_values[-1],
    y_values[-1],
    s=100,
    marker="X",
    label="End"
)

plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.title("Continuous Unicycle Model")
plt.grid(True)
plt.axis("equal")
plt.legend()

plt.show
