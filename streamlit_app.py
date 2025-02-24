import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Monte Carlo simulation for player prop bets
def simulate_player_prop(season_avg, recent_avg, opp_defense, line, simulations=10000):
    projected_points = (season_avg * 0.4) + (recent_avg * 0.3) + (opp_defense * 0.3)
    outcomes = np.random.normal(loc=projected_points, scale=5, size=simulations)
    over_hits = np.sum(outcomes > line) / simulations * 100
    under_hits = 100 - over_hits

    plt.figure(figsize=(10, 6))
    plt.hist(outcomes, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
    plt.axvline(line, color='red', linestyle='--', label=f'Betting Line: {line}')
    plt.xlabel('Projected Points')
    plt.ylabel('Frequency')
    plt.title(f'Simulation Results for Player Prop (Line: {line})')
    plt.legend()
    st.pyplot(plt)

    st.write(f"### Projected Points: {projected_points:.2f}")
    st.write(f"**Probability of OVER {line}: {over_hits:.2f}%**")
    st.write(f"**Probability of UNDER {line}: {under_hits:.2f}%**")

st.title("Player Prop Bet Simulator")

season_avg = st.slider("Season Average", 1, 70, 25)
recent_avg = st.slider("Recent Average", 1, 70, 25)
opp_def = st.slider("Opponent Defense", 1, 70, 25)
line = st.slider("Betting Line", 1, 60, 25)

if st.button("Run Simulation"):
    simulate_player_prop(season_avg, recent_avg, opp_def, line)
    