from gallery.models import Layout, ScoreBreakdown

def evaluate_layouts():
    layout = Layout(
        name="ExampleLayout",
        scores=[
            ScoreBreakdown("balance", 0.8),
            ScoreBreakdown("contrast", 0.6)
        ]
    )
    return [layout]
