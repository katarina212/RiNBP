import matplotlib.pyplot as plt
import os


def generate_norm_vs_denorm_image():
    """
    Generate a visualization comparing normalized and denormalized models
    side by side with their respective advantages.
    """
    print("Generating norm-vs-denorm visualization...")

    # Create figure
    plt.figure(figsize=(12, 8))

    # Define the layout with two columns
    gs = plt.GridSpec(3, 2, height_ratios=[1, 3, 1.5])

    # Add title
    plt.suptitle(
        'Usporedba normaliziranog i denormaliziranog pristupa',
        fontsize=18, fontweight='bold', y=0.98
    )

    # Normalized model - top left
    ax1 = plt.subplot(gs[0, 0])
    ax1.set_title('Normalizirani model', fontsize=14, fontweight='bold')
    ax1.axis('off')

    # Denormalized model - top right
    ax2 = plt.subplot(gs[0, 1])
    ax2.set_title('Denormalizirani model', fontsize=14, fontweight='bold')
    ax2.axis('off')

    # Normalized database schema - middle left
    ax3 = plt.subplot(gs[1, 0])
    ax3.axis('off')

    # Draw normalized tables
    tables = [
        {"name": "Users", "y": 0.8,
         "fields": ["user_id (PK)", "name", "email"]},
        {"name": "Posts", "y": 0.5,
         "fields": ["post_id (PK)", "user_id (FK)", "title", "content", "date"]},
        {"name": "Comments", "y": 0.2,
         "fields": ["comment_id (PK)", "post_id (FK)", "user_id (FK)", "text"]}
    ]

    for table in tables:
        # Table rectangle
        rect = plt.Rectangle(
            (0.1, table["y"] - 0.15), 0.8, 0.25,
            facecolor="#a8d1df", alpha=0.8, edgecolor='black'
        )
        ax3.add_patch(rect)

        # Table name
        ax3.text(
            0.5, table["y"] + 0.05, table["name"],
            ha='center', va='center', fontsize=12, fontweight='bold'
        )

        # Fields
        field_text = "\n".join(table["fields"])
        ax3.text(
            0.5, table["y"] - 0.05, field_text, ha='center',
            va='center', fontsize=10
        )

    # Draw relationships with arrows
    ax3.annotate(
        '', xy=(0.5, 0.65), xytext=(0.5, 0.8),
        arrowprops=dict(arrowstyle='->', linewidth=1.5, color='gray')
    )
    ax3.annotate(
        '', xy=(0.5, 0.35), xytext=(0.5, 0.5),
        arrowprops=dict(arrowstyle='->', linewidth=1.5, color='gray')
    )

    # Denormalized database schema - middle right
    ax4 = plt.subplot(gs[1, 1])
    ax4.axis('off')

    # Draw denormalized table
    rect = plt.Rectangle(
        (0.1, 0.2), 0.8, 0.6,
        facecolor="#f8cecc", alpha=0.8, edgecolor='black'
    )
    ax4.add_patch(rect)

    # Table name
    ax4.text(
        0.5, 0.7, "Posts_Denormalized",
        ha='center', va='center', fontsize=12, fontweight='bold'
    )

    # Fields with redundant fields highlighted
    fields = [
        "post_id (PK)",
        "title",
        "content",
        "date",
        "user_id",
        "user_name (redundantno)",
        "user_email (redundantno)",
        "comments: [",
        "  {",
        "    comment_id,",
        "    text,",
        "    user_id,",
        "    user_name (redundantno)",
        "  }",
        "]"
    ]

    field_text = "\n".join(fields)
    ax4.text(0.5, 0.4, field_text, ha='center', va='center', fontsize=9)

    # Advantages and disadvantages - normalized
    ax5 = plt.subplot(gs[2, 0])
    ax5.axis('off')

    norm_adv = [
        "✓ Minimalna redundancija podataka",
        "✓ Jednostavno ažuriranje (jedna lokacija)",
        "✓ Bolja konzistentnost podataka",
        "✓ Efektivnije korištenje prostora",
        "✗ Kompleksni JOIN upiti",
        "✗ Slabije performanse za složene upite"
    ]

    for i, adv in enumerate(norm_adv):
        color = "green" if "✓" in adv else "red"
        ax5.text(0.1, 0.9 - i*0.15, adv, fontsize=10, color=color)

    # Advantages and disadvantages - denormalized
    ax6 = plt.subplot(gs[2, 1])
    ax6.axis('off')

    denorm_adv = [
        "✓ Brže performanse za čitanje",
        "✓ Manje JOIN operacija",
        "✓ Jednostavniji upiti",
        "✓ Brži odgovor za tipične slučajeve",
        "✗ Redundantni podaci",
        "✗ Kompleksnije ažuriranje podataka"
    ]

    for i, adv in enumerate(denorm_adv):
        color = "green" if "✓" in adv else "red"
        ax6.text(0.1, 0.9 - i*0.15, adv, fontsize=10, color=color)

    # Show query examples
    query_norm = ("SELECT p.title, u.name\nFROM Posts p\nJOIN Users u\n"
                  "  ON p.user_id = u.user_id\nWHERE p.post_id = 123;")
    query_denorm = ("SELECT title, user_name\nFROM Posts_Denormalized\n"
                    "WHERE post_id = 123;")

    ax5.text(
        0.5, 0.1, query_norm, fontsize=8,
        bbox=dict(facecolor='#e6f3f7', alpha=0.5, boxstyle='round,pad=0.5')
    )
    ax6.text(
        0.5, 0.1, query_denorm, fontsize=8,
        bbox=dict(facecolor='#fce8e6', alpha=0.5, boxstyle='round,pad=0.5')
    )

    # Add additional annotations
    plt.figtext(
        0.5, 0.05,
        "Odabir između normaliziranog i denormaliziranog modela ovisi o "
        "konkretnom slučaju upotrebe,\n"
        "gdje je bitno razmotriti omjer operacija čitanja i pisanja te "
        "važnost konzistentnosti podataka.",
        ha='center', fontsize=10
    )

    # Save the figure
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/norm-vs-denorm.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Norm-vs-denorm image saved to images/norm-vs-denorm.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_norm_vs_denorm_image()