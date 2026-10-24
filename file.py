import streamlit as st
import pandas as pd
import plotly.express as px
import math
import time

# --- 1. CONFIG ---
st.set_page_config(page_title="Humanitarian Intelligence System", layout="wide")

# --- 2. WEAPON DATABASE (The "Type of Weapons" Section) ---
weapon_data = {
    "Conventional": ["MK-82 Bomb", "Tomahawk Missile", "MOAB"],
    "Tactical": ["B61-12 Warhead", "Iskander-M"],
    "Strategic": ["Minuteman III", "RS-28 Sarmat"]
}

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("🎮 Mission Control")
    
    # Weapon Category Selection
    w_cat = st.selectbox("Select Weapon Category", list(weapon_data.keys()))
    w_type = st.selectbox("Specific Model", weapon_data[w_cat])
    
    # Hit Count (How many times it hit)
    hit_count = st.number_input("Number of Strikes", min_value=1, max_value=20, value=1)
    
    # Place Name
    target_place = st.text_input("Place(s) Impacted", "Sector Alpha, District B")
    
    # Physics Settings
    if w_cat == "Conventional":
        yield_kt = st.slider("Yield per Strike (kT)", 0.001, 0.5, 0.1, format="%.3f")
    else:
        yield_kt = st.slider("Yield per Strike (kT)", 1.0, 100.0, 10.0)

    pop_density = st.number_input("Avg Population Density (p/km²)", value=8000)

# --- 4. CALCULATIONS (Multi-Hit Logic) ---
# Radius per single hit
r_lethal = 0.45 * (yield_kt**(1/3))
r_injury = 0.75 * (yield_kt**(1/3))

# Total Impact considering multiple strikes
total_area_lethal = math.pi * (r_lethal**2) * hit_count
total_area_injury = ((math.pi * (r_injury**2)) - (math.pi * (r_lethal**2))) * hit_count

total_deaths = int(total_area_lethal * pop_density * 0.95)
total_injuries = int(total_area_injury * pop_density * 0.60)
total_affected = total_deaths + total_injuries

# --- 5. MAIN DASHBOARD ---
st.title("🛡️ Humanitarian Intelligence & War Impact System")
st.markdown(f"**Weapon Deployed:** {w_type} ({w_cat}) | **Total Strikes:** {hit_count} | **Targets:** {target_place}")

# Summary Metrics
m1, m2, m3, m4 = st.columns(4)
m1.metric("Single Blast Radius", f"{round(r_lethal, 2)} km")
m2.metric("Total Fatalities", f"{total_deaths:,}")
m3.metric("Total Injuries", f"{total_injuries:,}")
m4.metric("Aid Target", f"{total_affected:,}")

st.divider()

# --- 6. ANALYSIS TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Impact Visualization", "📦 Logistical Support", "📚 Arsenal Specs"])

with tab1:
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.subheader("Blast Propagation Scaling")
        # Visualizing the difference between 1 strike and total strikes
        strike_df = pd.DataFrame({
            "Metric": ["Lethal Area (1 Strike)", "Total Lethal Area (All Strikes)"],
            "Area (km²)": [math.pi * (r_lethal**2), total_area_lethal]
        })
        fig = px.bar(strike_df, x="Metric", y="Area (km²)", color="Metric", 
                     color_discrete_sequence=["#1E88E5", "#D32F2F"], text_auto=True)
        st.plotly_chart(fig, use_container_width=True)
    with col_b:
        st.info(f"**Strike History:** {hit_count} detonations recorded in {target_place}.")
        st.warning(f"Total impacted footprint: {round(total_area_lethal + total_area_injury, 2)} km².")

with tab2:
    st.subheader("🚚 Supply Chain Requirements")
    # Table for logistics
    aid_data = {
        "Requirement": ["Drinking Water", "Food Rations", "Medical Packs", "Transport Trucks"],
        "Total Amount": [
            f"{total_affected * 15 * 30:,} Liters",
            f"{(total_affected * 0.5 * 30) / 1000:,.1f} Metric Tons",
            f"{int(total_affected / 50):,} Units",
            f"{math.ceil((total_affected * 0.5 * 30) / 5000)} Heavy Trucks"
        ]
    }
    st.table(pd.DataFrame(aid_data))

with tab3:
    st.subheader("🔬 Technical Specifications: " + w_type)
    specs = {
        "Weapon Class": [w_cat],
        "Standard Yield": [f"{yield_kt} kT"],
        "Mechanism": ["High-Pressure Shockwave"],
        "Deployment Mode": ["Airburst" if w_cat != "Conventional" else "Surface Impact"]
    }
    st.table(pd.DataFrame(specs))

st.caption("Humanitarian DSS Prototype | Calculations based on UN standard rations and Blast Scaling Laws.")how to run this code in vs code0