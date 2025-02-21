import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import cv2

class MarineEcosystemAnalyzer:
    def __init__(self):
        """
        Initialize advanced marine ecosystem analysis capabilities
        """
        # Pre-trained model placeholders (in a real-world scenario, these would be actual ML models)
        self.plastic_detection_model = self._load_plastic_detection_model()
        self.coral_health_model = self._load_coral_health_model()
        self.oil_spill_detection_model = self._load_oil_spill_model()
        self.hab_prediction_model = self._load_hab_model()

    def _load_plastic_detection_model(self):
        """
        Simulate a sophisticated plastic detection model
        Returns a dictionary of plastic type detection probabilities
        """
        return {
            'Microplastics': {'detection_weight': 0.3, 'ecological_impact': 0.8},
            'Fishing Nets': {'detection_weight': 0.2, 'ecological_impact': 0.7},
            'Plastic Bottles': {'detection_weight': 0.25, 'ecological_impact': 0.6},
            'Industrial Plastic Waste': {'detection_weight': 0.15, 'ecological_impact': 0.9}
        }

    def _load_coral_health_model(self):
        """
        Simulate an advanced coral health assessment model
        """
        return {
            'Healthy Coral': {'weight': 0.4, 'recovery_potential': 0.9},
            'Early Bleaching': {'weight': 0.3, 'recovery_potential': 0.6},
            'Advanced Bleaching': {'weight': 0.2, 'recovery_potential': 0.2},
            'Coral Disease': {'weight': 0.1, 'recovery_potential': 0.1}
        }

    def _load_oil_spill_model(self):
        """
        Simulate an oil spill detection and impact assessment model
        """
        return {
            'Severity Levels': {
                'Minor Spill': {'detection_weight': 0.4, 'ecological_impact': 0.3},
                'Moderate Spill': {'detection_weight': 0.3, 'ecological_impact': 0.6},
                'Major Spill': {'detection_weight': 0.2, 'ecological_impact': 0.9},
                'Catastrophic Spill': {'detection_weight': 0.1, 'ecological_impact': 1.0}
            }
        }

    def _load_hab_model(self):
        """
        Simulate a comprehensive HAB prediction model
        """
        return {
            'Risk Factors': {
                'Water Temperature': {'sensitivity': 0.3},
                'Nutrient Levels': {'sensitivity': 0.3},
                'Salinity': {'sensitivity': 0.2},
                'pH Levels': {'sensitivity': 0.2}
            }
        }

    def _load_biodiversity_model(self):
        """
        Simulate a marine biodiversity and water quality assessment model
        """
        return {
            'Species Diversity': {
                'Fish': {'health_index': 0.7, 'trend': 'declining'},
                'Mammals': {'health_index': 0.6, 'trend': 'stable'},
                'Invertebrates': {'health_index': 0.5, 'trend': 'declining'},
                'Plant Life': {'health_index': 0.4, 'trend': 'critical'}
            },
            'Water Quality': {
                'Dissolved Oxygen': {'optimal_range': (6.5, 8.5), 'importance': 0.3},
                'Turbidity': {'optimal_range': (0, 5), 'importance': 0.2},
                'Microplastic Count': {'optimal_range': (0, 10), 'importance': 0.3},
                'Chemical Pollutants': {'optimal_range': (0, 2), 'importance': 0.2}
            }
        }

    def analyze_plastic_waste(self, uploaded_image):
        """
        Perform detailed plastic waste analysis
        """
        st.subheader("Plastic Waste Analysis")
        
        st.markdown("""
        <small>This analysis shows the distribution of different types of plastic waste 
        and their ecological impact on marine environments.</small>
        """, unsafe_allow_html=True)
        
        # Create tabs for different aspects of analysis
        tab1, tab2 = st.tabs(["Distribution Analysis", "Impact Assessment"])
        
        with tab1:
            st.markdown("##### Distribution of Plastic Types")
            # Main visualization
            plt.figure(figsize=(8, 4))
            categories = list(self.plastic_detection_model.keys())
            probabilities = [self.plastic_detection_model[cat]['detection_weight'] for cat in categories]
            
            plt.bar(categories, probabilities)
            plt.title("Plastic Distribution by Type")
            plt.xlabel("Categories")
            plt.ylabel("Detection Probability")
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(plt)
        
        with tab2:
            st.markdown("##### Environmental Impact")
            # Key findings with explanations
            for category, details in self.plastic_detection_model.items():
                impact = details['ecological_impact']
                st.markdown(f"""
                **{category}**
                <small>Impact Score: {impact*100:.1f}% - 
                {self._get_impact_description(impact)}</small>
                """, unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("#### 📋 Recommended Actions")
        st.info("""
        • Reduce single-use plastics
        • Support local recycling programs
        • Choose sustainable alternatives
        """)

    def _get_impact_description(self, impact):
        """Helper method to provide impact descriptions"""
        if impact > 0.8:
            return "Severe impact requiring immediate attention"
        elif impact > 0.6:
            return "Significant impact on marine life"
        elif impact > 0.4:
            return "Moderate environmental concern"
        else:
            return "Lower impact but monitoring required"

    def analyze_coral_health(self, uploaded_image):
        """
        Coral reef health assessment
        """
        st.subheader("Coral Reef Health Assessment")
        
        # Main health status visualization
        plt.figure(figsize=(10, 6))
        categories = list(self.coral_health_model.keys())
        weights = [self.coral_health_model[cat]['weight'] for cat in categories]
        
        plt.pie(weights, labels=categories, autopct='%1.1f%%')
        plt.title("Coral Health Distribution")
        st.pyplot(plt)
        
        # Key health indicators
        st.write("#### Recovery Potential")
        for category, details in self.coral_health_model.items():
            st.write(f"**{category}**: {details['recovery_potential']*100:.1f}%")
        
        st.info("Key Stress Factors:\n"
                "• Ocean temperature\n"
                "• Water acidity\n"
                "• Environmental pollution")

    def analyze_oil_spill(self, uploaded_image):
        """
        Oil Spill Analysis
        """
        st.subheader("Oil Spill Impact Assessment")
        
        # Main severity visualization
        plt.figure(figsize=(10, 6))
        severity_levels = list(self.oil_spill_detection_model['Severity Levels'].keys())
        detection_weights = [
            self.oil_spill_detection_model['Severity Levels'][level]['detection_weight'] 
            for level in severity_levels
        ]
        
        plt.bar(severity_levels, detection_weights)
        plt.title("Spill Severity Analysis")
        plt.xlabel("Severity Level")
        plt.ylabel("Detection Probability")
        plt.xticks(rotation=45)
        st.pyplot(plt)
        
        # Impact summary
        st.write("#### Ecological Impact")
        for level, details in self.oil_spill_detection_model['Severity Levels'].items():
            st.write(f"**{level}**: {details['ecological_impact']*100:.1f}% impact severity")
        
        st.error("Critical Effects:\n"
                 "• Marine habitat damage\n"
                 "• Ecosystem disruption\n"
                 "• Biodiversity impact")

    def analyze_harmful_algal_bloom(self):
        """
        HAB risk assessment
        """
        st.subheader("Harmful Algal Bloom Risk Assessment")
        
        # Environmental inputs
        st.write("#### Environmental Parameters")
        water_temp = st.slider("Water Temperature (°C)", 20.0, 35.0, 25.0)
        nutrient_levels = st.slider("Nutrient Levels", 0.0, 10.0, 2.0)
        salinity = st.slider("Salinity", 30.0, 40.0, 35.0)
        ph_level = st.slider("pH Level", 6.0, 9.0, 8.0)
        
        # Risk calculation
        risk_factors = self.hab_prediction_model['Risk Factors']
        hab_risk_score = (
            risk_factors['Water Temperature']['sensitivity'] * (water_temp / 35) +
            risk_factors['Nutrient Levels']['sensitivity'] * (nutrient_levels / 10) +
            risk_factors['Salinity']['sensitivity'] * (1 - abs(salinity - 35) / 10) +
            risk_factors['pH Levels']['sensitivity'] * (1 - abs(ph_level - 8) / 2)
        )
        
        # Risk assessment
        risk_category = (
            "Critical" if hab_risk_score > 0.8 else 
            "High" if hab_risk_score > 0.6 else 
            "Moderate" if hab_risk_score > 0.4 else 
            "Low"
        )
        
        st.metric("Risk Level", risk_category)
        st.metric("Risk Score", f"{hab_risk_score*100:.1f}%")
        
        st.warning("Primary Concerns:\n"
                  "• Water quality degradation\n"
                  "• Marine life stress\n"
                  "• Ecosystem imbalance")

    def analyze_marine_health(self):
        """
        Comprehensive marine ecosystem health analysis
        """
        st.subheader("Marine Ecosystem Health Monitor")
        
        # Initialize biodiversity model if not exists
        if not hasattr(self, 'biodiversity_model'):
            self.biodiversity_model = self._load_biodiversity_model()

        # Water Quality Parameters Input
        st.write("#### Water Quality Parameters")
        dissolved_oxygen = st.slider("Dissolved Oxygen (mg/L)", 0.0, 10.0, 7.0)
        turbidity = st.slider("Turbidity (NTU)", 0.0, 20.0, 3.0)
        microplastic = st.slider("Microplastic Concentration (particles/L)", 0.0, 50.0, 5.0)
        chemical_pollution = st.slider("Chemical Pollutant Index", 0.0, 10.0, 1.0)

        # Calculate overall water quality score
        water_quality = self._calculate_water_quality(
            dissolved_oxygen, turbidity, microplastic, chemical_pollution
        )

        # Display Species Health Status
        st.write("#### Marine Species Health Status")
        species_data = self.biodiversity_model['Species Diversity']
        
        # Create health status visualization with smaller, more appropriate size
        plt.figure(figsize=(8, 4))  # Reduced from (10, 6) to (8, 4)
        categories = list(species_data.keys())
        health_indices = [species_data[cat]['health_index'] for cat in categories]
        
        colors = ['green' if idx > 0.6 else 'yellow' if idx > 0.4 else 'red' 
                 for idx in health_indices]
        
        # Create a more compact bar plot
        bars = plt.bar(categories, health_indices, color=colors)
        plt.title("Marine Species Health Index", pad=10)
        plt.ylabel("Health Score")
        plt.ylim(0, 1)
        plt.xticks(rotation=30, ha='right')  # Angled labels for better readability
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.2f}',
                    ha='center', va='bottom')
        
        plt.tight_layout()  # Adjust layout to prevent label cutoff
        st.pyplot(plt)

        # Display trend indicators and recommendations
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("#### Ecosystem Trends")
            for species, data in species_data.items():
                trend_icon = "🔴" if data['trend'] == 'critical' else "⚠️" if data['trend'] == 'declining' else "✅"
                st.write(f"{trend_icon} **{species}**: {data['trend'].title()}")

        with col2:
            st.write("#### Water Quality Score")
            quality_color = "green" if water_quality > 0.7 else "orange" if water_quality > 0.4 else "red"
            st.markdown(f"<h1 style='color: {quality_color}'>{water_quality:.1%}</h1>", unsafe_allow_html=True)

        # Conservation Recommendations
        st.write("#### Conservation Actions")
        self._display_conservation_recommendations(water_quality, health_indices)

    def _calculate_water_quality(self, oxygen, turbidity, microplastic, chemical):
        """
        Calculate overall water quality score
        """
        quality_model = self.biodiversity_model['Water Quality']
        
        # Calculate individual parameter scores
        oxygen_score = self._calculate_parameter_score(
            oxygen, quality_model['Dissolved Oxygen']['optimal_range'])
        turbidity_score = self._calculate_parameter_score(
            turbidity, quality_model['Turbidity']['optimal_range'])
        microplastic_score = self._calculate_parameter_score(
            microplastic, quality_model['Microplastic Count']['optimal_range'])
        chemical_score = self._calculate_parameter_score(
            chemical, quality_model['Chemical Pollutants']['optimal_range'])
        
        # Weighted average
        return (oxygen_score * 0.3 + 
                turbidity_score * 0.2 + 
                microplastic_score * 0.3 + 
                chemical_score * 0.2)

    def _calculate_parameter_score(self, value, optimal_range):
        """
        Calculate score for individual water quality parameters
        """
        min_val, max_val = optimal_range
        if min_val <= value <= max_val:
            return 1.0
        elif value < min_val:
            return max(0, 1 - (min_val - value) / min_val)
        else:
            return max(0, 1 - (value - max_val) / max_val)

    def _display_conservation_recommendations(self, water_quality, species_health):
        """
        Display targeted conservation recommendations
        """
        avg_species_health = sum(species_health) / len(species_health)
        
        if water_quality < 0.5 or avg_species_health < 0.5:
            st.error("Critical Actions Required:")
            st.write("• Implement immediate water quality improvement measures")
            st.write("• Establish protected marine zones")
            st.write("• Reduce industrial discharge")
            st.write("• Monitor species population regularly")
        else:
            st.success("Preventive Measures:")
            st.write("• Continue regular ecosystem monitoring")
            st.write("• Maintain sustainable fishing practices")
            st.write("• Support marine conservation programs")
            st.write("• Engage in community education")

