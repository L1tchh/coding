#!/usr/bin/env python3

# =========================
# IMPORT LIBRARY
# =========================
import os
import time
import cv2
from PIL import Image
import numpy as np

# =========================
# INTERPOLASI FRAME
# Membuat perpindahan video lebih halus
# =========================
def interpolate_frames(frame1, frame2, factor):

    # Jika salah satu frame kosong
    if frame1 is None or frame2 is None:
        return frame1 if frame1 is not None else frame2

    # Campur dua frame
    return cv2.addWeighted(frame1, 1 - factor, frame2, factor, 0)


# =========================
# UBAH FRAME MENJADI ASCII
# =========================
def frame_to_ascii(frame, width=80):

    # Ubah jadi grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ambil ukuran asli
    height, width_orig = gray.shape

    # Hitung rasio
    aspect_ratio = height / width_orig

    # Tinggi baru
    new_height = int(aspect_ratio * width * 0.5)

    # Resize
    resized = cv2.resize(gray, (width, new_height))

    # Konversi ke PIL
    img = Image.fromarray(resized)

    # Karakter ASCII
    chars = " .:-=+*#%@"

    # Ambil pixel
    pixels = list(img.getdata())

    # Mapping pixel ke karakter
    ascii_str = ""

    for pixel in pixels:
        index = pixel * (len(chars) - 1) // 255
        ascii_str += chars[index]

    # Pecah menjadi baris
    ascii_img = "\n".join(
        [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]
    )

    return ascii_img


# =========================
# PUTAR VIDEO ASCII
# =========================
def play_video(video_path, max_duration=20, ascii_width=80):

    # Buka video
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"[!] Tidak bisa membuka video: {video_path}")
        return

    # Ambil FPS
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps <= 0:
        fps = 24

    delay = 1 / fps

    # Waktu mulai
    start_time = time.time()

    prev_frame = None

    while True:

        # Batasi durasi
        if time.time() - start_time > max_duration:
            break

        # Baca frame
        ret, frame = cap.read()

        if not ret:
            break

        # Resize biar ringan
        frame = cv2.resize(frame, (320, 240))

        # Interpolasi sederhana
        if prev_frame is not None:

            smooth_frame = interpolate_frames(
                prev_frame,
                frame,
                0.5
            )

        else:
            smooth_frame = frame

        prev_frame = frame

        # Ubah jadi ASCII
        ascii_frame = frame_to_ascii(
            smooth_frame,
            width=ascii_width
        )

        # Bersihkan terminal
        os.system("cls" if os.name == "nt" else "clear")

        # Tampilkan
        print(ascii_frame)

        # Delay sesuai FPS
        time.sleep(delay)

    cap.release()

    print("\n[✓] Video selesai")


# =========================
# MAIN PROGRAM
# =========================
if __name__ == "__main__":

    # Ganti dengan nama video kamu
    video_path = "video.mp4"

    play_video(
        video_path=video_path,
        max_duration=20,
        ascii_width=100
    )
