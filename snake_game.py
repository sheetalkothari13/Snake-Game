import random
import time
from typing import List, Tuple, Optional
import streamlit as st

class SnakeGame:
    def __init__(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height
        self.reset_game()
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Initialize snake at center
        center_x, center_y = self.width // 2, self.height // 2
        self.snake = [(center_x, center_y), (center_x-1, center_y), (center_x-2, center_y)]
        self.direction = "RIGHT"
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
        self.paused = False
        self.last_move_time = time.time()
        self.movement_cooldown = 0.3  # Minimum time between moves
    
    def generate_food(self) -> Tuple[int, int]:
        """Generate food at random position where both x and y are multiples of 2"""
        while True:
            # Generate x and y coordinates that are multiples of 2
            food_x = random.randint(0, (self.width - 1) // 2) * 2
            food_y = random.randint(0, (self.height - 1) // 2) * 2
            if (food_x, food_y) not in self.snake:
                return (food_x, food_y)
    
    def move_snake(self, direction: Optional[str] = None):
        """Move the snake in the given direction"""
        if self.game_over or self.paused:
            return
        
        # Check if enough time has passed since last move
        current_time = time.time()
        if current_time - self.last_move_time < self.movement_cooldown:
            return
        
        if direction:
            # Prevent reverse movement
            if (direction == "LEFT" and self.direction == "RIGHT") or \
               (direction == "RIGHT" and self.direction == "LEFT") or \
               (direction == "UP" and self.direction == "DOWN") or \
               (direction == "DOWN" and self.direction == "UP"):
                return
            self.direction = direction
        
        # Get head position
        head_x, head_y = self.snake[0]
        
        # Calculate new head position
        if self.direction == "UP":
            new_head = (head_x, head_y - 1)
        elif self.direction == "DOWN":
            new_head = (head_x, head_y + 1)
        elif self.direction == "LEFT":
            new_head = (head_x - 1, head_y)
        elif self.direction == "RIGHT":
            new_head = (head_x + 1, head_y)
        
        # Check for wall collision
        if (new_head[0] < 0 or new_head[0] >= self.width or 
            new_head[1] < 0 or new_head[1] >= self.height):
            self.game_over = True
            return
        
        # Check for self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Add new head
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.score += 10
            self.food = self.generate_food()
        else:
            # Remove tail if no food eaten
            self.snake.pop()
        
        # Update last move time
        self.last_move_time = current_time
    
    def auto_move(self):
        """Auto move the snake in current direction"""
        current_time = time.time()
        if (current_time - self.last_move_time >= self.movement_cooldown and 
            not self.game_over and not self.paused):
            self.move_snake()
    
    def get_board_state(self) -> List[List[str]]:
        """Get current board state as 2D array"""
        board = [[" " for _ in range(self.width)] for _ in range(self.height)]
        
        # Place snake
        for i, (x, y) in enumerate(self.snake):
            if i == 0:  # Head
                board[y][x] = "🐍"
            else:  # Body
                board[y][x] = "🟢"
        
        # Place food
        food_x, food_y = self.food
        board[food_y][food_x] = "🍎"
        
        return board
    
    def toggle_pause(self):
        """Toggle pause state"""
        self.paused = not self.paused
    
    def set_speed(self, speed: float):
        """Set movement speed (lower = faster)"""
        self.movement_cooldown = max(0.1, min(1.0, speed))
    
    def get_status(self) -> str:
        """Get current game status"""
        if self.game_over:
            return "Game Over! Final Score: " + str(self.score)
        elif self.paused:
            return "Paused - Score: " + str(self.score)
        else:
            return "Playing - Score: " + str(self.score) 