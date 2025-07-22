"""Analysis to determine the number of passengers per day globally."""

import aviation

days_per_year = 365.0
passengers_per_year = 5_000_000_000.0

passengers_per_day = aviation.passengers_per_day(passengers_per_year, days_per_year)
print(f"{passengers_per_day=}")
