"""Reels videosuna _muzik/ klasöründeki parçalardan birini gömer.
Kullanım: python3 _muzik/muzik_ekle.py <reel.mp4> <çıktı.mp4> [parça_no]
parça_no verilmezse video adına göre sırayla dağıtılır. Ses -16 LUFS'a eşitlenir, sonda 2,5 sn kısılır.
Parçalar Pixabay Music lisansıyla kullanılıyor (ücretsiz, atıf gerekmez).
"""
import sys, os, glob, subprocess, zlib

HERE = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1], sys.argv[2]
tracks = sorted(glob.glob(os.path.join(HERE, "[0-9]-*.mp3")))
if len(sys.argv) > 3:
    tr = tracks[int(sys.argv[3]) - 1]
else:
    tr = tracks[zlib.crc32(os.path.abspath(src).encode()) % len(tracks)]
dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "csv=p=0", src]).decode().strip())
fo = max(0.0, dur - 2.5)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-i", tr,
                "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                "-af", f"loudnorm=I=-16:TP=-1.5:LRA=11,afade=t=in:d=0.4,afade=t=out:st={fo:.2f}:d=2.5",
                "-t", f"{dur:.2f}", "-movflags", "+faststart", out], check=True)
print("ok", out, "←", os.path.basename(tr))
