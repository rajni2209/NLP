import torch
import numpy as np
from PIL import Image
import hashlib


def prompt_to_seed(prompt: str) -> int:
    """Convert prompt text into a deterministic seed."""
    h = hashlib.sha256(prompt.encode()).hexdigest()
    return int(h[:8], 16)


def generate_art(prompt: str, width: int, height: int, seed: int, output_path: str):
    # If seed not given, derive from prompt
    if seed == 0:
        seed = prompt_to_seed(prompt)

    torch.manual_seed(seed)

    # Create coordinate grid
    y = torch.linspace(-3, 3, steps=height).view(-1, 1).repeat(1, width)
    x = torch.linspace(-3, 3, steps=width).view(1, -1).repeat(height, 1)

    # Base noise
    noise = torch.randn(height, width) * 0.15

    # Prompt affects pattern style
    style_value = (sum(ord(c) for c in prompt) % 10) + 1

    # Artistic pattern (procedural "AI-like")
    pattern = (
        torch.sin(x * style_value) +
        torch.cos(y * (style_value + 1)) +
        torch.sin((x**2 + y**2) * 0.5 * style_value)
    )

    # Combine with noise
    img = (pattern * 2.0) + noise

    # Normalize to 0-255
    img = img - img.min()
    img = img / img.max()
    img = img ** 0.8
    img = (img * 255).clamp(0, 255).byte()

    # Make RGB image by shifting channels
    r = img
    g = torch.roll(img, shifts=20, dims=1)
    b = torch.roll(img, shifts=40, dims=0)

    rgb = torch.stack([r, g, b], dim=-1).cpu().numpy().astype(np.uint8)

    image = Image.fromarray(rgb, mode="RGB")
    image.save(output_path)
