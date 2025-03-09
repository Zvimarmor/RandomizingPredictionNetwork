import sys
import datetime
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFrame, QGridLayout
from PyQt6.QtCore import QTimer
import matplotlib.pyplot as plt
import random
import time

class coloringGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)
        self.current_colors = [0, 1]
        self.current_color = 0
        
    def color_cell(self, row, col):
        color = np.random.choice(self.current_colors)
        self.grid[row, col] = color
        
    def color_grid(self):
        self.grid = np.zeros((self.rows, self.cols), dtype=int)
        for row in range(self.rows):
            for col in range(self.cols):
                self.color_cell(row, col)
                
    def get_grid(self):
        return self.grid
    
    def print_grid(self):
        plt.imshow(self.grid, cmap='gray')
        plt.show()

if __name__ == '__main__':
    mygrid = coloringGrid(30,30)
    mygrid.color_grid()
    mygrid.print_grid()
            
            
        
        