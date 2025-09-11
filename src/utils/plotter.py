#######################################################################################
# Import required libraries/modules
# =====================================================================================
import numpy as np
import matplotlib.pyplot as plt
import re
from utils.config import Config
from PIL import Image
import os

config = Config()

class Plotter:  # Class name should follow PascalCase
    def __init__(self, design_number):
        self.design_number = design_number

    def plot_residuals(self, filename, output_file):
        data = np.loadtxt(filename, skiprows=3)  # Skip header lines
        time = data[:, 0]
        Ux, Uy, Uz, p, k, omega = data[:, 1], data[:, 2], data[:, 3], data[:, 4], data[:, 5], data[:, 6]
        
        plt.figure(figsize=(10, 6))
        plt.plot(time, Ux, label='Ux')
        plt.plot(time, Uy, label='Uy')
        plt.plot(time, Uz, label='Uz')
        plt.plot(time, p, label='p')
        plt.plot(time, k, label='k')
        plt.plot(time, omega, label='omega')
        
        plt.xlabel('Iterations')
        plt.ylabel('Residuals')
        plt.title('Residuals vs Time')
        plt.legend()
        plt.yscale('log')
        plt.grid(True, linestyle="--", linewidth=0.5)
        plt.savefig(output_file)
        plt.close()

    def plot_probe_pressure(self, filename, output_file):
        data = np.loadtxt(filename, skiprows=2)  # Skip header lines
        time = data[:, 0]
        press1 = data[:, 1]
        press2 = data[:, 2]
        press3 = data[:, 3]

        plt.figure(figsize=(10, 6))
        plt.plot(time, press1, label='Probe-1')
        plt.plot(time, press2, label='Probe-2')
        plt.plot(time, press3, label='Probe-3')
        plt.xlabel('Iterations')
        plt.ylabel('Pressure')
        plt.title('Pressure vs Time (Probe)')
        plt.ylim(-3000, 500)     # Set y-axis limits here
        plt.grid(True)
        plt.savefig(output_file)
        plt.close()

    def plot_probe_U(self, filename, output_file):

        with open(filename, 'r') as f:
            lines = f.readlines()

        time = []
        probe_data = []  # will hold 3 probes × 3 components each

        # regex to extract (number number number)
        pattern = re.compile(r'\((-?\d*\.?\d*(?:e[-+]?\d+)?)[ ]+(-?\d*\.?\d*(?:e[-+]?\d+)?)[ ]+(-?\d*\.?\d*(?:e[-+]?\d+)?)\)')

        for line in lines[4:]:  # skip first two header lines
            parts = line.strip().split()
            t = float(parts[0])
            time.append(t)

            vectors = pattern.findall(line)
            # vectors = list of tuples of 3 strings (Ux, Uy, Uz) for each probe
            # Convert each to float and flatten all probes into one list for plotting
            flattened = []
            for v in vectors:
                flattened.extend([float(c) for c in v])
            probe_data.append(flattened)

        time = np.array(time)
        probe_data = np.array(probe_data)  # shape (time_steps, 9)

        labels = [
            'Probe1 Ux', 'Probe1 Uy', 'Probe1 Uz',
            'Probe2 Ux', 'Probe2 Uy', 'Probe2 Uz',
            'Probe3 Ux', 'Probe3 Uy', 'Probe3 Uz'
        ]

        plt.figure(figsize=(12, 7))
        for i in range(probe_data.shape[1]):
            plt.plot(time, probe_data[:, i], label=labels[i])

        plt.xlabel('Iterations')
        plt.ylabel('U [m/s]')
        plt.title('Probe Velocity Components over Time')
        plt.legend()
        plt.grid(True)
        # Save or show the plot as needed
        plt.savefig(output_file)
        plt.close()

    
    def generate_plots(self):
        # File paths
        residuals_file = rf"{config.foam_case}\postProcessing\residuals\0\residuals.dat"
        pressure_probe_file = rf"{config.foam_case}\postProcessing\probes\0\p"
        U_probe_file = rf"{config.foam_case}\postProcessing\probes\0\U"

        # Output file paths
        residuals_output = rf"{config.residual_probes}\residuals_design-"+str(self.design_number)+".png"
        pressure_output = rf"{config.residual_probes}\probe_press_design-"+str(self.design_number)+".png"
        U_output = rf"{config.residual_probes}\probe_U_design-"+str(self.design_number)+".png"

        # Generate plots
        self.plot_residuals(residuals_file, residuals_output)
        self.plot_probe_pressure(pressure_probe_file, pressure_output)
        self.plot_probe_U(U_probe_file, U_output)

    def create_collage(self, image_paths, output_pdf_path):
        cols=3
        spacing=10
        bg_color=(255, 255, 255)
        images = [Image.open(img).convert("RGB") for img in image_paths]
        if not images:
            print("No images to process.")
            return

        # Get max width and height for consistent image size (optional: resize to same size if needed)
        widths, heights = zip(*(img.size for img in images))
        max_width = max(widths)
        max_height = max(heights)

        rows = (len(images) + cols - 1) // cols
        collage_width = cols * max_width + (cols - 1) * spacing
        collage_height = rows * max_height + (rows - 1) * spacing

        # Create blank background image
        collage = Image.new("RGB", (collage_width, collage_height), bg_color)

        for index, img in enumerate(images):
            row, col = divmod(index, cols)
            x = col * (max_width + spacing)
            y = row * (max_height + spacing)
            collage.paste(img, (x, y))

        # Save as PDF
        pdf_path = output_pdf_path + ".pdf"
        collage.save(pdf_path, "PDF", resolution=100.0)
        print(f"PDF saved to: {pdf_path}")

if __name__ == "__main__":
        # Generate and save plots using the PlotResiduals class
        plotter = PlotResiduals(5)
        plotter.generate_plots()