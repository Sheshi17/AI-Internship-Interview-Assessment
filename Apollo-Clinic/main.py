from simulation import simulate_clinic_operations

from analysis import analyze_results

if __name__ == "__main__":
    results = simulate_clinic_operations(days=7)
    analyze_results(results)
