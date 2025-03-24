import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import numpy as np
import os


def generate_denormalization_image():
    """
    Generate an image visualizing database denormalization with examples.
    """
    print("Generating denormalization visualization...")

    # Create a figure with grid layout
    fig = plt.figure(figsize=(12, 8))
    gs = gridspec.GridSpec(2, 2, width_ratios=[1, 1], height_ratios=[0.2, 1])

    # Set the background color
    fig.patch.set_facecolor('#f8f9fa')

    # Add a title to the figure
    ax_title = fig.add_subplot(gs[0, :])
    ax_title.set_facecolor('#f8f9fa')
    ax_title.set_xticks([])
    ax_title.set_yticks([])
    ax_title.spines['top'].set_visible(False)
    ax_title.spines['right'].set_visible(False)
    ax_title.spines['bottom'].set_visible(False)
    ax_title.spines['left'].set_visible(False)
    ax_title.set_title('Database Denormalization', fontsize=24, fontweight='bold', pad=10)

    # Normalized tables (left side)
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.set_facecolor('#f8f9fa')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.set_title('Normalized Database Schema', fontsize=18, fontweight='bold')

    # Denormalized tables (right side)
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.set_facecolor('#f8f9fa')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.set_title('Denormalized Database Schema', fontsize=18, fontweight='bold')

    # Draw normalized tables
    # Orders table
    orders_headers = ['order_id', 'customer_id', 'order_date', 'status']
    orders_data = [
        ['1001', '101', '2023-01-15', 'shipped'],
        ['1002', '102', '2023-01-16', 'processing'],
        ['1003', '103', '2023-01-17', 'delivered'],
    ]

    # OrderItems table
    order_items_headers = ['item_id', 'order_id', 'product_id', 'quantity']
    order_items_data = [
        ['5001', '1001', 'P101', '1'],
        ['5002', '1001', 'P102', '2'],
        ['5003', '1002', 'P101', '1'],
        ['5004', '1003', 'P103', '1'],
        ['5005', '1003', 'P104', '2'],
    ]

    # Products table
    products_headers = ['product_id', 'name', 'price', 'category']
    products_data = [
        ['P101', 'Laptop', '$1200', 'Electronics'],
        ['P102', 'Mouse', '$25', 'Electronics'],
        ['P103', 'Keyboard', '$50', 'Electronics'],
        ['P104', 'Monitor', '$300', 'Electronics'],
    ]

    # Customers table
    customers_headers = ['customer_id', 'name', 'email', 'address']
    customers_data = [
        ['101', 'John Smith', 'john@example.com', '123 Main St'],
        ['102', 'Sarah Lee', 'sarah@example.com', '456 Oak Ave'],
        ['103', 'Mike Jones', 'mike@example.com', '789 Pine Rd'],
    ]

    # Draw normalized tables
    normalized_tables = [
        {
            'name': 'Customers',
            'headers': customers_headers,
            'data': customers_data,
            'x': 0.1,
            'y': 0.9,
            'color': '#E8F5E9',
            'header_color': '#43A047'
        },
        {
            'name': 'Orders',
            'headers': orders_headers,
            'data': orders_data,
            'x': 0.6,
            'y': 0.9,
            'color': '#E1F5FE',
            'header_color': '#039BE5'
        },
        {
            'name': 'OrderItems',
            'headers': order_items_headers,
            'data': order_items_data,
            'x': 0.1,
            'y': 0.5,
            'color': '#F3E5F5',
            'header_color': '#8E24AA'
        },
        {
            'name': 'Products',
            'headers': products_headers,
            'data': products_data,
            'x': 0.6,
            'y': 0.5,
            'color': '#FFF3E0',
            'header_color': '#FB8C00'
        },
    ]

    # Draw each normalized table
    for table in normalized_tables:
        draw_table(
            ax1,
            table['name'],
            table['headers'],
            table['data'],
            table['x'],
            table['y'],
            table['color'],
            table['header_color']
        )

    # Draw relationship arrows between normalized tables
    arrow_style = dict(arrowstyle='->', linewidth=1.5, color='#455A64')

    # Orders -> Customers (FK relationship)
    ax1.annotate('',
                xy=(0.1 + 0.35/len(orders_headers), 0.9),
                xytext=(0.6, 0.9 - 0.02),
                arrowprops=arrow_style)

    # OrderItems -> Orders (FK relationship)
    ax1.annotate('',
                xy=(0.1 + 0.35/len(order_items_headers), 0.5),
                xytext=(0.6, 0.9 - 0.1),
                arrowprops=arrow_style)

    # OrderItems -> Products (FK relationship)
    ax1.annotate('',
                xy=(0.6, 0.5 + 0.02),
                xytext=(0.1 + 0.35, 0.5),
                arrowprops=arrow_style)

    # Add example query for normalized schema
    query_text = """
    -- Fetch order details with customer and product info
    SELECT
        o.order_id, o.order_date, c.name,
        p.name, p.price, oi.quantity
    FROM
        Orders o
    JOIN
        Customers c ON o.customer_id = c.customer_id
    JOIN
        OrderItems oi ON o.order_id = oi.order_id
    JOIN
        Products p ON oi.product_id = p.product_id
    WHERE
        o.order_id = 1001;
    """

    # Add query box
    query_box = patches.Rectangle((0.1, 0.1), 0.8, 0.25,
                                 fc='white', ec='black', alpha=0.8)
    ax1.add_patch(query_box)
    ax1.text(0.5, 0.225, query_text, fontsize=8, family='monospace',
            ha='center', va='center')

    # Add normalized benefits & drawbacks
    norm_points = [
        "+ Data integrity & consistency",
        "+ Reduced data redundancy",
        "+ Easier data updates",
        "- Multiple JOINs needed",
        "- Complex queries",
        "- Slower read performance"
    ]

    for i, point in enumerate(norm_points):
        color = "#2E7D32" if point.startswith("+") else "#C62828"
        ax1.text(0.1, 0.08 - 0.03*i, point, fontsize=9, color=color)

    # Now draw denormalized table
    # OrderDetails denormalized table
    order_details_headers = [
        'order_id', 'order_date', 'status', 'customer_id',
        'customer_name', 'customer_email', 'product_id',
        'product_name', 'product_price', 'quantity'
    ]

    order_details_data = [
        ['1001', '2023-01-15', 'shipped', '101', 'John Smith',
         'john@example.com', 'P101', 'Laptop', '$1200', '1'],
        ['1001', '2023-01-15', 'shipped', '101', 'John Smith',
         'john@example.com', 'P102', 'Mouse', '$25', '2'],
        ['1002', '2023-01-16', 'processing', '102', 'Sarah Lee',
         'sarah@example.com', 'P101', 'Laptop', '$1200', '1'],
        ['1003', '2023-01-17', 'delivered', '103', 'Mike Jones',
         'mike@example.com', 'P103', 'Keyboard', '$50', '1'],
        ['1003', '2023-01-17', 'delivered', '103', 'Mike Jones',
         'mike@example.com', 'P104', 'Monitor', '$300', '2'],
    ]

    # Additional denormalized product_categories table for read optimization
    product_categories_headers = [
        'category', 'product_count', 'avg_price', 'total_inventory'
    ]

    product_categories_data = [
        ['Electronics', '4', '$393.75', '120'],
        ['Books', '10', '$24.99', '350'],
        ['Clothing', '15', '$39.99', '500'],
    ]

    # Draw denormalized tables
    denormalized_tables = [
        {
            'name': 'OrderDetails (Denormalized)',
            'headers': order_details_headers,
            'data': order_details_data,
            'x': 0.1,
            'y': 0.8,
            'color': '#EDE7F6',
            'header_color': '#673AB7'
        },
        {
            'name': 'ProductCategories (Aggregated)',
            'headers': product_categories_headers,
            'data': product_categories_data,
            'x': 0.1,
            'y': 0.2,
            'color': '#E0F7FA',
            'header_color': '#00ACC1'
        }
    ]

    # Draw each denormalized table
    for table in denormalized_tables:
        draw_table(
            ax2,
            table['name'],
            table['headers'],
            table['data'],
            table['x'],
            table['y'],
            table['color'],
            table['header_color']
        )

    # Highlight redundancy in denormalized table
    redundancy_marker1 = patches.Rectangle((0.1, 0.8 - 0.05 * 1), 0.8, 0.05,
                                         fc='#FFCDD2', alpha=0.3, ec='none')
    redundancy_marker2 = patches.Rectangle((0.1, 0.8 - 0.05 * 2), 0.8, 0.05,
                                         fc='#FFCDD2', alpha=0.3, ec='none')

    ax2.add_patch(redundancy_marker1)
    ax2.add_patch(redundancy_marker2)

    # Add note about redundancy
    ax2.annotate('Redundant customer data',
                xy=(0.4, 0.8 - 0.05 * 1.5),
                xytext=(0.85, 0.65),
                arrowprops=dict(arrowstyle='->', color='#D32F2F'),
                fontsize=9,
                color='#D32F2F',
                ha='center')

    # Add example query for denormalized schema
    denorm_query_text = """
    -- Fetch order details directly (no JOINs)
    SELECT
        order_id, order_date, customer_name,
        product_name, product_price, quantity
    FROM
        OrderDetails
    WHERE
        order_id = 1001;
    """

    # Add query box
    query_box2 = patches.Rectangle((0.4, 0.35), 0.5, 0.2,
                                  fc='white', ec='black', alpha=0.8)
    ax2.add_patch(query_box2)
    ax2.text(0.65, 0.45, denorm_query_text, fontsize=8, family='monospace',
            ha='center', va='center')

    # Add denormalized benefits & drawbacks
    denorm_points = [
        "+ Faster read performance",
        "+ Simpler queries (fewer JOINs)",
        "+ Better for reporting/analytics",
        "- Data redundancy",
        "- Increased storage needs",
        "- Update anomalies"
    ]

    for i, point in enumerate(denorm_points):
        color = "#2E7D32" if point.startswith("+") else "#C62828"
        ax2.text(0.1, 0.08 - 0.03*i, point, fontsize=9, color=color)

    # Add a big arrow between the normalized and denormalized sections
    fig.text(0.5, 0.5, "→", fontsize=40, ha='center', va='center',
            color='#455A64', weight='bold')

    # Add text explaining when to use denormalization
    when_to_use = """
    When to use denormalization:
    • Read-heavy workloads
    • Reporting and analytics
    • When query performance matters more than storage
    • When data updates are infrequent
    """

    fig.text(0.5, 0.07, when_to_use, fontsize=10, ha='center', va='center',
            bbox=dict(facecolor='#E3F2FD', alpha=0.8, boxstyle='round,pad=0.5'))

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/denormalization.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Denormalization image saved to images/denormalization.png")


