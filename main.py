import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

folder = './data/2023-08-03/'

# def pull():
#     plt.style.use('dark_background')
#     file_name = 'pull.csv'
#     csv_file = folder + file_name
#     data = pd.read_csv(csv_file)

#     fig, ax1 = plt.subplots(figsize=(18, 14))

#     ax1.plot(data['Vehicle speed (km/h)'], data['Engine Torque (N•m)'], label='Engine Torque', color='#e00b12', linestyle='-')
#     ax1.set_xlabel('Vehicle Speed (km/h)')
#     ax1.set_ylabel('Engine Torque (N•m)', color='#e00b12')

#     ax2 = ax1.twinx()
#     ax2.plot(data['Vehicle speed (km/h)'], data['Engine Power (hp)'], label='Engine Power', color='#9309de', linestyle='-')
#     ax2.set_ylabel('Engine Power (whp)', color='#9309de')

#     for x, y, rpm, bar in zip(data['Vehicle speed (km/h)'], data['Engine Power (hp)'], data['Engine RPM (RPM)'], data['Boost (bar)']):
#         ax2.scatter(x, y, color='#0aa6f5', s=20, alpha=0.5)
#         ax2.annotate(f'{rpm} RPM', (x, y), textcoords="offset points", xytext=(0, 9), ha='center', fontsize=9, color='#0aa6f5', alpha=0.7)
#         ax2.annotate(f'{bar} bar', (x, y), textcoords="offset points", xytext=(0, 24), ha='center', fontsize=12, color='#f5800a', alpha=0.7)

#     max_power_idx = data['Engine Power (hp)'].idxmax()
#     max_power_hp = data.loc[max_power_idx, 'Engine Power (hp)']
#     max_power_rpm = data.loc[max_power_idx, 'Engine RPM (RPM)']

#     max_torque_idx = data['Engine Torque (N•m)'].idxmax()
#     max_torque = data.loc[max_torque_idx, 'Engine Torque (N•m)']
#     max_torque_rpm = data.loc[max_torque_idx, 'Engine RPM (RPM)']

#     max_boost = data['Boost (bar)'].max()

#     label_text = f'{max_power_hp:.1f} whp @ {max_power_rpm} RPM\n{max_torque:.1f} N•m @ {max_torque_rpm} RPM\n{max_boost:.2f} bar'
#     plt.text(0.02, 0.98, label_text, transform=ax2.transAxes, ha='left', va='top', fontsize=12)

#     ax1.grid(True, axis='x', linewidth=0.5, color='#707070')

#     plt.savefig(f"{folder}/pull.png", bbox_inches='tight')

#     plt.show()



# def trip():
#     plt.style.use('dark_background')
#     file_name = 'trip.csv'
#     csv_file = folder + file_name
#     data = pd.read_csv(csv_file)

#     fig, ax1 = plt.subplots(figsize=(18, 14))

#     ax1.plot(data.index, data['Engine Torque (N•m)'], label='Engine Torque', color='#e00b12', linestyle='-')
#     ax1.set_xlabel('Index')
#     ax1.set_ylabel('Engine Torque (N•m)', color='#e00b12')

#     ax2 = ax1.twinx()
#     ax2.plot(data.index, data['Vehicle speed (km/h)'], label='Vehicle Speed', color='#9309de', linestyle='-')
#     ax2.set_ylabel('Vehicle Speed (km/h)', color='#9309de')

#     max_power_idx = data['Engine Power (hp)'].idxmax()
#     max_power_hp = data.loc[max_power_idx, 'Engine Power (hp)']
#     max_power_rpm = data.loc[max_power_idx, 'Engine RPM (RPM)']

#     max_torque_idx = data['Engine Torque (N•m)'].idxmax()
#     max_torque = data.loc[max_torque_idx, 'Engine Torque (N•m)']
#     max_torque_rpm = data.loc[max_torque_idx, 'Engine RPM (RPM)']

#     max_boost = data['Boost (bar)'].max()

#     label_text = f'{max_power_hp:.1f} whp @ {max_power_rpm} RPM\n{max_torque:.1f} N•m @ {max_torque_rpm} RPM\n{max_boost:.2f} bar'
#     plt.text(0.02, 0.98, label_text, transform=ax1.transAxes, ha='left', va='top', fontsize=12)

