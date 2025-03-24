import matplotlib.pyplot as plt
import os
import textwrap


def generate_acid_vs_base_image():
    """
    Generate visualization comparing ACID and BASE models
    for transactional properties in databases.
    """
    print("Generating ACID vs BASE comparison visualization...")

    # Create figure with increased size for better text visibility
    plt.figure(figsize=(14, 10))

    # Define columns for ACID and BASE
    ax = plt.gca()
    ax.axis('off')

    # Draw two boxes for ACID and BASE
    acid_rect = plt.Rectangle(
        (0.05, 0.22), 0.4, 0.68,
        facecolor='#d5e8d4', alpha=0.5, edgecolor='black'
    )
    base_rect = plt.Rectangle(
        (0.55, 0.22), 0.4, 0.68,
        facecolor='#dae8fc', alpha=0.5, edgecolor='black'
    )
    ax.add_patch(acid_rect)
    ax.add_patch(base_rect)

    # Add titles
    plt.text(0.25, 0.92, 'ACID', fontsize=28, fontweight='bold', ha='center')
    plt.text(0.75, 0.92, 'BASE', fontsize=28, fontweight='bold', ha='center')

    # Add subtitle - typical database systems
    plt.text(
        0.25, 0.87, '(Tradicionalne relacijske baze)',
        fontsize=13, ha='center', style='italic'
    )
    plt.text(
        0.75, 0.87, '(Mnoge NoSQL baze)',
        fontsize=13, ha='center', style='italic'
    )

    # ACID properties with more vertical space
    acid_props = [
        {"name": "Atomicity", "desc": "Atomičnost - sve ili ništa",
         "pos": 0.82},
        {"name": "Consistency", "desc": "Konzistentnost - očuvanje pravila",
         "pos": 0.72},
        {"name": "Isolation", "desc": "Izoliranost - neovisno izvršavanje",
         "pos": 0.62},
        {"name": "Durability", "desc": "Trajnost - zapisano zauvijek",
         "pos": 0.52}
    ]

    for prop in acid_props:
        plt.text(
            0.1, prop["pos"], "•", fontsize=20, ha='center',
            fontweight='bold', color='green'
        )
        plt.text(
            0.15, prop["pos"], prop["name"],
            fontsize=18, fontweight='bold'
        )
        plt.text(0.15, prop["pos"]-0.04, prop["desc"], fontsize=14)

    # BASE properties with more spacing between them
    base_props = [
        {"name": "Basically Available",
         "desc": "Osnovno dostupni - svaki zahtjev dobiva odgovor",
         "pos": 0.82},
        {"name": "Soft state",
         "desc": "Promjenjivo stanje - stanje može mijenjati bez unosa",
         "pos": 0.72},
        {"name": "Eventually consistent",
         "desc": "Eventualno konzistentni - s vremenom će "
                 "postati konzistentni",
         "pos": 0.60}  # Lowered position to provide more space
    ]

    # Draw the BASE property bullets and names
    for i, prop in enumerate(base_props):
        # Draw bullet point
        plt.text(
            0.6, prop["pos"], "•", fontsize=20, ha='center',
            fontweight='bold', color='blue'
        )
        # Draw property name
        plt.text(
            0.65, prop["pos"], prop["name"],
            fontsize=18, fontweight='bold'
        )

        # Handle descriptions with special case for Eventually consistent
        if i == 2:  # Eventually consistent
            # Split the text to ensure it fits properly
            lines = textwrap.wrap(prop["desc"], width=40)
            for j, line in enumerate(lines):
                plt.text(
                    0.65, prop["pos"]-0.04-(j*0.04),  # Extra vertical spacing
                    line, fontsize=14
                )
        else:
            plt.text(0.65, prop["pos"]-0.04, prop["desc"], fontsize=14)

    # Key differences - adjusted position
    plt.text(
        0.5, 0.42, "Ključne razlike", fontsize=20,
        fontweight='bold', ha='center'
    )

    differences = [
        {"acid": "Strogi zahtjevi konzistentnosti",
         "base": "Veća tolerancija na privremene nekonzistentnosti",
         "pos": 0.37},
        {"acid": "Manja skalabilnost",
         "base": "Veća skalabilnost",
         "pos": 0.32},
        {"acid": "Fokus na 100% pouzdanost",
         "base": "Fokus na visoku dostupnost",
         "pos": 0.27}
    ]

    for i, diff in enumerate(differences):
        plt.text(0.25, diff["pos"], diff["acid"], fontsize=14, ha='center')
        plt.text(0.75, diff["pos"], diff["base"], fontsize=14, ha='center')

        # Draw arrow between differences
        plt.annotate(
            '', xy=(0.55, diff["pos"]), xytext=(0.45, diff["pos"]),
            arrowprops=dict(arrowstyle='<->', color='gray')
        )

    # Add footer text with better spacing
    plt.figtext(
        0.5, 0.12,
        "CAP teorem: U distribuiranom sustavu možete imati najviše dvije od "
        "tri svojstva:\n"
        "Konzistentnost (C), Dostupnost (A) i Toleranciju particije (P).\n"
        "ACID model prioritizira konzistentnost, dok BASE model prioritizira "
        "dostupnost i toleranciju particije.",
        ha='center', fontsize=13, bbox=dict(facecolor='#f5f5f5', alpha=0.5)
    )

    # Title
    plt.suptitle('ACID vs. BASE model', fontsize=24, fontweight='bold', y=0.98)

    # Save the figure with higher DPI for better quality
    plt.savefig('images/acid-vs-base.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("ACID vs BASE image saved to images/acid-vs-base.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_acid_vs_base_image()