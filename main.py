"""
main.py

Purpose: Generate train images

1. read pulse data from .csv
2. find peaks
3. split graph (height 1100 to 1600 && distance 200)
4. save graph by 200x200 size (save at "./train_data/")
"""
try: # if user don't install libraries, send error message
    import matplotlib.pyplot as plt
    from scipy.signal import find_peaks
    import numpy as np
    import platform
    import csv
    import os
except:
    print("Error: You need to install libraries")


class ExtractPulseFigure:
    def __init__(self, csv_file_name):
        self.csv_file_name: str = csv_file_name
        self.y: list = []
        self.peaks:list = []
    """
    Read pulse data || from .csv
    """
    def read_pulse_data(self):
        f = open(f"{os.getcwd()}\\data\\106_MLII.csv", "r")
        data = csv.reader(f)
        next(data) # Skip header || because of unuseful data
        
        """Convert type to list to numpy array"""
        [self.y.append(int(row[0])) for row in data]
        # close .csv file
        f.close()

        # change type to numpy array
        self.y = np.array(self.y)
    """
    Find peaks from graph
    """
    def find_peaks(self):
        # standard height [1100, 1600] ; distance 200
        self.peaks, _ = find_peaks(self.y, height=(1100, 1600), distance=200)
        # print peaks' arr length on terminal
        print(len(self.peaks))
    """
    Save figure from "./train_data/"
    """
    def save_figure(self):
        for pulse_N in range(1, len(self.peaks)-1):
            fig = plt.figure(frameon=False)
            fig.set_size_inches(2, 2)
            ax = fig.add_axes([0, 0, 1, 1])
            ax.axis("off")
            ax.plot(self.y[self.peaks[pulse_N]: self.peaks[pulse_N+1]])
            try:
                fig.savefig(f"{os.getcwd()}\\train_data\\{pulse_N}.png", format="png")
            except:
                os.makedirs("train_data")
                fig.savefig(f"{os.getcwd()}\\train_data\\{pulse_N}.png", format="png")
            plt.close()


def main():
    epf = ExtractPulseFigure("106_MLII.csv")
    epf.read_pulse_data()
    epf.find_peaks()
    epf.save_figure()

if __name__=="__main__":
    main()