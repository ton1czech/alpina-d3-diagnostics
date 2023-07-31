import matplotlib.pyplot as plt
import pandas as pd

folder = './data/2023-07-30/'

def pull():
    file_name = 'pull.csv'
    csv_file = folder + file_name
    data = pd.read_csv(csv_file)

    fig, ax1 = plt.subplots(figsize=(18, 14))

    ax1.plot(data['Vehicle speed (km/h)'], data['Engine Torque (N•m)'], label='Engine Torque (N•m)', color='blue', linestyle='-')
    ax1.set_xlabel('Vehicle Speed (km/h)')
    ax1.set_ylabel('Engine Torque (N•m)', color='blue')

    ax2 = ax1.twinx()
    ax2.plot(data['Vehicle speed (km/h)'], data['Engine Power (hp)'], label='Engine Power (whp)', color='green', linestyle='-')
    ax2.set_ylabel('Engine Power (hp)', color='green')

    for x, y, rpm, bar in zip(data['Vehicle speed (km/h)'], data['Engine Power (hp)'], data['Engine RPM (RPM)'], data['Boost (bar)']):
        ax2.scatter(x, y, color='red', s=10, alpha=0.5)
        ax2.annotate(f'{rpm} RPM', (x, y), textcoords="offset points", xytext=(0, 9), ha='center', fontsize=9, color='red', alpha=0.7)
        ax2.annotate(f'{bar} bar', (x, y), textcoords="offset points", xytext=(0, 24), ha='center', fontsize=12, color='purple', alpha=0.7)

    max_power_hp = data['Engine Power (hp)'].max()
    max_rpm = data['Engine RPM (RPM)'].max()
    max_torque = data['Engine Torque (N•m)'].max()
    max_boost = data['Boost (bar)'].max()
    label_text = f'{max_power_hp:.1f} whp @ {max_rpm} RPM\n{max_torque:.1f} N•m\n{max_boost:.2f} bar'
    plt.text(0.02, 0.98, label_text, transform=ax2.transAxes, ha='left', va='top', fontsize=12)

    plt.grid(True)

    plt.savefig(f"{folder}/pull.png", bbox_inches='tight')

    plt.show()

if __name__ == "__main__":
    pull()
