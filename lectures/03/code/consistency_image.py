import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os


def generate_consistency_image():
    """
    Generate an image visualizing database consistency property.
    """
    print("Generating consistency visualization...")

    # Create figure
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8),
                                        gridspec_kw={'height_ratios': [1, 1, 1]})

    # Common styling
    account_style = {'facecolor': 'lightblue', 'edgecolor': 'blue',
                    'alpha': 0.7, 'boxstyle': 'round,pad=0.5'}

    # Before Transaction (Initial State)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 3)

    # Draw accounts
    account_a1 = patches.FancyBboxPatch((1, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor=account_style['facecolor'],
                                        edgecolor=account_style['edgecolor'],
                                        alpha=account_style['alpha'])
    account_b1 = patches.FancyBboxPatch((6, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor=account_style['facecolor'],
                                        edgecolor=account_style['edgecolor'],
                                        alpha=account_style['alpha'])

    ax1.add_patch(account_a1)
    ax1.add_patch(account_b1)

    # Add text labels
    ax1.text(2.5, 1.5, 'Account A\n€1000', ha='center', va='center', fontsize=12)
    ax1.text(7.5, 1.5, 'Account B\n€500', ha='center', va='center', fontsize=12)
    ax1.text(5, 2.5, 'Before Transaction: Total = €1500', ha='center',
             va='center', fontsize=14, fontweight='bold')

    # During Transaction (Intermediate State)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 3)

    # Draw accounts
    account_a2 = patches.FancyBboxPatch((1, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor='mistyrose',
                                        edgecolor='red',
                                        alpha=account_style['alpha'])
    account_b2 = patches.FancyBboxPatch((6, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor=account_style['facecolor'],
                                        edgecolor=account_style['edgecolor'],
                                        alpha=account_style['alpha'])

    ax2.add_patch(account_a2)
    ax2.add_patch(account_b2)

    # Add text labels
    ax2.text(2.5, 1.5, 'Account A\n€800', ha='center', va='center', fontsize=12)
    ax2.text(7.5, 1.5, 'Account B\n€500', ha='center', va='center', fontsize=12)
    ax2.text(5, 2.5, 'During Transaction: Total = €1300 (Inconsistent!)',
             ha='center', va='center', fontsize=14, fontweight='bold', color='red')

    # Add arrow
    ax2.arrow(3.5, 1.5, 2, 0, head_width=0.2, head_length=0.3, fc='red', ec='red')
    ax2.text(4.5, 1.7, '€200', ha='center', va='center', fontsize=12, color='red')

    # After Transaction (Final State)
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 3)

    # Draw accounts
    account_a3 = patches.FancyBboxPatch((1, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor='lightgreen',
                                        edgecolor='green',
                                        alpha=account_style['alpha'])
    account_b3 = patches.FancyBboxPatch((6, 1), 3, 1, boxstyle=account_style['boxstyle'],
                                        facecolor='lightgreen',
                                        edgecolor='green',
                                        alpha=account_style['alpha'])

    ax3.add_patch(account_a3)
    ax3.add_patch(account_b3)

    # Add text labels
    ax3.text(2.5, 1.5, 'Account A\n€800', ha='center', va='center', fontsize=12)
    ax3.text(7.5, 1.5, 'Account B\n€700', ha='center', va='center', fontsize=12)
    ax3.text(5, 2.5, 'After Transaction: Total = €1500 (Consistent!)',
             ha='center', va='center', fontsize=14, fontweight='bold', color='green')

    # Adjust overall appearance
    for ax in [ax1, ax2, ax3]:
        ax.axis('off')

    # Add overall title
    fig.suptitle('CONSISTENCY: Database Integrity Rules are Preserved',
                 fontsize=16, y=0.98)

    # Add explanation text
    fig.text(0.5, 0.02, 'Transactions must maintain all database rules (e.g., total money is constant).\n'
                        'Intermediate inconsistent states should never be visible to users.',
                         ha='center', fontsize=12, fontweight='bold')

    # Save the figure
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig('images/consistency.png', dpi=200)
    plt.close()

    print("Consistency image saved to images/consistency.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)
    generate_consistency_image()