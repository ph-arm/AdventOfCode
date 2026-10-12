import matplotlib.pyplot as plt

# Read the tiles
with open("input.txt") as f:
    tiles = []
    for line in f:
        if line.strip():
            x, y = map(int, line.strip().split(","))
            tiles.append((x, y))

print(f"Total tiles: {len(tiles)}")

# Extract x and y coordinates
xs = [t[0] for t in tiles]
ys = [t[1] for t in tiles]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 10))

# Plot the polygon outline
polygon_xs = xs + [xs[0]]  # Close the loop
polygon_ys = ys + [ys[0]]
ax.plot(polygon_xs, polygon_ys, "r-", linewidth=2, label="Red tile polygon")

# Plot the red tiles
ax.scatter(xs, ys, c="red", s=50, zorder=5, label=f"Red tiles ({len(tiles)})")

# Add grid
ax.grid(True, alpha=0.3)

# Set labels
ax.set_xlabel("X coordinate")
ax.set_ylabel("Y coordinate")
ax.set_title("Day 9 Part 2: Red Tile Polygon")
ax.legend()

# Make axes equal
ax.set_aspect("equal")

# Show coordinate ranges
print(f"X range: {min(xs)} to {max(xs)} (width: {max(xs) - min(xs)})")
print(f"Y range: {min(ys)} to {max(ys)} (height: {max(ys) - min(ys)})")

plt.tight_layout()
plt.savefig("tiles_plot.png", dpi=150)
print("Plot saved to tiles_plot.png")
plt.show()
