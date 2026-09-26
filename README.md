# Smart Travel Planner

A friendly Python console program for estimating the cost of a trip. It asks for
traveler and destination details, group size, trip length, and the main travel
costs, then prints a formatted summary with totals and useful averages.

## Run the program

Use Python 3 to run the program from this folder:

```bash
python smart_travel_planner.py
```

Enter costs in dollars. The program asks for:

- Traveler name and destination
- Number of travelers and travel days
- Transportation cost per traveler
- Hotel cost per day for the group
- Food cost per traveler per day
- Activity cost per traveler for the trip

Food cost is collected separately because the program needs a rate to calculate
the total hotel food cost. The hotel rate is treated as the group's total rate
per day; transportation and activity rates are multiplied by the number of
travelers.

## How the estimate is calculated

- Transportation total = transportation cost per traveler x travelers
- Hotel total = hotel cost per day x travel days
- Hotel food total = food cost per traveler per day x travelers x travel days
- Activity total = activity cost per traveler x travelers
- Overall trip cost = transportation + hotel + food + activities
- Cost per traveler = overall trip cost / travelers
- Average daily cost = overall trip cost / travel days

The program uses separate calculation functions that return their results. A
dictionary keeps the related trip details together. Input helpers check that
names are not blank, counts are positive whole numbers, and costs are valid
non-negative amounts. The implementation uses only Python's built-in features
and does not use classes, databases, APIs, or external libraries.