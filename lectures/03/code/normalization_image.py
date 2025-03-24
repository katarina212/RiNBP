import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.gridspec as gridspec
import numpy as np
import os


def generate_normalization_image():
    """
    Generate an image visualizing database normalization principles.
    """
    print("Generating normalization visualization...")

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
    ax_title.set_title('Database Normalization', fontsize=24, fontweight='bold', pad=10)

    # Non-normalized table
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.set_facecolor('#f8f9fa')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.set_title('Non-Normalized Table', fontsize=18, fontweight='bold')

    # Normalized tables
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.set_facecolor('#f8f9fa')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax2.set_title('Normalized Tables', fontsize=18, fontweight='bold')

    # Create a non-normalized table
    table_x = 0.1
    table_y = 0.8
    table_width = 0.8
    table_height = 0.6

    # Table background
    ax1.add_patch(patches.Rectangle((table_x, table_y - table_height),
                                   table_width, table_height,
                                   facecolor='#E3F2FD', alpha=0.8,
                                   edgecolor='black', linewidth=1))

    # Column headers
    headers = ['Order ID', 'Customer Name', 'Customer Address', 'Product ID',
               'Product Name', 'Product Category', 'Quantity', 'Price']

    header_height = 0.08
    cell_width = table_width / len(headers)

    # Draw header cells
    for i, header in enumerate(headers):
        # Header cell
        ax1.add_patch(patches.Rectangle((table_x + i * cell_width, table_y),
                                       cell_width, -header_height,
                                       facecolor='#1976D2', alpha=0.8,
                                       edgecolor='black', linewidth=1))
        # Header text
        ax1.text(table_x + i * cell_width + cell_width/2, table_y - header_height/2,
                header, ha='center', va='center', fontsize=8,
                fontweight='bold', color='white', wrap=True)

    # Data rows
    data = [
        ['1001', 'John Smith', '123 Main St', 'P101', 'Laptop', 'Electronics', '1', '$1200'],
        ['1001', 'John Smith', '123 Main St', 'P102', 'Mouse', 'Electronics', '2', '$25'],
        ['1002', 'Sarah Lee', '456 Oak Ave', 'P101', 'Laptop', 'Electronics', '1', '$1200'],
        ['1003', 'Mike Jones', '789 Pine Rd', 'P103', 'Keyboard', 'Electronics', '1', '$50'],
        ['1003', 'Mike Jones', '789 Pine Rd', 'P104', 'Monitor', 'Electronics', '2', '$300'],
    ]

    row_height = (table_height - header_height) / len(data)

    # Draw data cells
    for row_idx, row in enumerate(data):
        y_pos = table_y - header_height - row_idx * row_height
        for col_idx, cell in enumerate(row):
            # Cell
            ax1.add_patch(patches.Rectangle(
                (table_x + col_idx * cell_width, y_pos),
                cell_width, -row_height,
                facecolor='white', alpha=0.8,
                edgecolor='black', linewidth=1))

            # Cell text
            ax1.text(table_x + col_idx * cell_width + cell_width/2,
                    y_pos - row_height/2,
                    cell, ha='center', va='center', fontsize=8)

    # Highlight redundancy issues
    redundancy_text = [
        'Redundant Customer Data',
        'Redundant Product Data'
    ]

    # Add arrows pointing to redundant data
    arrow_props = dict(arrowstyle='->', linewidth=2, color='#F44336')
    ax1.annotate(redundancy_text[0],
                xy=(table_x + 1.5 * cell_width, table_y - header_height - 1.5 * row_height),
                xytext=(table_x - 0.05, table_y - header_height - 1.5 * row_height),
                fontsize=10, color='#F44336', fontweight='bold',
                arrowprops=arrow_props, ha='right')

    ax1.annotate(redundancy_text[1],
                xy=(table_x + 5 * cell_width, table_y - header_height - 2.5 * row_height),
                xytext=(table_x + table_width + 0.05, table_y - header_height - 2.5 * row_height),
                fontsize=10, color='#F44336', fontweight='bold',
                arrowprops=arrow_props, ha='left')

    # Draw problems list
    problems = [
        '- Data redundancy',
        '- Update anomalies',
        '- Insert anomalies',
        '- Delete anomalies'
    ]

    for i, problem in enumerate(problems):
        ax1.text(table_x, table_y - table_height - 0.05 - 0.04 * i,
                problem, ha='left', va='top', fontsize=9, color='#D32F2F')

    # Now draw normalized tables

    # Customers table
    customers_headers = ['Customer ID', 'Name', 'Address']
    customers_data = [
        ['C001', 'John Smith', '123 Main St'],
        ['C002', 'Sarah Lee', '456 Oak Ave'],
        ['C003', 'Mike Jones', '789 Pine Rd']
    ]

    # Products table
    products_headers = ['Product ID', 'Name', 'Category', 'Price']
    products_data = [
        ['P101', 'Laptop', 'Electronics', '$1200'],
        ['P102', 'Mouse', 'Electronics', '$25'],
        ['P103', 'Keyboard', 'Electronics', '$50'],
        ['P104', 'Monitor', 'Electronics', '$300']
    ]

    # Orders table
    orders_headers = ['Order ID', 'Customer ID', 'Date']
    orders_data = [
        ['1001', 'C001', '2023-01-15'],
        ['1002', 'C002', '2023-01-16'],
        ['1003', 'C003', '2023-01-17']
    ]

    # Order Items table
    order_items_headers = ['Order ID', 'Product ID', 'Quantity']
    order_items_data = [
        ['1001', 'P101', '1'],
        ['1001', 'P102', '2'],
        ['1002', 'P101', '1'],
        ['1003', 'P103', '1'],
        ['1003', 'P104', '2']
    ]

    # Draw the normalized tables
    tables = [
        {'name': 'Customers', 'headers': customers_headers, 'data': customers_data,
         'x': 0.1, 'y': 0.9, 'color': '#E8F5E9', 'header_color': '#43A047'},
        {'name': 'Products', 'headers': products_headers, 'data': products_data,
         'x': 0.6, 'y': 0.9, 'color': '#FFF3E0', 'header_color': '#FB8C00'},
        {'name': 'Orders', 'headers': orders_headers, 'data': orders_data,
         'x': 0.1, 'y': 0.5, 'color': '#E1F5FE', 'header_color': '#039BE5'},
        {'name': 'Order Items', 'headers': order_items_headers, 'data': order_items_data,
         'x': 0.6, 'y': 0.5, 'color': '#F3E5F5', 'header_color': '#8E24AA'}
    ]

    for table_info in tables:
        name = table_info['name']
        headers = table_info['headers']
        data = table_info['data']
        x = table_info['x']
        y = table_info['y']
        color = table_info['color']
        header_color = table_info['header_color']

        # Calculate dimensions
        t_width = 0.35
        header_height = 0.05
        num_rows = len(data)
        t_height = header_height + num_rows * 0.04
        cell_width = t_width / len(headers)

        # Table name
        ax2.text(x, y + 0.02, name, ha='left', va='bottom',
                fontsize=10, fontweight='bold')

        # Background
        ax2.add_patch(patches.Rectangle((x, y - t_height),
                                       t_width, t_height,
                                       facecolor=color, alpha=0.8,
                                       edgecolor='black', linewidth=1))

        # Headers
        for i, header in enumerate(headers):
            # Header cell
            ax2.add_patch(patches.Rectangle((x + i * cell_width, y),
                                           cell_width, -header_height,
                                           facecolor=header_color, alpha=0.8,
                                           edgecolor='black', linewidth=1))
            # Header text
            ax2.text(x + i * cell_width + cell_width/2, y - header_height/2,
                    header, ha='center', va='center', fontsize=8,
                    fontweight='bold', color='white')

        # Data
        row_height = 0.04
        for row_idx, row in enumerate(data):
            y_pos = y - header_height - row_idx * row_height
            for col_idx, cell in enumerate(row):
                # Cell
                ax2.add_patch(patches.Rectangle(
                    (x + col_idx * cell_width, y_pos),
                    cell_width, -row_height,
                    facecolor='white', alpha=0.8,
                    edgecolor='black', linewidth=1))

                # Cell text
                ax2.text(x + col_idx * cell_width + cell_width/2,
                        y_pos - row_height/2,
                        cell, ha='center', va='center', fontsize=7)

    # Draw relationship arrows between tables
    arrow_style = dict(arrowstyle='->', linewidth=1.5, color='#455A64')

    # Orders -> Customers (FK relationship)
    ax2.annotate('',
                xy=(0.1 + 0.35/len(orders_headers), 0.5),
                xytext=(0.1 + 0.35/len(customers_headers), 0.9 - 0.05 - len(customers_data) * 0.04),
                arrowprops=arrow_style)

    # Order Items -> Orders (FK relationship)
    ax2.annotate('',
                xy=(0.6, 0.5 - 0.02),
                xytext=(0.1 + 0.35, 0.5 - 0.02),
                arrowprops=arrow_style)

    # Order Items -> Products (FK relationship)
    ax2.annotate('',
                xy=(0.6 + 0.35/len(order_items_headers), 0.5),
                xytext=(0.6 + 0.35/len(products_headers), 0.9 - 0.05 - len(products_data) * 0.04),
                arrowprops=arrow_style)

    # Add benefits of normalization
    benefits = [
        '+ Eliminates redundancy',
        '+ Improves data integrity',
        '+ More flexible database design',
        '+ Efficient storage'
    ]

    for i, benefit in enumerate(benefits):
        ax2.text(0.1, 0.1 - 0.04 * i, benefit, ha='left', va='top',
                fontsize=9, color='#2E7D32')

    # Add normalization levels at the bottom
    ax2.text(0.6, 0.1, 'Normal Forms:', ha='left', va='top',
            fontsize=10, fontweight='bold')

    nf_descriptions = [
        '1NF: Atomic values, no repeating groups',
        '2NF: 1NF + No partial dependencies',
        '3NF: 2NF + No transitive dependencies',
        'BCNF/4NF/5NF: Further refinements'
    ]

    for i, desc in enumerate(nf_descriptions):
        ax2.text(0.6, 0.1 - 0.04 * (i+1), desc, ha='left', va='top', fontsize=8)

    # Save the figure
    plt.tight_layout()
    plt.savefig('images/normalization.png', dpi=300, bbox_inches='tight')
    plt.close()

    print("Normalization image saved to images/normalization.png")


if __name__ == "__main__":
    # Create images directory if it doesn't exist
    os.makedirs('images', exist_ok=True)

    # Set random seed for reproducibility
    np.random.seed(42)

    generate_normalization_image()