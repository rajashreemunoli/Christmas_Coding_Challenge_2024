import numpy as np


def create_star(size):
    # Ensure the size is odd for symmetry
    if size % 2 == 0:
        size += 1

    # Create a square array with zeros
    star = np.zeros((size, size), dtype=int)

    # Add the center cross
    star[size // 2, :] = 1  # Horizontal line
    star[:, size // 2] = 1  # Vertical line

    # Add diagonal lines
    np.fill_diagonal(star, 1)  # Top-left to bottom-right
    np.fill_diagonal(np.fliplr(star), 1)  # Top-right to bottom-left

    return star


def display_star(star):
    for row in star:
        print(' '.join(['*' if cell else ' ' for cell in row]))


# Set the size of the star
star_size = 9
star = create_star(star_size)
display_star(star)