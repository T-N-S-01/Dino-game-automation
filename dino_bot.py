import argparse
import time

import cv2
import numpy as np
from PIL import ImageGrab


def detect_obstacle(frame: np.ndarray, threshold: int, min_pixels: int) -> bool:
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    obstacle_pixels = int(np.sum(gray < threshold))
    return obstacle_pixels >= min_pixels


def capture_roi(x: int, y: int, width: int, height: int) -> np.ndarray:
    image = ImageGrab.grab(bbox=(x, y, x + width, y + height))
    return np.array(image)


def run_bot(
    x: int,
    y: int,
    width: int,
    height: int,
    threshold: int,
    min_pixels: int,
    jump_key: str,
    interval: float,
) -> None:
    import pyautogui

    print("Starting in 2 seconds. Focus the Chrome Dino game window.")
    time.sleep(2)
    print("Bot running. Press Ctrl+C to stop.")

    while True:
        frame = capture_roi(x, y, width, height)
        if detect_obstacle(frame, threshold, min_pixels):
            pyautogui.press(jump_key)
            time.sleep(interval)
        else:
            time.sleep(0.01)


def main() -> None:
    parser = argparse.ArgumentParser(description="Auto-play Chrome Dino using CV.")
    parser.add_argument("--x", type=int, default=300, help="ROI top-left X coordinate.")
    parser.add_argument("--y", type=int, default=380, help="ROI top-left Y coordinate.")
    parser.add_argument("--width", type=int, default=180, help="ROI width.")
    parser.add_argument("--height", type=int, default=80, help="ROI height.")
    parser.add_argument(
        "--threshold",
        type=int,
        default=120,
        help="Grayscale threshold for obstacle pixels.",
    )
    parser.add_argument(
        "--min-pixels",
        type=int,
        default=120,
        help="Minimum dark pixels to classify as obstacle.",
    )
    parser.add_argument("--jump-key", default="space", help="Key used to jump.")
    parser.add_argument(
        "--interval",
        type=float,
        default=0.08,
        help="Delay after jump to avoid repeated triggers.",
    )
    args = parser.parse_args()

    run_bot(
        x=args.x,
        y=args.y,
        width=args.width,
        height=args.height,
        threshold=args.threshold,
        min_pixels=args.min_pixels,
        jump_key=args.jump_key,
        interval=args.interval,
    )


if __name__ == "__main__":
    main()
