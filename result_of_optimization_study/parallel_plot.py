import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load both datasets
df_all = pd.read_csv(r"F:\Preetham\Optimization\optimization_designs_data_table.csv")
df_pareto = pd.read_csv(r"F:\Preetham\Optimization\result_of_optimization_study\pareto_front_solutions.csv")

# Define the columns to use
columns = [
    'Core Diameter [mm]',
    'Blade Count',
    'Blade Angle [deg]',
    'Blade Height [mm]',
    'Eff Sep Cham Length [mm]',
    'Imm Pipe Diameter [mm]',
    'Imm Pipe Length [mm]',
    'Swirl Number',
    'Pressure Drop [Pa]',
    'Centrifugal Acceleration [m/s²]'
]

# Identify Pareto designs
pareto_designs = df_pareto['Design Number'].unique()
df_all['Is Pareto'] = df_all['Design Number'].apply(lambda x: 1 if x in pareto_designs else 0)

# Split into two DataFrames
df_pareto_only = df_all[df_all['Is Pareto'] == 1].copy()
df_non_pareto = df_all[df_all['Is Pareto'] == 0].copy()

# Assign each Pareto design a unique numeric color ID
design_to_id = {design: idx for idx, design in enumerate(df_pareto_only['Design Number'].unique())}
df_pareto_only['Color ID'] = df_pareto_only['Design Number'].map(design_to_id)

# Plot Pareto designs with unique colors (using numeric IDs)
fig = px.parallel_coordinates(
    df_pareto_only,
    dimensions=columns,
    color='Color ID',
    color_continuous_scale='Turbo',
    title="Parallel Coordinates Plot with Unique Colors for Pareto Designs"
)

# Optional: Add non-Pareto designs in light grey (as background)
for _, row in df_non_pareto.iterrows():
    fig.add_trace(
        go.Parcoords(
            line=dict(color='lightgrey'),
            dimensions=[dict(label=col, values=[row[col]]) for col in columns],
            name='Non-Pareto'
        )
    )

fig.show()

#---------------------------------
