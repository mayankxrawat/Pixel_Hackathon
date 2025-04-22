# utils/visualizer.py
import matplotlib.pyplot as plt

def plot_work_hours(faculty_data):
    """Plots a bar chart of work hours by faculty."""
    names = [faculty['name'] for faculty in faculty_data]
    hours = [faculty['total_hours'] for faculty in faculty_data]

    plt.bar(names, hours)
    plt.xlabel("Faculty Members")
    plt.ylabel("Total Work Hours")
    plt.title("Faculty Work Hours")
    plt.xticks(rotation=45)
    plt.show()

def generate_summary_report(faculty_data):
    """Generates a simple report summarizing work hours."""
    summary = "\n".join([f"{faculty['name']}: {faculty['total_hours']} hours" for faculty in faculty_data])
    return summary