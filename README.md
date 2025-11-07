# Construction & Warehouse Project Cost Analysis Dashboard

**Project Overview:**  
This project analyzes 30 warehouse projects (Zepto, Flipkart, Swiggy, Dunzo, BigBasket) including civil and electrical work (cabin setup, racks, cold rooms, AC points, wiring, flooring).  
It calculates total costs, profit margins, and visualizes data using Python and Power BI dashboards to help management track project performance and profitability.

## Tools & Technologies

- **Python** (Pandas, Matplotlib) for ETL, cleaning, and analysis  
- **Power BI Desktop** for interactive dashboards  
- **GitHub** for version control and portfolio  
- **Skills Demonstrated:** Data Cleaning, ETL, Dashboard Reporting, Cost Analysis, Data Visualization, KPI Tracking

## Dataset

- **Number of Projects:** 30  
- **Columns:**  
  - Project Name  
  - Client  
  - Location  
  - Work Type (Civil/Electrical)  
  - Work Description  
  - Material Cost  
  - Labor Cost  
  - Equipment Cost  
  - Total Cost  
  - Profit Margin (%)  
  - Profit Value  
  - Start Date  
  - End Date  
  - Project Status  
- **CSV Files:**  
  - `warehouse_projects_data.csv` → raw data  
  - `cleaned_warehouse_projects.csv` → processed data used in dashboards

## Power BI Dashboard Preview

### Dashboard images
![Dashboard](dashboard/screenshots/dashboard.png)

### Total Cost Comparison and Profit Margin per Project
![Profit Margin Chart](dashboard/screenshots/total_cost_chart.png)

### Project status summary and work type distribution
![Project status summary](dashboard/screenshots/Project_status_summary.png)

## Key Insights

- Zepto and Flipkart projects had the highest total costs due to complex civil and electrical setups.  
- Projects with optimized labor and material usage achieved profit margins above 15%.  
- The dashboard helps management quickly identify over-budget projects and plan resources efficiently.  

## How to Run

1. Open Python project in PyCharm  
2. Place `warehouse_projects_data.csv` in `data/` folder  
3. Run `scripts/analyze_costs.py` → generates `cleaned_warehouse_projects.csv`  
4. Open Power BI Desktop → load `cleaned_warehouse_projects.csv` → explore dashboard visuals  

## Contact
 
- GitHub: https://github.com/Pavan-klaus
