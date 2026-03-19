import csv
from gallery.models import Layout

def write_scores_csv(layouts):
    with open("output/scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Layout", "Metric", "Score"])
        for layout in layouts:
            for s in layout.scores:
                writer.writerow([layout.name, s.name, s.score])
