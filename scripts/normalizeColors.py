import csv


def hex_to_rgb(hex_color):
    return int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:], 16)


def normalize_color(color, min_rgb, max_rgb):
    r, g, b = hex_to_rgb(color)
    normalized_r = (r - min_rgb[0]) / (max_rgb[0] - min_rgb[0]) * 255
    normalized_g = (g - min_rgb[1]) / (max_rgb[1] - min_rgb[1]) * 255
    normalized_b = (b - min_rgb[2]) / (max_rgb[2] - min_rgb[2]) * 255
    return "#{:02x}{:02x}{:02x}".format(int(normalized_r), int(normalized_g), int(normalized_b))


def normalize_colors_in_csv(input_csv, output_csv):
    with open(input_csv, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        rows = list(reader)

    # Extract RGB components and find extremes
    rgb_colors = [hex_to_rgb(row[2]) for row in rows]
    min_rgb = [min(values) for values in zip(*rgb_colors)]
    max_rgb = [max(values) for values in zip(*rgb_colors)]

    # Normalizing colors
    for row in rows:
        row.append(normalize_color(row[2], min_rgb, max_rgb))

    # Writing to the output CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header + ['Normalized Color'])
        writer.writerows(rows)


# File paths
input_csv = '../data/emojiColor.csv'
output_csv = '../data/emojiNormalizedColor.csv'

# Execute the function
normalize_colors_in_csv(input_csv, output_csv)