#     ax1.grid(True, axis='x', linewidth=0.5, color='#707070')

#     plt.savefig(f"{folder}/trip.png", bbox_inches='tight')

#     plt.show()



# def dyno():
#     plt.style.use('dark_background')
#     file_name = 'downhill.csv'
#     csv_file = folder + file_name
#     data = pd.read_csv(csv_file)

#     fig, ax1 = plt.subplots(figsize=(18, 14))

#     ax1.plot(data['Engine RPM (RPM)'], data['Engine Torque (N•m)'], label='Engine Torque', color='#e00b12', linestyle='-')
#     ax1.set_xlabel('Engine RPM (RPM)')
#     ax1.set_ylabel('Engine Torque (N•m)', color='#e00b12')

#     ax2 = ax1.twinx()
#     ax2.plot(data['Engine RPM (RPM)'], data['Engine Power (hp)'], label='Engine Power', color='#9309de', linestyle='-')
#     ax2.set_ylabel('Engine Power (whp)', color='#9309de')

#     max_power_idx = data['Engine Power (hp)'].idxmax()
#     max_power_hp = data.loc[max_power_idx, 'Engine Power (hp)']
#     max_power_rpm = data.loc[max_power_idx, 'Engine RPM (RPM)']

#     max_torque_idx = data['Engine Torque (N•m)'].idxmax()
#     max_torque = data.loc[max_torque_idx, 'Engine Torque (N•m)']
#     max_torque_rpm = data.loc[max_torque_idx, 'Engine RPM (RPM)']

#     max_boost = data['Boost (bar)'].max()

#     label_text = f'{max_power_hp:.1f} whp @ {max_power_rpm} RPM\n{max_torque:.1f} N•m @ {max_torque_rpm} RPM\n{max_boost:.2f} bar'
#     plt.text(0.02, 0.98, label_text, transform=ax2.transAxes, ha='left', va='top', fontsize=12)

#     ax1.grid(True, axis='x', linewidth=0.5, color='#707070')

#     plt.savefig(f"{folder}/dyno.png", bbox_inches='tight')

#     plt.show()



def dyno():
    file_name = 'uphill.csv'
    csv_file = folder + file_name
    data = pd.read_csv(csv_file)

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=data['Engine RPM (RPM)'], y=data['Engine Torque (N•m)'],
                             mode='lines', name='Engine Torque', line=dict(color='#e00b12')))

    fig.add_trace(go.Scatter(x=data['Engine RPM (RPM)'], y=data['Engine Power (hp)'],
                             mode='lines', name='Engine Power', line=dict(color='#9309de')), secondary_y=True)

    fig.update_xaxes(title_text='Engine RPM (RPM)')
    fig.update_yaxes(title_text='Engine Torque (N•m)', color='#e00b12', secondary_y=False)
    fig.update_yaxes(title_text='Engine Power (whp)', color='#9309de', secondary_y=True)

    max_power_idx = data['Engine Power (hp)'].idxmax()
    max_power_hp = data.loc[max_power_idx, 'Engine Power (hp)']
    max_power_rpm = data.loc[max_power_idx, 'Engine RPM (RPM)']

    max_torque_idx = data['Engine Torque (N•m)'].idxmax()
    max_torque = data.loc[max_torque_idx, 'Engine Torque (N•m)']
    max_torque_rpm = data.loc[max_torque_idx, 'Engine RPM (RPM)']

    max_boost = data['Boost (bar)'].max()

    label_text = f'{max_power_hp:.1f} whp @ {max_power_rpm} RPM\n{max_torque:.1f} N•m @ {max_torque_rpm} RPM\n{max_boost:.2f} bar'
    fig.add_annotation(
        go.layout.Annotation(
            text=label_text,
            x=0.02,
            y=0.98,
            xref='paper',
            yref='paper',
            showarrow=False,
            align='left',
            valign='top',
            font=dict(size=12)
        )
    )

    fig.update_layout(
        template='plotly_dark',
        width=900,
        height=700,
        margin=dict(l=40, r=40, t=40, b=40),
    )

    fig.write_image(f"{folder}/uphill.png")
    fig.show()


if __name__ == "__main__":
    dyno()