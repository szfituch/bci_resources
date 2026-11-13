import time
import math
import random
from pylsl import StreamInfo, StreamOutlet

info = StreamInfo('BrainWare', 'Control', 3, 10, 'float32', 'mock_id_123')
outlet = StreamOutlet(info)

print("LSL var preview:")
print("-" * 60)

heal = 0.0

while True:
    wave = math.sin(time.time() * 0.2)

    focus = max(0.0, wave)
    rage = max(0.0, -wave)

    heal += random.uniform(-0.02, 0.02)
    heal = max(0.0, min(1.0, heal))

    sample = [focus, rage, heal]
    outlet.push_sample(sample)

    focus_text = f"FOCUS: {focus:.2f}"
    rage_text = f"RAGE: {rage:.2f}"
    heal_text = f"HEAL: {heal:.2f}"

    print(f"\r{focus_text}  |  {rage_text}  |  {heal_text}", end="", flush=True)

    time.sleep(0.1)