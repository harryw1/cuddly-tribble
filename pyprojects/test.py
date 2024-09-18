def check_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} is installed and working correctly.")
    except ImportError:
        print(f"{package_name} is not installed or not working correctly.")

def main():
    print("Testing environment for required packages:")

    # Check pandas
    check_package("pandas")

    # Check numpy
    check_package("numpy")

    # Check matplotlib
    check_package("matplotlib")

    # Simple demonstration of numpy and matplotlib (if available)
    try:
        import numpy as np
        import matplotlib.pyplot as plt

        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("Test Plot")
        print("Successfully created a test plot (not displayed in this environment).")
    except Exception as e:
        print(f"Error demonstrating numpy/matplotlib: {e}")

if __name__ == "__main__":
    main()
