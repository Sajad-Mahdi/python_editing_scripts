import subprocess
import json
from pathlib import Path

def probe_video(file_path):
    result = subprocess.run(
        [
            'ffprobe', '-v',
            'error', '-show_entries',
            'format=duration',
            '-of', 'json',
            str(file_path)
        ],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    return json.loads(result.stdout)