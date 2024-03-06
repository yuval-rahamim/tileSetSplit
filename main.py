from PIL import Image

# Load the tileset image
tileset_image = Image.open("tileset.png")

# Define tile dimensions
tile_width = 16  # Example tile width
tile_height = 16  # Example tile height

# Calculate the number of tiles horizontally and vertically
num_tiles_x = tileset_image.width // tile_width
num_tiles_y = tileset_image.height // tile_height

# Iterate over tiles and save each one as a PNG file
for y in range(num_tiles_y):
    for x in range(num_tiles_x):
        # Define the bounding box for the current tile
        left = x * tile_width
        upper = y * tile_height
        right = left + tile_width
        lower = upper + tile_height
        tile_bbox = (left, upper, right, lower)

        # Extract the current tile
        tile = tileset_image.crop(tile_bbox)

        # Save the tile as a PNG file
        tile.save("tiles\\" + f"tile_{y}_{x}.png")

print("Tiles extracted and saved successfully.")
