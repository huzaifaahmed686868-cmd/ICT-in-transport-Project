import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="ICT in Transport & Energy Consumption",
    page_icon="⚡",
    layout="wide"
)

# App Title & Overview
st.title("⚡ Information & Communication Technology (ICT) in Transport")
st.markdown("""
This interactive application explores how **ICT** transforms modern transportation systems and analyzes its dual impact on **energy consumption**. 
Discover applications, analyze the net energy balance, and simulate energy efficiency scenarios.
""")

# --- GROUP MEMBERS / PROJECT CONTRIBUTORS SECTION ---
st.markdown("---")
st.subheader("👥 Project Group Members")

# Displaying group members in a clean grid format using native Streamlit columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    * **Huzaifa Ahmed** 🔢 Roll No: `25-ME-168`
    * **Farhan Ali Shahid** 🔢 Roll No: `25-ME-204`
    """)

with col2:
    st.markdown("""
    * **Syed Muhammad Aunn** 🔢 Roll No: `25-ME-224`
    * **Shah Muhammad** 🔢 Roll No: `25-ME-140`
    """)

with col3:
    st.markdown("""
    * **Mian Muhammad Mussab** 🔢 Roll No: `25-ME-60`
    """)
st.markdown("---")

# Navigation Sidebar using pure Streamlit radio buttons
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to:", ["Overview & Applications", "Energy Impact Analysis", "Interactive Savings Calculator"])

# PAGE 1: Overview & Applications
if page == "Overview & Applications":
    st.header("🌐 Core Applications of ICT in Transport")
    st.write("ICT integrates communication and information systems into transport infrastructure to improve efficiency, safety, and sustainability.")
    
    p_col1, p_col2, p_col3 = st.columns(3)
    
    with p_col1:
        st.subheader("🤖 Intelligent Transport Systems (ITS)")
        st.markdown("""
        * **Smart Traffic Lights:** Adaptive signaling based on real-time traffic flow to reduce idling.
        * **Dynamic Routing:** GPS and AI-driven navigation redirecting vehicles away from congestion.
        """)
        
    with p_col2:
        st.subheader("📈 Logistics & Fleet Management")
        st.markdown("""
        * **Telematics:** Monitoring driver behavior, speed, and fuel idling.
        * **Load Optimization:** Ensuring freight trucks travel fully loaded, reducing total trips.
        """)
        
    with p_col3:
        st.subheader("🚗 Smart Mobility & EV Integration")
        st.markdown("""
        * **MaaS (Mobility as a Service):** Apps integrating public transit, ride-sharing, and bikes.
        * **Grid-to-Vehicle (V2G):** Smart charging systems managing power grids for electric vehicles.
        """)

    st.markdown("---")
    st.subheader("📊 Primary Domains of Impact")
    
    # Pure Python data representation using a dictionary (No Pandas)
    app_data = {
        "Traffic Flow Optimization": 15,
        "Public Transit Scheduling": 20,
        "Freight Logistics": 25,
        "Eco-Driving Feedback": 10,
        "Autonomous Driving": 12
    }
    
    # Using Streamlit's native chart to display data purely from a Python dict
    st.write("Expected Efficiency Gain (%) by Domain:")
    st.bar_chart(app_data)

# PAGE 2: Energy Impact Analysis (Increase vs. Decrease)
elif page == "Energy Impact Analysis":
    st.header("📉 The Dual Role of ICT: Energy Consumption vs. Savings")
    st.markdown("""
    Does ICT increase or decrease energy use? The answer is a **net balance**. 
    While ICT infrastructure consumes electrical energy, the operational optimization it provides drastically reduces overall fuel and energy usage.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("🔺 Factors INCREASING Energy Usage (Direct Footprint)")
        st.markdown("""
        * **Data Centers & Servers:** Cloud computations, real-time tracking, and AI route modeling require massive server power.
        * **On-Board Hardware:** Embedded sensors, GPS modules, radar, and cameras draw continuous power from the vehicle.
        * **Infrastructure:** 5G networks and roadside IoT communication units require constant electrical upkeep.
        """)
        
    with col2:
        st.success("🔻 Factors DECREASING Energy Usage (Indirect Optimization)")
        st.markdown("""
        * **Reduced Idling:** Smart intersections cut down on stop-and-go energy waste.
        * **Eco-Routing:** Shorter travel times translate directly into lower fuel/battery consumption.
        * **Modal Shifts:** Efficient digital public transit apps encourage commuters to abandon personal vehicles.
        """)
        
    st.markdown("---")
    st.subheader("🔄 Net Energy Balance Assessment")
    
    # Native Streamlit visualization using Python lists
    balance_data = {
        "Data Centers (Usage ↑)": 15,
        "On-Board Sensors (Usage ↑)": 8,
        "Network Infrastructure (Usage ↑)": 12,
        "Traffic Smoothness (Savings ↓)": -35,
        "Logistics Routing (Savings ↓)": -40,
        "Eco-Driving Adaptation (Savings ↓)": -20
    }
    
    st.write("Relative impact units on energy baseline (Positive values consume energy | Negative values save energy):")
    st.bar_chart(balance_data)
    st.info("💡 **Conclusion:** Though building and running ICT hardware creates a small rise in energy baseline usage, the broad optimization savings outpace the costs by an estimated ratio of **4:1** to **10:1**.")

