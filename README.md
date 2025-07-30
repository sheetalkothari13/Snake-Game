# 🐍 Snake Game with Streamlit

A classic Snake game built with Python and Streamlit, featuring a beautiful web interface with modern controls and **fixed single-step movement**.

## 🎮 Features

- **Classic Snake Gameplay**: Control a snake to eat food and grow longer
- **Single-Step Movement**: **Fixed** - Snake now moves exactly one step at a time
- **Beautiful UI**: Modern Streamlit interface with emojis and styling
- **Customizable Settings**: Adjustable game speed and board size
- **Score Tracking**: Real-time score display and high score tracking
- **Pause/Resume**: Pause the game at any time
- **Responsive Controls**: Button controls for precise movement
- **Game Over Handling**: Clear game over screen with final statistics

## 🚀 Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the game**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser**
   - The game will automatically open in your default browser
   - Usually at `http://localhost:8501`

## 🎯 How to Play

### Controls
- **Arrow Buttons**: Use the on-screen arrow buttons to control the snake
- **Game Speed**: Adjust the speed slider in the sidebar (0.1 to 1.0 seconds per move)
- **Board Size**: Choose from 15x15, 20x20, 25x25, or 30x30 grid sizes
- **New Game**: Click "🔄 New Game" to start a fresh game
- **Pause/Resume**: Click "⏸️ Pause/Resume" to pause or resume the game

### Game Rules
1. **Objective**: Eat the 🍎 (food) to grow your snake and score points
2. **Movement**: The snake moves continuously in the current direction
3. **Scoring**: Each food eaten gives you 10 points
4. **Game Over**: The game ends if you:
   - Hit the wall (boundaries)
   - Hit your own body
5. **Growth**: The snake grows longer each time it eats food

### Game Elements
- 🐍 **Snake Head**: The front of your snake
- 🟢 **Snake Body**: The rest of your snake
- 🍎 **Food**: Eat this to grow and score points
- ⬜ **Empty Space**: Safe areas to move through

## 🔧 Technical Details

### Movement Fix
The game now includes a **movement cooldown system** to prevent the snake from taking 2 steps at a time:

- **Movement Cooldown**: Minimum time between moves (0.1 to 1.0 seconds)
- **Timing Control**: Proper time tracking to ensure single-step movement
- **Auto-Move Logic**: Separate auto-move function with proper timing
- **Speed Control**: Real-time speed adjustment without movement issues

### Key Improvements
1. **Single-Step Movement**: Snake moves exactly one cell at a time
2. **Proper Timing**: Movement cooldown prevents rapid-fire button presses
3. **Speed Control**: Adjustable speed that works correctly
4. **Smooth Gameplay**: No more double-stepping or erratic movement

## 🎨 Customization

### Changing Game Speed
- Use the speed slider in the sidebar
- Lower values = faster gameplay
- Higher values = slower, more controlled gameplay
- **Note**: Speed changes are applied immediately without movement issues

### Changing Board Size
- Select different board sizes from the sidebar
- Larger boards = more space but longer games
- Smaller boards = faster, more intense gameplay

## 🐛 Troubleshooting

### Common Issues

1. **Streamlit not found**
   ```bash
   pip install streamlit
   ```

2. **Port already in use**
   ```bash
   streamlit run app.py --server.port 8502
   ```

3. **Game not responding**
   - Refresh the browser page
   - Check if the game is paused
   - Try starting a new game

4. **Movement issues**
   - The double-step issue has been fixed
   - If you experience any movement problems, try refreshing the page

## 📁 Project Structure

```
snake-game/
├── app.py              # Main Streamlit application
├── snake_game.py       # Game logic and SnakeGame class
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new features
- Improving the UI/UX
- Fixing bugs
- Adding sound effects
- Implementing multiplayer functionality

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Enjoy Playing!

The Snake game now features smooth, single-step movement that makes gameplay much more enjoyable and predictable. Try to beat your high score and challenge your friends!

---

**Happy Gaming! 🐍🍎** 