from gallery.evaluator import evaluate_layouts
from gallery.csv_writer import write_scores_csv

def main():
    layouts = evaluate_layouts()
    write_scores_csv(layouts)
    print("Done. Output written to output/scores.csv")

if __name__ == "__main__":
    main()