# PAGE 3: Interactive Savings Calculator
elif page == "Interactive Savings Calculator":
    st.header("🧮 ICT Transport Savings Simulator")
    st.write("Adjust the parameters below to see how applying ICT strategies changes the net fuel consumption of a regional transport fleet.")
    
    st.sidebar.subheader("Fleet Specifications")
    fleet_size = st.sidebar.number_input("Total Number of Fleet Vehicles", min_value=1, max_value=100000, value=1000, step=50)
    avg_distance = st.sidebar.slider("Average Daily Distance per Vehicle (km)", min_value=10, max_value=500, value=120)
    base_fuel = st.sidebar.slider("Base Fuel Consumption (Liters per 100km)", min_value=5.0, max_value=40.0, value=12.0, step=0.5)
    
    st.sidebar.subheader("ICT Implementation Level")
    smart_routing = st.sidebar.checkbox("Enable Dynamic Smart Routing (Est. ~12% savings)")
    eco_driving = st.sidebar.checkbox("Enable Telematics & Eco-Driving Training (Est. ~8% savings)")
    traffic_opt = st.sidebar.checkbox("Enable Infrastructure Traffic Optimization (Est. ~10% savings)")
    
    # Pure Python mathematical calculations
    daily_base_energy = (fleet_size * avg_distance * base_fuel) / 100
    
    savings_pct = 0.0
    if smart_routing: savings_pct += 0.12
    if eco_driving: savings_pct += 0.08
    if traffic_opt: savings_pct += 0.10
    
    ict_overhead = (fleet_size * 0.15) if (smart_routing or eco_driving or traffic_opt) else 0.0
    
    daily_saved_energy = daily_base_energy * savings_pct
    net_daily_energy = daily_base_energy - daily_saved_energy + ict_overhead
    
    # Metric metrics components native to Streamlit
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Baseline Daily Consumption", f"{daily_base_energy:,.1f} L")
    kpi2.metric("ICT Optimized Daily Consumption", f"{net_daily_energy:,.1f} L", delta=f"-{(daily_saved_energy - ict_overhead):,.1f} L" if savings_pct > 0 else 0)
    
    efficiency_gain = (savings_pct * 100) - ((ict_overhead/daily_base_energy)*100 if daily_base_energy > 0 else 0)
    kpi3.metric("Net Energy Efficiency Gain", f"{efficiency_gain:.1f}%" if savings_pct > 0 else "0.0%")
    
    st.markdown("---")
    
    # Display comparison natively using a dictionary structure
    chart_comparison = {
        "Standard Fleet (No ICT)": daily_base_energy,
        "Optimized Fleet (With ICT)": net_daily_energy
    }
    st.write("Daily Fuel Consumption Comparison (Liters):")
    st.bar_chart(chart_comparison)

# Footer info
st.sidebar.markdown("---")
st.sidebar.caption("Developed for ICT Academic Project Framework | Powered by Streamlit")
