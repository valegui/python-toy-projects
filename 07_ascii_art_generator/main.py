from PIL import Image


def load_image(image_path, new_width=100):
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    new_height = int(new_width * aspect_ratio * 0.55)
    img = img.resize((new_width, new_height))
    return img


def convert_to_grayscale(img):
    return img.convert("L")


def map_pixels_to_ascii(img):
    ascii_chars = "@%#*+=-:."
    pixels = img.getdata()
    ascii_str = "".join([ascii_chars[pixel // 25] for pixel in pixels])
    return ascii_str


def generate_ascii_art(image_path, new_width=100):
    img = load_image(image_path, new_width=new_width)
    gray_img = convert_to_grayscale(img)
    ascii_str = map_pixels_to_ascii(gray_img)
    ascii_art = "\n".join(
        [ascii_str[i : i + new_width] for i in range(0, len(ascii_str), new_width)]
    )
    return ascii_art


def save_ascii_art(ascii_art, output_path):
    with open(output_path, "w") as f:
        f.write(ascii_art)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate ASCII art from an image")
    parser.add_argument("input_image", type=str, help="Path to the input image")
    parser.add_argument("output_file", type=str, help="Path to the output file")
    parser.add_argument("--width", type=int, default=100, help="Width of the ASCII art")
    args = parser.parse_args()
    ascii_art = generate_ascii_art(args.input_image, args.width)
    save_ascii_art(ascii_art, args.output_file)
    print(f"ASCII art saved to {args.output_file}")
