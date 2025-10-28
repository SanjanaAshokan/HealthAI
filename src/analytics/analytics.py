import plotly.express as px

def plot_vitals_time_series(df):
    # expects timestamp, heart_rate, bp_sys, bp_dia, glucose
    fig = px.line(df, x="timestamp", y=["heart_rate", "bp_sys", "bp_dia", "glucose"],
                  labels={"value":"Measurement", "timestamp":"Time"}, title="Vitals Over Time")
    return fig