def main():
    st.set_page_config(
        page_title="Marine Ecosystem Guardian",
        page_icon="🌊",
        layout="wide"
    )

    # Welcome section
    st.title("🌊 Marine Ecosystem Guardian")
    
    # Initial page selection
    page = st.sidebar.radio(
        "Navigation",
        ["Home", "Analysis Tools", "Prevention Guide", "About Project"]
    )

    if page == "Home":
        show_home_page()
    elif page == "Analysis Tools":
        show_analysis_tools()
    elif page == "Prevention Guide":
        show_prevention_guide()
    elif page == "About Project":
        show_about_page()

def show_home_page():
    st.markdown("""
    ### 🌊 Protecting Our Oceans Together
    
    Marine Ecosystem Guardian is an advanced monitoring and analysis platform designed to help protect our ocean ecosystems. 
    Our tools provide real-time insights into various marine environmental challenges.
    
    #### Key Features:
    1. 🔍 **Real-time Analysis** of marine environmental conditions
    2. 📊 **Data Visualization** for better understanding
    3. 🎯 **Actionable Insights** for conservation
    4. 🤝 **Community Engagement** in marine protection
    
    #### Why It Matters:
    - Ocean health directly impacts global climate
    - Marine biodiversity is crucial for ecosystem balance
    - Human activities significantly affect marine environments
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("##### Marine Health\nMonitor ecosystem vitality")
    with col2:
        st.warning("##### Pollution Impact\nTrack environmental threats")
    with col3:
        st.success("##### Conservation\nImplement protection measures")

def show_analysis_tools():
    analyzer = MarineEcosystemAnalyzer()
    
    # Analysis type selection with descriptions
    st.markdown("### 📊 Select Analysis Type")
    
    analysis_descriptions = {
        "Marine Ecosystem Health": "Monitor overall marine health, water quality, and species diversity",
        "Plastic Waste Impact": "Analyze plastic pollution distribution and impact (requires image)",
        "Coral Reef Health": "Assess coral reef conditions and bleaching status (requires image)",
        "Oil Spill Detection": "Evaluate oil spill severity and environmental effects (requires image)"
    }
    
    analysis_type = st.selectbox(
        "Choose your analysis focus",
        list(analysis_descriptions.keys())
    )

    if analysis_type == "Marine Ecosystem Health":
        analyzer.analyze_marine_health()
    elif analysis_type in ["Plastic Waste Impact", "Coral Reef Health", "Oil Spill Detection"]:
        uploaded_file = st.file_uploader(f"Upload {analysis_type} Image", type=["jpg", "png", "jpeg"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", width= 600)
            
            # Call appropriate analysis method
            if analysis_type == "Plastic Waste Impact":
                analyzer.analyze_plastic_waste(uploaded_file)
            elif analysis_type == "Coral Reef Health":
                analyzer.analyze_coral_health(uploaded_file)
            elif analysis_type == "Oil Spill Detection":
                analyzer.analyze_oil_spill(uploaded_file)
    
    elif analysis_type == "Marine Ecosystem Health":
        analyzer.analyze_marine_health()

def show_prevention_guide():
    st.markdown("""
    # 🛡️ Marine Protection Guidelines
    
    <style>
    .main-title {
        font-size: 32px;
        color: #ffffff;
        font-weight: 700;
        margin-bottom: 30px;
    }
    .section-title {
        font-size: 28px;
        color: #f0f0f0;
        font-weight: 600;
        margin: 25px 0 15px 0;
    }
    .subsection-title {
        font-size: 22px;
        color: #e0e0e0;
        font-weight: 500;
        margin: 20px 0 10px 0;
    }
    .list-items {
        font-size: 18px;
        color: #d0d0d0;
        line-height: 2;
        margin-left: 25px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Individual Actions Section
    st.markdown('<p class="section-title">Individual Actions</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<p class="subsection-title">Daily Habits</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="list-items">
        • Reduce single-use plastics<br>
        • Choose sustainable seafood<br>
        • Use reef-safe sunscreen<br>
        • Properly dispose of waste
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<p class="subsection-title">Active Participation</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="list-items">
        • Join beach cleanup events<br>
        • Support marine conservation groups<br>
        • Report marine pollution incidents<br>
        • Share awareness on social media
        </div>
        """, unsafe_allow_html=True)

    # Educational Resources Section
    st.markdown('<p class="section-title">📚 Educational Resources</p>', unsafe_allow_html=True)
    
    with st.expander("🎥 Must-Watch Documentaries"):
        st.markdown("""
        1. [**A Plastic Ocean**](https://www.netflix.com/title/80164032) - Netflix
        2. [**Chasing Coral**](https://www.chasingcoral.com/view-the-film/) - Netflix
        3. [**Mission Blue**](https://www.netflix.com/title/70308278) - Netflix
        4. [**Seaspiracy**](https://www.netflix.com/title/81014008) - Netflix
        """)

    with st.expander("📰 Informative Articles & Blogs"):
        st.markdown("""
        #### News Articles
        • [**National Geographic: Ocean Coverage**](https://www.nationalgeographic.com/environment/topic/oceans)
        • [**The Guardian: Ocean Pollution**](https://www.theguardian.com/environment/ocean-pollution)
        
        #### Scientific Blogs
        • [**NOAA's Ocean Blog**](https://blog.noaa.gov/)
        • [**Deep Sea News**](http://www.deepseanews.com/)
        • [**Ocean Conservancy Blog**](https://oceanconservancy.org/blog/)
        """)

    with st.expander("🎓 Educational YouTube Channels"):
        st.markdown("""
        1. [**National Geographic**](https://www.youtube.com/user/NationalGeographic)
        > Ocean documentaries and marine life features
        
        2. [**BBC Earth**](https://www.youtube.com/bbcearth)
        > High-quality ocean documentaries and marine life behavior
        
        3. [**Ocean Conservation Research**](https://www.youtube.com/c/OceanConservationResearch)
        > Scientific insights into marine conservation
        
        4. [**Coral Reef Research**](https://www.youtube.com/c/CoralReefResearch)
        > Focused content on coral reef ecosystems
        """)

    # Impact Statistics
    st.markdown('<p class="section-title">📊 Impact Statistics</p>', unsafe_allow_html=True)
    
    impact_col1, impact_col2, impact_col3 = st.columns(3)
    with impact_col1:
        st.metric("Plastic in Oceans", "8M tons/year", "↑ 3.2%")
    with impact_col2:
        st.metric("Coral Reef Loss", "50% since 1950", "↓ 4.7%")
    with impact_col3:
        st.metric("Marine Species at Risk", "2,270 species", "↑ 2.8%")

    # Call to Action
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; margin-top: 30px;">
    <p class="section-title" style="color: #1e90ff;">🎯 Take Action Today</p>
    <p style="font-size: 18px;">
    Join the global movement to protect our oceans. Start with small changes in your daily life 
    and become part of the solution. Remember, every action counts!
    </p>
    </div>
    """, unsafe_allow_html=True)

    # Additional Resources
    st.markdown('<p class="section-title">🔗 Useful Links</p>', unsafe_allow_html=True)
    
    with st.expander("Marine Conservation Organizations"):
        st.markdown("""
        • [Ocean Conservancy](https://oceanconservancy.org/)
        • [Marine Conservation Institute](https://marine-conservation.org/)
        • [Project AWARE](https://www.padi.com/aware)
        • [Sea Shepherd Conservation Society](https://seashepherd.org/)
        """)

    with st.expander("Report Environmental Issues"):
        st.markdown("""
        • [NOAA Marine Debris Program](https://marinedebris.noaa.gov/)
        • [Environmental Protection Agency](https://www.epa.gov/report-environment)
        • [Ocean Pollution Report](https://www.marinepolice.com/report-pollution)
        """)

def show_about_page():
    st.markdown("""
    ### About Marine Ecosystem Guardian
    
    This project combines advanced analytics with environmental science to protect our oceans.
    
    #### Technology Stack:
    - Image Analysis
    - Real-time Monitoring
    - Data Visualization
    - Predictive Analytics
    
    #### Future Developments:
    - Artificial Intelligence Integration
    - Mobile Application
    - Community Features
    - Global Data Integration
    """)

if __name__ == "__main__":
    main()