import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QVBoxLayout, QWidget, QLabel
import matplotlib.pyplot as plt

#oop way
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("plot test")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Plot 1", "Plot 2", "Plot 3"])
        self.list_widget.currentItemChanged.connect(self.update_plot)
        self.layout.addWidget(self.list_widget)
        self.plot_label = QLabel("Select a plot from the list")
        self.layout.addWidget(self.plot_label)

    def update_plot(self, current, previous):
        if current is not None:
            plot_name = current.text()
            self.plot_label.setText(f"showing {plot_name}")
            self.show_plot(plot_name)

    def show_plot(self, plot_name):
        plt.clf()
        if plot_name == "Plot 1":
            plt.plot([1, 2, 3], [1, 4, 9], label="Plot 1 Data")
        elif plot_name == "Plot 2":
            plt.plot([1, 2, 3], [9, 4, 1], label="Plot 2 Data")
        elif plot_name == "Plot 3":
            plt.plot([1, 2, 3], [1, 2, 3], label="Plot 3 Data")
        plt.legend()
        plt.title(plot_name)
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
