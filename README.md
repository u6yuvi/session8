
# Q1
Use the Faker Links to an external site. library to get 10000 random profiles. Using namedtuple, calculate the largest blood type, mean-current_location, oldest_person_age, and average age (add proper doc-strings). - 250 (including 5 test cases

## Profile Generation:

generate_profiles(num_profiles) creates a list of Profile namedtuples. Each profile contains a name, age, blood type, and current location (latitude).
The Profile namedtuple provides a structured way to hold this data.
Statistics Calculation:

## calculate_statistics(profiles) computes:
Largest Blood Type: Most frequently occurring blood type.
Mean Current Location: Average of all latitude values (as a proxy for location).
Oldest Age: Maximum age in the profiles.
Average Age: Mean age of all profiles.
Output:

The results are printed out, showing the largest blood type, mean current location, oldest age, and average age.

# Q2
Do the same thing above using a dictionary. Prove that namedtuple is faster

It is the same implementation as above replace Namedtuple with Dictionary to store profiles.

# Q3
Create fake data (you can use Faker for company names) for an imaginary stock exchange for the top 100 companies (name, symbol, open, high, close). Assign a random weight to all the companies. Srock Market Value would be the sum of each_stock_value*random number/(sum of random values) or
 for 100 companies.
Calculate and show what value the stock market started at, what was the highest value during the day, and where did it end. Make sure your open, high, and close are not totally random

## Stock
Stock is a namedtuples, containing:
1. name (str): The name of the company.
2. symbol (str): The stock symbol, consisting of a company suffix and a random number.
3. open (float): The opening price of the stock (between 100 and 500).
4. high (float): The highest price of the stock (between 500 and 1000).
5. lose (float): The closing price of the stock (between 200 and 600).
6. weight (float): A random weight for the stock (between 0.5 and 2.0).

## generate_stocks
The generate_stocks function uses the Faker library to generate random company names and suffixes. Stock prices and weights are also randomly generated within specified ranges. This function is useful for creating mock data for testing and simulations.

## calculate_market_values
The calculate_market_values function computes three key market values:

start_value: The sum of the opening values of all stocks, weighted by a random normalization factor.
high_value: The sum of the highest values of all stocks, similarly weighted.
end_value: The sum of the closing values of all stocks, weighted.
The function prints some intermediate values for debugging purposes and returns a dictionary with the calculated market values.

## Testcases Explanation
test_generate_stocks_count: Ensures the function generates the correct number of stocks.
test_generate_stocks_attributes: Verifies that each stock has the correct attributes and types.
test_generate_stocks_symbol_format: Checks that the stock symbol meets a minimum length requirement.
test_generate_stocks_value_ranges: Ensures that generated values fall within specified ranges.
test_calculate_market_values: Validates that the calculate_market_values function returns the expected keys and types.
test_calculate_market_values_positive: Ensures the market values are non-negative.
test_calculate_market_values_zero_stocks: Tests the function behavior when no stocks are provided.