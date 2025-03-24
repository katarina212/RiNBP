import matplotlib.pyplot as plt
import os


def generate_trade_offs_image():
    """
    Generate an image visualizing trade-offs between different database designs.
    This visualization shows the balance between different database properties
    like consistency, availability, and partition tolerance.
    """
    print("Generating trade-offs visualization...")

    # Create a figure
    plt.figure(figsize=(12, 8))

    # Set the title
    plt.suptitle('Database Trade-offs', fontsize=20, fontweight='bold')

    # Define axes
    ax = plt.gca()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')  # Hide the axes

    # Example: Draw a triangle to represent CAP theorem
    # Here you would add code to draw the CAP theorem triangle
    # with vertices labeled Consistency, Availability, and Partition Tolerance

    # Example: Create a spectrum showing the trade-offs
    # For example, a horizontal bar showing the spectrum from
    # ACID (traditional RDBMS) to BASE (NoSQL systems)

    # Example: Add annotations to highlight specific trade-offs
    plt.annotate(
        'Example trade-off note',
        xy=(5, 5), xytext=(6, 6),
        arrowprops=dict(arrowstyle='->'),
        fontsize=12
    )

    # Add a legend or explanation
    plt.figtext(
        0.5, 0.05,
        "This visualization shows the fundamental trade-offs in database "
        "design.\n"
        "Different database systems make different choices based on their "
        "use cases.",
        ha='center', fontsize=10
    )

    # Save the figure
    plt.savefig('images/trade-offs.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Trade-offs image saved to images/trade-offs.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_trade_offs_image()