# <span style="color:#48D1CC; font-size:28px; font-weight:bold; text-shadow: 0 0 10px #48D1CC;">Innovate with GoIStats: HCES 2022-23 Analysis</span>
**<span style="color:#00BFFF; font-size:20px; text-shadow: 0 0 8px #00BFFF;">A Data-Driven Approach to Bridging Urban-Rural Divides for Viksit Bharat</span>**

![Dashboard Demo](DASHBOARD/screenshots/dashboard_demo.gif)

---

## <span style="color:#FFD700; text-shadow: 0 0 8px #FFD700;">Table of Contents</span>
- [<span style="color:#87CEEB;">Project Overview</span>](#project-overview)
- [<span style="color:#87CEEB;">Repository Structure</span>](#repository-structure)
- [<span style="color:#87CEEB;">Installation</span>](#installation)
- [<span style="color:#87CEEB;">Getting Started</span>](#getting-started)
- [<span style="color:#87CEEB;">Data Processing & Visualization</span>](#data-processing--visualization)
- [<span style="color:#87CEEB;">Dashboard Features</span>](#dashboard-features)
- [<span style="color:#87CEEB;">Reproducibility</span>](#reproducibility)
- [<span style="color:#87CEEB;">Ethical Compliance</span>](#ethical-compliance)
- [<span style="color:#87CEEB;">Contributing</span>](#contributing)
- [<span style="color:#87CEEB;">License</span>](#license)
- [<span style="color:#87CEEB;">Contact</span>](#contact)

---

## <span style="color:#32CD32; text-shadow: 0 0 8px #32CD32;">Project Overview</span>
This project analyzes the **Household Consumer Expenditure Survey (HCES) 2022-23** dataset to generate actionable insights for India’s *Viksit Bharat* initiative. Key focus areas include:
- **Digital Divide:** Urban vs. rural internet penetration and online transactions.
- **Expenditure Patterns:** Monthly consumption trends and subsidy impacts.
- **Policy Tools:** Interactive dashboard for evidence-based decision-making.

**Key Features:**
- Parallel processing of 15 hierarchical datasets.
- Dynamic visualizations (choropleth maps, heatmaps).
- Real-time policy impact simulation.

---

## <span style="color:#FF4500; text-shadow: 0 0 8px #FF4500;">Repository Structure</span>
```bash
GoIStats_2025/
├── CONCLUSION/               # Final reports and policy recommendations
├── DASHBOARD/               # Streamlit dashboard code and assets
│   ├── app.py               # Dashboard main script
│   ├── assets/              # CSS, images, and geojson files
│   ├── requirements.txt     # Moved inside DASHBOARD
├── DOCUMENTATION/           # MoSPI documentation and layout files
│   ├── Layout_HCES_2022-23.xls
│   ├── Tabulation_state_code.xlsx
├── OUTPUT/                  # Processed datasets and visualizations
│   ├── results.csv
│   ├── plots/
├── RAWDATA/                 # Raw HCES 2022-23 microdata (15 levels)
│   ├── hces22_lvl_01.TXT
│   └── ...
├── Untitled.py              # Data preprocessing script
└── README.md
```

---

## <span style="color:#1E90FF; text-shadow: 0 0 8px #1E90FF;">Installation</span>

### Prerequisites
- Python 3.10
- Git

### Steps
1. Clone the Repository:
   ```bash
   git clone https://github.com/abhi-1408-shek/GoIStats_2025.git
   cd GoIStats_2025
   ```

2. Install Dependencies:
   ```bash
   pip install -r DASHBOARD/requirements.txt
   ```

---

## <span style="color:#DAA520; text-shadow: 0 0 8px #DAA520;">Getting Started</span>

### 1. Data Preprocessing
Run the preprocessing script to clean and merge raw data:
```bash
python Untitled.py
```
*Output:* `OUTPUT/results.csv` (processed dataset).

### 2. Launch Interactive Dashboard
```bash
streamlit run DASHBOARD/app.py
```
Access the dashboard at `http://localhost:8501`.

---

## <span style="color:#FFA500; text-shadow: 0 0 8px #FFA500;">Data Processing & Visualization</span>

### Workflow
1. **Data Ingestion:** Parse fixed-width files using `Layout_HCES_2022-23.xls`.
2. **Household Consolidation:** Generate `HH_ID` for merging 15 hierarchical levels.
3. **Visualization:**
   - **Choropleth Maps:** State-wise internet penetration.
   - **Heatmaps:** Correlation between education and healthcare spending.

![Data Workflow](DOCUMENTATION/workflow.png)

---

## <span style="color:#7CFC00; text-shadow: 0 0 8px #7CFC00;">Dashboard Features</span>
### Interactive Filters
- **State:** Compare metrics across 36 states/UTs.
- **Sector:** Urban vs. rural trends.
- **Year:** Analyze temporal patterns (2020–2023).

### Visualization Tools
1. **Geospatial Analysis:**
   - Highlight low-adoption states (e.g., Bihar, Odisha).
2. **Policy Simulation:**
   - Estimate the impact of doubling rural internet coverage.
3. **Real-Time Updates:**
   - Dynamic charts adjust to filters instantly.

---

## <span style="color:#00FA9A; text-shadow: 0 0 8px #00FA9A;">Reproducibility</span>
### Key Practices
- **Version Control:** All code and data are Git-tracked.
- **Modular Code:** Reusable scripts for preprocessing and visualization.
- **Documentation:** Detailed variable definitions in `DOCUMENTATION/`.

---

## <span style="color:#FF6347; text-shadow: 0 0 8px #FF6347;">Ethical Compliance</span>
- **Anonymization:** Removed `HH_ID` and sensitive fields.
- **Data Usage:** Compliant with MoSPI’s non-disclosure guidelines.
- **Licensing:** Raw data is non-shareable (see [MoSPI Terms](https://mospi.gov.in)).

---

## <span style="color:#EE82EE; text-shadow: 0 0 8px #EE82EE;">Contributing</span>
1. Fork the repository.
2. Create a branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Submit a PR with a detailed description.

---

## <span style="color:#00CED1; text-shadow: 0 0 8px #00CED1;">License</span>
This project is licensed under **MIT License** (code) and **MoSPI NDA** (data).

---

## <span style="color:#DC143C; text-shadow: 0 0 8px #DC143C;">Contact</span>
**Team:** Abhishek Sharma  
**Email:** your.email@example.com  
**GitHub Issues:** [Report Here](https://github.com/abhi-1408-shek/GoIStats_2025/issues)

---

*<span style="color:#FF1493; text-shadow: 0 0 8px #FF1493;">Submitted to MoSPI’s "Innovate with GoIStats" Hackathon 2025.</span>*

