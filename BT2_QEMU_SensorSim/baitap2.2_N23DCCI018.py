import matplotlib.pyplot as plt


def plot_chart(x, distances, span):
    fig, ax = plt.subplots()

    # Đường span màu đỏ nét đứt
    ax.axhline(
        y=span,
        color='r',
        linestyle='--',
        linewidth=2,
        label=f'Span = {span:.0f} cm'
    )

    # Tô vùng span
    ax.fill_between(
        x,
        0,
        [min(d, span) for d in distances],
        alpha=0.2,
        color='red',
        label='Vùng Span'
    )

    # Tiêu đề + nhãn
    ax.set_title('Ultrasonic Sensor Simulation — Span Detection')
    ax.set_xlabel('Sample')
    ax.set_ylabel('Distance (cm)')
    ax.set_ylim(0, max(distances) + 10)

    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('sensor_chart.png', dpi=150)

    print("Saved: sensor_chart.png")


if __name__ == "__main__":
    # dữ liệu test mẫu (để chạy CI không lỗi)
    x = list(range(10))
    distances = [10, 20, 30, 25, 15, 40, 35, 20, 10, 5]
    span = 25

    plot_chart(x, distances, span)
