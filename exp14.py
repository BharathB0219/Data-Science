def calculate_age_frequency(ages):
    age_frequency = {}  
    for age in ages:
        if age in age_frequency:
            age_frequency[age] += 1
        else:
            age_frequency[age] = 1
    return age_frequency
def main():
    customer_ages = [25, 30, 40, 25, 35, 25, 40, 35, 30, 35]
    age_distribution = calculate_age_frequency(customer_ages)
    print("Age\tFrequency")
    for age, frequency in age_distribution.items():
        print(f"{age}\t{frequency}")
if __name__ == "__main__":
    main()
