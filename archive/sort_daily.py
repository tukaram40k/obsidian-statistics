import shutil as sh
import os
import re

SRC = "C:/Users/Ivan/Documents/Obsidian/Vault1/Daily/2025"
TRG = "C:/Users/Ivan/Documents/Obsidian/Vault1/Daily/2025/march"
PATTERN = '\d+\-03-\d+'

for filename in os.listdir(SRC):
    if re.match(PATTERN, filename):
        sh.move(os.path.join(SRC, filename), TRG)