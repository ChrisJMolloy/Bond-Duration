import seaborn as sns

# Set seaborn style and context
sns.set_theme(
    style="whitegrid",  # Background style ("whitegrid", "darkgrid", "white", "dark", "ticks")
    context="notebook",  # Context for scaling elements ("paper", "notebook", "talk", "poster")
    palette="deep",     # Color palette ("deep", "muted", "bright", "pastel", "dark", "colorblind")
    font="sans-serif",  # Font family
    font_scale=1.1,     # Font scaling relative to context
    rc={
        'figure.figsize': (8, 6),  # Default figure size
        'figure.facecolor': 'white',  # Figure background color
        'axes.grid': True,  # Show grid by default
        'grid.alpha': 0.3,  # Grid transparency
        'axes.edgecolor': '.15',  # Edge color
        'axes.labelpad': 8,  # Padding for axis labels
        'axes.titlepad': 12,  # Padding for title
        'lines.linewidth': 1.75,  # Line width
        'patch.edgecolor': 'black',  # Edge color for patches
        'patch.force_edgecolor': True,  # Always show edges on patches
        'xtick.bottom': True,  # Draw ticks on bottom
        'ytick.left': True,  # Draw ticks on left
    }
)