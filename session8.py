from faker import Faker
from collections import namedtuple
from typing import List, Dict
from statistics import mean, mode
from collections import Counter
import time
import random
from random import randint, uniform

# Initialize Faker
fake = Faker()

# Define the namedtuple for the profile
Profile = namedtuple(
    'Profile', [
        'name', 'age', 'blood_type', 'current_location'])


def generate_profiles(num_profiles: int) -> List[Profile]:
    """Generates a list of fake profiles."""
    profiles = []
    profile = fake.profile()
    for _ in range(num_profiles):
        profile_nt = Profile(
            name=profile['name'],
            age=fake.random_int(min=18, max=100),
            blood_type=profile['blood_group'],
            current_location=fake.latitude()  # Assume latitude for location
        )
        profiles.append(profile_nt)
    return profiles


def generate_profiles_dict(num_profiles: int) -> List[Dict[str, any]]:
    """Generates a list of fake profiles using dictionary."""
    profiles = []
    profile = fake.profile()
    for _ in range(num_profiles):
        profile_dict = fake.profile()
        profile_data = {
            'name': profile['name'],
            'age': fake.random_int(min=18, max=100),
            'blood_type': profile_dict['blood_group'],
            'current_location': fake.latitude()
        }
        profiles.append(profile_data)
    return profiles


def calculate_statistics(profiles: List[Profile]) -> Dict[str, float]:
    """Calculates required statistics from the list of profiles."""
    # Extract data
    ages = [profile.age for profile in profiles]
    blood_types = [profile.blood_type for profile in profiles]
    current_locations = [float(profile.current_location)
                        for profile in profiles]

    # Calculate the largest blood type (most frequent blood type)
    most_common_blood_type = mode(blood_types)

    # Calculate mean current location
    mean_location = mean(current_locations)

    # Calculate the oldest person's age
    oldest_age = max(ages)

    # Calculate average age
    average_age = float(mean(ages))

    return {
        'most_common_blood_type': most_common_blood_type,
        'mean_current_location': mean_location,
        'oldest_age': oldest_age,
        'average_age': average_age
    }


def calculate_statistics_dict(
        profiles: List[Dict[str, any]]) -> Dict[str, float]:
    """Calculates required statistics from the list of dictionaries."""
    ages = [profile['age'] for profile in profiles]
    blood_types = [profile['blood_type'] for profile in profiles]
    current_locations = [float(profile['current_location'])
                        for profile in profiles]

    most_common_blood_type = mode(blood_types)
    mean_location = mean(current_locations)
    oldest_age = max(ages)
    average_age = mean(ages)

    return {
        'most_common_blood_type': most_common_blood_type,
        'mean_current_location': mean_location,
        'oldest_age': oldest_age,
        'average_age': float(average_age)
    }


# Q4
# Define the namedtuple for the stock data
Stock = namedtuple(
    'Stock', [
        'name', 'symbol', 'open', 'high', 'close', 'weight'])


def generate_stocks(num_stocks: int) -> List[Stock]:
    """Generates a list of fake stock data."""
    stocks = []
    for _ in range(num_stocks):
        stock = Stock(
            name=fake.company(),
            symbol=f"{fake.company_suffix().upper()}+{random.randint(1, 100000)}",
            open=uniform(100, 500),
            high=uniform(500, 1000),
            close=uniform(200, 600),
            weight=uniform(0.5, 2.0)  # Random weight for each stock
        )
        stocks.append(stock)
    return stocks


def calculate_market_values(stocks: List[Stock]) -> Dict[str, float]:
    """Calculates the stock market values based on the provided formula."""
    # Calculate stock values
    stock_values_open = [stock.open * stock.weight for stock in stocks]
    stock_values_high = [stock.high * stock.weight for stock in stocks]
    stock_values_close = [stock.close * stock.weight for stock in stocks]
    # Random number to normalize values
    random_weights = [uniform(0.5, 2.0) for _ in stocks]

    # Calculate market values
    total_random_weight = sum(random_weights)
    stock_market_values_open = [
        value *
        random /
        total_random_weight for value,
        random in zip(
            stock_values_open,
            random_weights)]
    stock_market_values_high = [
        value *
        random /
        total_random_weight for value,
        random in zip(
            stock_values_high,
            random_weights)]
    stock_market_values_close = [
        value *
        random /
        total_random_weight for value,
        random in zip(
            stock_values_close,
            random_weights)]

    start_value = sum(
        stock_market_values_open[i] for i,
        stock in enumerate(stocks))
    high_value = sum(
        stock_market_values_high[i] for i,
        stock in enumerate(stocks))
    end_value = sum(
        stock_market_values_close[i] for i,
        stock in enumerate(stocks))
    return {
        'start_value': start_value,
        'high_value': high_value,
        'end_value': end_value
    }
# if __name__ == "__main__":
    # Q1
    # Generate 10,000 profiles
    # profiles = generate_profiles(10000)

    # # Calculate statistics
    # stats = calculate_statistics(profiles)

    # # Print the results
    # print(f"Most common blood type: {stats['most_common_blood_type']}")
    # print(f"Mean current location: {stats['mean_current_location']:.6f}")
    # print(f"Oldest person's age: {stats['oldest_age']}")
    # print(f"Average age: {stats['average_age']:.2f}")

    # # Test cases (generating smaller sets for testing)
    # test_profiles_1 = generate_profiles(5)
    # test_profiles_2 = generate_profiles(10)
    # test_profiles_3 = generate_profiles(50)
    # test_profiles_4 = generate_profiles(100)
    # test_profiles_5 = generate_profiles(500)

    # # Print test results
    # print("\nTest Case Results:")
    # for i, test_profiles in enumerate([test_profiles_1, test_profiles_2, test_profiles_3, test_profiles_4, test_profiles_5], start=1):
    #     stats = calculate_statistics(test_profiles)
    #     print(f"Test case {i}:")
    #     print(f"Most common blood type: {stats['most_common_blood_type']}")
    #     print(f"Mean current location: {stats['mean_current_location']:.6f}")
    #     print(f"Oldest person's age: {stats['oldest_age']}")
    #     print(f"Average age: {stats['average_age']:.2f}\n")

    # Q2
    # start_time = time.time()
    # profiles_namedtuple = generate_profiles(10000)
    # stats_namedtuple = calculate_statistics(profiles_namedtuple)
    # end_time = time.time()
    # namedtuple_duration = end_time - start_time

    # # Benchmarking dictionary
    # start_time = time.time()
    # profiles_dict = generate_profiles_dict(10000)
    # stats_dict = calculate_statistics_dict(profiles_dict)
    # end_time = time.time()
    # dict_duration = end_time - start_time

    # # Print the results
    # print(f"Namedtuple Statistics: {stats_namedtuple}")
    # print(f"Dictionary Statistics: {stats_dict}")
    # print(f"Namedtuple Time: {namedtuple_duration:.4f} seconds")
    # print(f"Dictionary Time: {dict_duration:.4f} seconds")

    # Q4
    # stocks = generate_stocks(100)

    # # Calculate market values
    # market_values = calculate_market_values(stocks)

    # # Print the results
    # print(f"Stock Market Start Value: ${market_values['start_value']:.2f}")
    # print(
    #     f"Stock Market Highest Value During the Day: ${market_values['high_value']:.2f}")
    # print(f"Stock Market End Value: ${market_values['end_value']:.2f}")
