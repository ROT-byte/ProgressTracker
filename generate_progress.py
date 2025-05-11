import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import patheffects

# Load progress data
with open("progresscode.json", "r") as f:
    data = json.load(f)

categories = ['Easy', 'Medium', 'Hard']
colors = ['#4CAF50', '#FFC107', '#F44336']
completed = [data[c]['completed'] for c in categories]
totals = [data[c]['total'] for c in categories]

# Calculate percentages
total_completed = sum(completed)
total_questions = sum(totals)
percent_total = round((total_completed / total_questions) * 100)

# Set up figure
fig, ax = plt.subplots(figsize=(8, 6), dpi=100)
ax.axis('equal')
plt.subplots_adjust(left=0.1, right=0.75)  # Make space for labels

# Create concentric rings
radii = [0.92, 0.72, 0.52]
width = 0.16
bg_color = '#E5E5E5'

for i, (comp, total) in enumerate(zip(completed, totals)):
    # Background ring
    ax.pie([1], radius=radii[i], colors=[bg_color], startangle=90,
           wedgeprops=dict(width=width, edgecolor='white', linewidth=0.5, alpha=0.5))
    
    # Progress ring
    if total > 0:
        progress = comp / total
        ax.pie([progress, 1-progress], radius=radii[i], colors=[colors[i], 'none'],
               startangle=90, wedgeprops=dict(width=width, edgecolor='white', linewidth=0.5))

# Centered percentage text
ax.text(0, 0, f"{percent_total}%", ha='center', va='center',
        fontsize=36, fontweight='black', color='black',
        path_effects=[patheffects.withStroke(linewidth=5, foreground='white')])

# Category labels on the right
label_x = 1.0  # X position for labels
label_y_positions = [0.3, 0, -0.3]  # Y positions for Easy/Medium/Hard

for i, (category, color, comp, total) in enumerate(zip(categories, colors, completed, totals)):
    ax.text(label_x, label_y_positions[i], 
           f"{category} - {comp}/{total}",
           fontsize=35, fontweight='bold', color=color,
           ha='left', va='center')

plt.savefig("progresscode.png", transparent=True, bbox_inches='tight', pad_inches=0)
plt.close()
