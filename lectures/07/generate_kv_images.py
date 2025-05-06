# flake8: noqa
import os
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, Rectangle

# Output directory relative to this script
IMG_DIR = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(IMG_DIR, exist_ok=True)


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(IMG_DIR, name), dpi=300)
    plt.close(fig)


###########################################################
# 1. Consistent Hashing Ring
###########################################################

def generate_consistent_hashing_image():
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Draw ring
    ring = Circle((0.5, 0.5), 0.45, fill=False, lw=2, color="#1f77b4")
    ax.add_patch(ring)

    # Draw nodes on ring
    nodes = [0, 60, 140, 220, 300]
    for angle in nodes:
        x = 0.5 + 0.45 * np.cos(np.deg2rad(angle))
        y = 0.5 + 0.45 * np.sin(np.deg2rad(angle))
        ax.plot(x, y, "o", color="#ff7f0e", markersize=10)
        ax.text(  # noqa: E501
            x,
            y,
            f"N{nodes.index(angle)+1}",
            ha="center",
            va="center",
            color="white",
            fontsize=8,
            fontweight="bold",
        )

    ax.text(0.5, 1.02, "Consistent Hashing Ring", ha="center", va="bottom", fontsize=12, fontweight="bold")  # noqa: E501
    save(fig, "consistent_hashing_ring.png")


###########################################################
# 2. Master-Slave vs Masterless
###########################################################

def generate_replication_models_image():
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))
    titles = ["Master-Slave", "Masterless"]
    for idx, ax in enumerate(axes):
        ax.axis("off")
        if idx == 0:
            # master-slave
            ax.text(0.5, 0.9, titles[idx], ha="center", fontsize=10, fontweight="bold")  # noqa: E501
            ax.add_patch(Rectangle((0.4, 0.6), 0.2, 0.1, color="#1f77b4"))  # noqa: E501
            ax.text(0.5, 0.65, "Master", ha="center", color="white")  # noqa: E501
            slave_y = 0.3
            for s in range(3):
                x = 0.2 + s * 0.3
                ax.add_patch(Rectangle((x, slave_y), 0.2, 0.1, color="#ff7f0e"))  # noqa: E501
                ax.text(x + 0.1, slave_y + 0.05, f"S{s+1}", ha="center", color="white")  # noqa: E501
                # arrow
                ax.add_patch(  # noqa: E501
                    FancyArrowPatch((0.5, 0.6), (x + 0.1, slave_y + 0.1), arrowstyle="->", mutation_scale=15)
                )
        else:
            # masterless ring of 4
            ax.text(0.5, 0.9, titles[idx], ha="center", fontsize=10, fontweight="bold")  # noqa: E501
            coords = [(0.2, 0.6), (0.7, 0.6), (0.2, 0.2), (0.7, 0.2)]
            for i, (x, y) in enumerate(coords):
                ax.add_patch(Rectangle((x, y), 0.15, 0.1, color="#2ca02c"))
                ax.text(x + 0.075, y + 0.05, f"N{i+1}", ha="center", color="white")  # noqa: E501
                # arrows clockwise
            for i in range(4):
                x1, y1 = coords[i]
                x2, y2 = coords[(i + 1) % 4]
                ax.add_patch(  # noqa: E501
                    FancyArrowPatch(
                        (x1 + 0.075, y1),
                        (x2 + 0.075, y2 + 0.1),
                        arrowstyle="->",
                        mutation_scale=12,
                    )
                )
    save(fig, "replication_models.png")


###########################################################
# 3. Key Prefix Design
###########################################################

def generate_key_prefix_image():
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axis("off")
    sample_keys = [  # noqa: E501
        "wu:123e4567",
        "ctx:42",
        "ts:ctx42:1700000000:123e4567",
        "meta:priority:high:123e4567",
    ]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]
    for i, key in enumerate(sample_keys):
        ax.text(0.02, 0.9 - i * 0.2, key, fontsize=10, color=colors[i])
    ax.text(0.5, -0.1, "Strategija prefiksa ključeva", ha="center", fontsize=12, fontweight="bold")
    save(fig, "key_prefixes.png")


###########################################################
# 4. Latency Comparison Chart
###########################################################

def generate_latency_chart():
    fig, ax = plt.subplots(figsize=(4, 3))
    categories = ["RAM (Redis)", "SSD (BeaverDB)", "HDD"]
    latency = [0.2, 2, 10]  # u ms
    ax.bar(categories, latency, color=["#1f77b4", "#ff7f0e", "#2ca02c"])
    ax.set_ylabel("Latencija (ms)")
    ax.set_title("Usporedba latencija čitanja")
    save(fig, "latency_comparison.png")


###########################################################
# 5. Secondary Indexing Flow
###########################################################

def generate_secondary_index_image():
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.axis("off")
    ax.add_patch(Rectangle((0.05, 0.3), 0.25, 0.2, color="#1f77b4"))  # noqa: E501
    ax.text(0.175, 0.4, "Write", ha="center", color="white")
    ax.add_patch(  # noqa: E501
        FancyArrowPatch((0.3, 0.4), (0.45, 0.4), arrowstyle="->", mutation_scale=15)
    )

    ax.add_patch(Rectangle((0.45, 0.6), 0.25, 0.2, color="#ff7f0e"))
    ax.text(0.575, 0.7, "Primary KV", ha="center", color="white")

    ax.add_patch(Rectangle((0.45, 0.1), 0.25, 0.2, color="#2ca02c"))
    ax.text(0.575, 0.2, "Index KV", ha="center", color="white")

    ax.add_patch(  # noqa: E501
        FancyArrowPatch((0.575, 0.6), (0.575, 0.3), arrowstyle="->", mutation_scale=15)
    )
    ax.text(0.76, 0.35, "prefiks→scan", fontsize=9)
    ax.set_title("Sekundarno indeksiranje u KV bazi")
    save(fig, "secondary_index_flow.png")


###########################################################
# 6. BeaverDB Architecture (simplified)
###########################################################

def generate_beaver_architecture_image():
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.axis("off")
    ax.add_patch(Rectangle((0.2, 0.75), 0.6, 0.15, color="#1f77b4"))
    ax.text(0.5, 0.825, "App / Engram", ha="center", color="white")

    ax.add_patch(  # noqa: E501
        FancyArrowPatch((0.5, 0.75), (0.5, 0.55), arrowstyle="->", mutation_scale=15)
    )

    ax.add_patch(Rectangle((0.2, 0.4), 0.6, 0.15, color="#ff7f0e"))
    ax.text(0.5, 0.475, "BeaverDB Engine", ha="center", color="white")

    ax.add_patch(  # noqa: E501
        FancyArrowPatch((0.5, 0.4), (0.5, 0.2), arrowstyle="->", mutation_scale=15)
    )

    ax.add_patch(Rectangle((0.2, 0.05), 0.6, 0.15, color="#2ca02c"))
    ax.text(0.5, 0.125, "Disk (WAL + SST)", ha="center", color="white")

    ax.set_title("Pojednostavljena arhitektura BeaverDB-a")
    save(fig, "beaver_architecture.png")


if __name__ == "__main__":
    import numpy as np

    generate_consistent_hashing_image()
    generate_replication_models_image()
    generate_key_prefix_image()
    generate_latency_chart()
    generate_secondary_index_image()
    generate_beaver_architecture_image()
    print("KV lecture images generated in", IMG_DIR)