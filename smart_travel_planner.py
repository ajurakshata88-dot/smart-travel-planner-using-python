def read_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number greater than zero.")
            continue

        if value > 0:
            return value
        print("The value must be greater than zero.")


def read_non_negative_cost(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid amount, such as 25 or 25.50.")
            continue

        if 0 <= value < float("inf"):
            return value
        print("The amount must be a finite number and cannot be negative.")


def calculate_transportation_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_hotel_cost(cost_per_day, travel_days):
    return cost_per_day * travel_days


def calculate_food_cost(cost_per_traveler_per_day, traveler_count, travel_days):
    return cost_per_traveler_per_day * traveler_count * travel_days


def calculate_activity_cost(cost_per_traveler, traveler_count):
    return cost_per_traveler * traveler_count


def calculate_total_trip_cost(transportation, hotel, food, activities):
    return transportation + hotel + food + activities


def calculate_cost_per_traveler(total_cost, traveler_count):
    return total_cost / traveler_count


def calculate_average_daily_cost(total_cost, travel_days):
    return total_cost / travel_days


def main():
    print("=" * 48)
    print("             SMART TRAVEL PLANNER")
    print("=" * 48)
    print("Enter all costs in dollars.\n")

    trip = {
        "traveler": read_non_empty_text("Traveler name: "),
        "destination": read_non_empty_text("Destination: "),
        "traveler_count": read_positive_integer("Number of travelers: "),
        "travel_days": read_positive_integer("Number of travel days: "),
        "transportation_per_traveler": read_non_negative_cost(
            "Transportation cost per traveler ($): "
        ),
        "hotel_per_day": read_non_negative_cost("Hotel cost per day ($): "),
        "food_per_traveler_per_day": read_non_negative_cost(
            "Food cost per traveler per day ($): "
        ),
        "activities_per_traveler": read_non_negative_cost(
            "Activity cost per traveler ($): "
        ),
    }

    transportation_total = calculate_transportation_cost(
        trip["transportation_per_traveler"], trip["traveler_count"]
    )
    hotel_total = calculate_hotel_cost(trip["hotel_per_day"], trip["travel_days"])
    food_total = calculate_food_cost(
        trip["food_per_traveler_per_day"],
        trip["traveler_count"],
        trip["travel_days"],
    )
    activity_total = calculate_activity_cost(
        trip["activities_per_traveler"], trip["traveler_count"]
    )
    total_cost = calculate_total_trip_cost(
        transportation_total, hotel_total, food_total, activity_total
    )
    cost_per_traveler = calculate_cost_per_traveler(
        total_cost, trip["traveler_count"]
    )
    average_daily_cost = calculate_average_daily_cost(total_cost, trip["travel_days"])

    print("\n" + "=" * 48)
    print("                    TRIP SUMMARY")
    print("=" * 48)
    print(f"Traveler:                 {trip['traveler']}")
    print(f"Destination:              {trip['destination']}")
    print(f"Travelers:                {trip['traveler_count']}")
    print(f"Travel days:              {trip['travel_days']}")
    print("-" * 48)
    print(f"Transportation total:     ${transportation_total:,.2f}")
    print(f"Hotel total:              ${hotel_total:,.2f}")
    print(f"Hotel food total:         ${food_total:,.2f}")
    print(f"Activities total:         ${activity_total:,.2f}")
    print("-" * 48)
    print(f"Overall trip cost:        ${total_cost:,.2f}")
    print(f"Cost per traveler:        ${cost_per_traveler:,.2f}")
    print(f"Average cost per day:     ${average_daily_cost:,.2f}")
    print("=" * 48)


if __name__ == "__main__":
    main()