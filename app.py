import streamlit as st
import time
from snake_game import SnakeGame

# Page configuration
st.set_page_config(
    page_title="Snake Game",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E8B57;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .game-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    .score-display {
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        color: #FF6B6B;
        margin: 1rem 0;
    }
    .controls {
        text-align: center;
        margin: 1rem 0;
    }
    .game-board {
        font-family: monospace;
        font-size: 1.2rem;
        line-height: 1.2;
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 10px;
        border: 3px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

def display_game_board(board):
    """Display the game board with proper formatting"""
    board_html = "<div class='game-board'>"
    for row in board:
        board_html += "<div style='display: flex; justify-content: center;'>"
        for cell in row:
            if cell == "🐍":  # Snake head
                board_html += f"<span style='margin: 1px; font-size: 1.5rem;'>{cell}</span>"
            elif cell == "🟢":  # Snake body
                board_html += f"<span style='margin: 1px; font-size: 1.5rem;'>{cell}</span>"
            elif cell == "🍎":  # Food
                board_html += f"<span style='margin: 1px; font-size: 1.5rem;'>{cell}</span>"
            else:  # Empty space
                board_html += "<span style='margin: 1px; font-size: 1.5rem;'>⬜</span>"
        board_html += "</div>"
    board_html += "</div>"
    return board_html

def main():
    # Initialize session state
    if 'game' not in st.session_state:
        st.session_state.game = SnakeGame()
    if 'last_auto_move' not in st.session_state:
        st.session_state.last_auto_move = time.time()
    
    # Header
    st.markdown('<h1 class="main-header">🐍 Snake Game 🐍</h1>', unsafe_allow_html=True)
    
    # Sidebar for controls
    with st.sidebar:
        st.header("Game Controls")
        
        # Game speed control
        st.subheader("Game Speed")
        speed = st.slider("Speed (seconds per move)", 0.1, 1.0, 0.3, 0.1)
        st.session_state.game.set_speed(speed)
        
        # Game size control
        st.subheader("Game Size")
        size = st.selectbox("Board Size", [15, 20, 25, 30], index=1)
        
        # Control buttons
        st.subheader("Actions")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 New Game"):
                st.session_state.game = SnakeGame(size, size)
                st.session_state.last_auto_move = time.time()
                st.rerun()
        
        with col2:
            if st.button("⏸️ Pause/Resume"):
                st.session_state.game.toggle_pause()
                st.rerun()
        
        # Instructions
        st.subheader("How to Play")
        st.markdown("""
        - Use arrow buttons to control the snake
        - Eat the 🍎 to grow and score points
        - Avoid hitting walls or yourself
        - Try to get the highest score!
        """)
        
        # High score (simple implementation)
        if 'high_score' not in st.session_state:
            st.session_state.high_score = 0
        
        if st.session_state.game.score > st.session_state.high_score:
            st.session_state.high_score = st.session_state.game.score
        
        st.subheader("High Score")
        st.metric("Best Score", st.session_state.high_score)
    
    # Main game area
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Score display
        st.markdown(f'<div class="score-display">{st.session_state.game.get_status()}</div>', 
                   unsafe_allow_html=True)
        
        # Game board
        board = st.session_state.game.get_board_state()
        st.markdown(display_game_board(board), unsafe_allow_html=True)
        
        # Control buttons
        st.markdown('<div class="controls">', unsafe_allow_html=True)
        
        # Direction controls
        col_up, col_down = st.columns(2)
        
        with col_up:
            if st.button("⬆️ Up", use_container_width=True):
                st.session_state.game.move_snake("UP")
                st.rerun()
        
        with col_down:
            if st.button("⬇️ Down", use_container_width=True):
                st.session_state.game.move_snake("DOWN")
                st.rerun()
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            if st.button("⬅️ Left", use_container_width=True):
                st.session_state.game.move_snake("LEFT")
                st.rerun()
        
        with col_right:
            if st.button("➡️ Right", use_container_width=True):
                st.session_state.game.move_snake("RIGHT")
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Auto-move logic with proper timing
    current_time = time.time()
    if (current_time - st.session_state.last_auto_move >= speed and 
        not st.session_state.game.game_over and not st.session_state.game.paused):
        st.session_state.game.auto_move()
        st.session_state.last_auto_move = current_time
        st.rerun()
    
    # Game over handling
    if st.session_state.game.game_over:
        st.error("Game Over! Click 'New Game' to play again.")
        
        # Show final stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Final Score", st.session_state.game.score)
        with col2:
            st.metric("Snake Length", len(st.session_state.game.snake))
        with col3:
            st.metric("High Score", st.session_state.high_score)

if __name__ == "__main__":
    main() 