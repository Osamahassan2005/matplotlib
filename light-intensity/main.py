import matplotlib.pyplot as plt
# import numpy as np

# distances = np.array([1, 2, 3, 4, 5])
# candle = np.array([10, 2.5, 1.1, 0.6, 0.4])
# led = np.array([280, 70, 30, 17, 11])
# tecno_flash = np.array([30, 7.5, 3.3, 1.9, 1.2])
# theory_led = 280 / distances**2  # Inverse-square prediction

# plt.figure(figsize=(10, 6))
# plt.scatter(distances, led, color='blue', s=100, label="LED Bulb (Measured)")
# plt.plot(distances, theory_led, 'b--', label="LED (Theoretical: $I ∝ 1/d²$)")
# plt.scatter(distances, tecno_flash, color='green', s=100, label="TECNO Camon 20 Flashlight")
# plt.scatter(distances, candle, color='red', s=100, label="Candle")
# plt.xlabel("Distance (m)", fontsize=12)
# plt.ylabel("Light Intensity (lux)", fontsize=12)
# plt.title("Light Intensity vs. Distance from Source", fontsize=14)
# plt.legend(fontsize=10)
# plt.grid(True, linestyle='--', alpha=0.6)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Data
distances = np.array([1, 2, 3, 4, 5])
candle = np.array([10, 2.5, 1.1, 0.6, 0.4])
led = np.array([280, 70, 30, 17, 11])
tecno_flash = np.array([30, 7.5, 3.3, 1.9, 1.2])

# Theoretical LED data based on inverse square law
theory_led = 280 / distances**2

# Plot setup
plt.figure(figsize=(10, 6))

# Measured points
plt.scatter(distances, led, color='blue', s=100, label="LED Bulb (Measured)")
plt.plot(distances, theory_led, 'b--', label="LED (Theoretical: $I ∝ 1/d²$)")
plt.scatter(distances, tecno_flash, color='green', s=100, label="TECNO Camon 20 Flashlight")
plt.scatter(distances, candle, color='red', s=100, label="Candle")

# Labels and Title
plt.xlabel("Distance (m)", fontsize=12)
plt.ylabel("Light Intensity (lux)", fontsize=12)
plt.title("Light Intensity vs. Distance from Source", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

#save graph
plt.savefig('intensity-vs-distance.png',dpi=300)

# Display the graph
plt.show()





