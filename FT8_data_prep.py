import pandas as pd


def prepare_rst_long_data(data: pd.DataFrame, x_column: str) -> pd.DataFrame:
    """Return long-format RST data for consistent SENT/RCVD plotting."""
    plot_data = data.copy()
    plot_data['RST_SENT'] = pd.to_numeric(plot_data['RST_SENT'], errors='coerce')
    plot_data['RST_RCVD'] = pd.to_numeric(plot_data['RST_RCVD'], errors='coerce')
    plot_data = plot_data.dropna(subset=[x_column, 'RST_SENT', 'RST_RCVD']).copy()
    return plot_data.melt(
        id_vars=[x_column],
        value_vars=['RST_SENT', 'RST_RCVD'],
        var_name='RST_TYPE',
        value_name='RST_VALUE'
    )


def prepare_rst_line_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return DATE/RST rows cleaned for line plots."""
    plot_data = data.copy()
    plot_data['DATE'] = pd.to_datetime(plot_data['DATE'], errors='coerce')
    plot_data['RST_SENT'] = pd.to_numeric(plot_data['RST_SENT'], errors='coerce')
    plot_data['RST_RCVD'] = pd.to_numeric(plot_data['RST_RCVD'], errors='coerce')
    return plot_data.dropna(subset=['DATE', 'RST_SENT', 'RST_RCVD']).sort_values('DATE')


def prepare_mean_rst_line_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return DATE-grouped mean RST rows for line plots."""
    plot_data = prepare_rst_line_data(data)
    if plot_data.empty:
        return plot_data
    return plot_data.groupby('DATE', as_index=False).agg({'RST_SENT': 'mean', 'RST_RCVD': 'mean'})


def prepare_time_adl_rst_plot_data(data: pd.DataFrame) -> pd.DataFrame:
    """Return long-format TIME_ADL/RST data used by TIME_ADL scatter plots."""
    plot_data = data.copy()
    # Accept raw HH:MM:SS strings, datetime values, and Python time objects.
    time_values = pd.to_datetime(plot_data['TIME_ADL'], errors='coerce')
    if time_values.isna().any():
        fallback_values = pd.to_datetime(
            plot_data['TIME_ADL'].astype(str),
            format='%H:%M:%S',
            errors='coerce'
        )
        time_values = time_values.fillna(fallback_values)
    plot_data['TIME_ADL'] = time_values
    plot_data['RST_SENT'] = pd.to_numeric(plot_data['RST_SENT'], errors='coerce')
    plot_data['RST_RCVD'] = pd.to_numeric(plot_data['RST_RCVD'], errors='coerce')
    plot_data = plot_data.dropna(subset=['TIME_ADL', 'RST_SENT', 'RST_RCVD']).copy()
    plot_data = plot_data.sort_values(by='TIME_ADL', ascending=True).reset_index(drop=True)
    return plot_data.melt(
        id_vars=['TIME_ADL', 'BAND'],
        value_vars=['RST_SENT', 'RST_RCVD'],
        var_name='RST_TYPE',
        value_name='RST_VALUE'
    )