def draw_table(ax, name, headers, data, x, y, bg_color, header_color):
    """
    Helper function to draw a database table
    """
    # Calculate dimensions
    if len(headers) <= 5:
        header_height = 0.05
        row_height = 0.04
        cell_width = 0.8 / len(headers)
        t_width = 0.8
    else:
        header_height = 0.05
        row_height = 0.05
        t_width = 0.8
        cell_width = t_width / len(headers)

    num_rows = len(data)
    t_height = header_height + num_rows * row_height

    # Table name
    ax.text(x, y + 0.02, name, ha='left', va='bottom',
            fontsize=10, fontweight='bold')

    # Background
    ax.add_patch(patches.Rectangle((x, y - t_height),
                                 t_width, t_height,
                                 facecolor=bg_color, alpha=0.8,
                                 edgecolor='black', linewidth=1))

    # Headers
    for i, header in enumerate(headers):
        # Header cell
        ax.add_patch(patches.Rectangle((x + i * cell_width, y),
                                     cell_width, -header_height,
                                     facecolor=header_color, alpha=0.8,
                                     edgecolor='black', linewidth=1))
        # Header text
        ax.text(x + i * cell_width + cell_width/2, y - header_height/2,
                header, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white')

    # Data
    for row_idx, row in enumerate(data):
        y_pos = y - header_height - row_idx * row_height
        for col_idx, cell in enumerate(row):
            # Cell
            ax.add_patch(patches.Rectangle(
                (x + col_idx * cell_width, y_pos),
                cell_width, -row_height,
                facecolor='white', alpha=0.8,
                edgecolor='black', linewidth=1))

            # Cell text
            ax.text(x + col_idx * cell_width + cell_width/2,
                   y_pos - row_height/2,
                   cell, ha='center', va='center', fontsize=7)


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Set random seed for reproducibility
    np.random.seed(42)

    generate_denormalization_image()