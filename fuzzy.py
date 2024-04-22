import numpy as np
import matplotlib.pyplot as plt

class FuzzyController:
    def __init__(self):
        self.temperature = np.arange(0, 101, 1)
        self.cold = self.trimf(self.temperature, [0, 0, 50])
        self.hot = self.trimf(self.temperature, [50, 100, 100])

    def trimf(self, x, params):
        a, b, c = params
        return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

    def infer(self, temp):
        cold_degree = self.trimf(temp, [0, 0, 50])
        hot_degree = self.trimf(temp, [50, 100, 100])
        return cold_degree, hot_degree

    def defuzzify(self, cold_degree, hot_degree):
        cold_area = np.sum(np.minimum(self.cold, cold_degree))
        hot_area = np.sum(np.minimum(self.hot, hot_degree))
        total_area = cold_area + hot_area
        if total_area == 0:
            return 0
        return (50 * cold_area + 100 * hot_area) / total_area

    def plot_membership(self):
        plt.plot(self.temperature, self.cold, label='Cold')
        plt.plot(self.temperature, self.hot, label='Hot')
        plt.xlabel('Temperature')
        plt.ylabel('Membership Degree')
        plt.title('Temperature Membership Functions')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    controller = FuzzyController()
    controller.plot_membership()

    temp = float(input("Enter the current temperature (0-100): "))
    cold_degree, hot_degree = controller.infer(temp)
    print("Cold degree:", cold_degree)
    print("Hot degree:", hot_degree)
    
    result = controller.defuzzify(cold_degree, hot_degree)
    print("Defuzzified result:", result)

if __name__ == "__main__":
    main()

