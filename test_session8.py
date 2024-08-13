from session8 import generate_profiles_dict, generate_profiles,calculate_statistics, calculate_statistics_dict, Profile, generate_stocks, calculate_market_values, Stock
import session8
from decimal import Decimal
import time
from random import randint, uniform
import os
import inspect
import re

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for enum, space in enumerate(spaces):
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

#Q1
def test_generate_profiles_namedtuple():
    """Test dtypes of Namedtuple Profile"""
    profiles = generate_profiles(5)
    assert len(profiles) == 5
    for profile in profiles:
        assert isinstance(profile, Profile)
        assert isinstance(profile.name, str)
        assert isinstance(profile.age, int)
        assert isinstance(profile.blood_type, str)
        assert isinstance(profile.current_location, Decimal)

def test_calculate_statistics_namedtuple():
    """Test dtypes of Namedtuple Statistics"""
    profiles = generate_profiles(10)
    stats = calculate_statistics(profiles)
    assert isinstance(stats, dict)
    assert 'most_common_blood_type' in stats
    assert 'mean_current_location' in stats
    assert 'oldest_age' in stats
    assert 'average_age' in stats
    assert isinstance(stats['most_common_blood_type'], str)
    assert isinstance(stats['mean_current_location'], float)
    assert isinstance(stats['oldest_age'], int)
    assert isinstance(stats['average_age'], float) 

def test_calculate_oldest_age():
    """Verify that the function correctly identifies the oldest age."""
    profiles = [
        Profile(name='Person1', age=30, blood_type='A', current_location='40.7128'),
        Profile(name='Person2', age=45, blood_type='B', current_location='34.0522'),
        Profile(name='Person3', age=60, blood_type='AB', current_location='37.7749')
    ]
    statistics = calculate_statistics(profiles)
    assert statistics['oldest_age'] == 60

def test_calculate_average_age():
    """Verify the average age calculation is accurate"""
    profiles = [
        Profile(name='Person1', age=20, blood_type='O', current_location='40.7128'),
        Profile(name='Person2', age=30, blood_type='A', current_location='34.0522'),
        Profile(name='Person3', age=40, blood_type='B', current_location='37.7749')
    ]
    statistics = calculate_statistics(profiles)
    assert abs(statistics['average_age'] - (20 + 30 + 40) / 3) < 1e-2

def test_calculate_mean_current_location():
    """Verify the mean current location (latitude) is correctly calculated."""
    profiles = [
        Profile(name='Person1', age=25, blood_type='A', current_location='40.7128'),
        Profile(name='Person2', age=35, blood_type='B', current_location='34.0522'),
        Profile(name='Person3', age=45, blood_type='AB', current_location='37.7749')
    ]
    statistics = calculate_statistics(profiles)
    expected_mean_location = (40.7128 + 34.0522 + 37.7749) / 3
    assert abs(statistics['mean_current_location'] - expected_mean_location) < 1e-4

def test_calculate_largest_blood_type():
    """Verify that the largest blood type (most common) is calculated correctly"""
    profiles = [
        Profile(name='Person1', age=30, blood_type='O', current_location='40.7128'),
        Profile(name='Person2', age=40, blood_type='O', current_location='34.0522'),
        Profile(name='Person3', age=50, blood_type='A', current_location='37.7749'),
        Profile(name='Person4', age=60, blood_type='O', current_location='47.6062')
    ]
    statistics = calculate_statistics(profiles)
    assert statistics['most_common_blood_type'] == 'O'

#Q2
def test_generate_profiles_dict():
    """Test dtypes of Dict Profile"""
    profiles = generate_profiles_dict(5)
    assert len(profiles) == 5
    for profile in profiles:
        assert isinstance(profile, dict)
        assert 'name' in profile
        assert 'age' in profile
        assert 'blood_type' in profile
        assert 'current_location' in profile
        assert isinstance(profile['name'], str)
        assert isinstance(profile['age'], int)
        assert isinstance(profile['blood_type'], str)
        assert isinstance(profile['current_location'], Decimal)


def test_calculate_statistics_dict():
    """Test dtypes of Dict Statistics"""
    profiles = generate_profiles_dict(10)
    stats = calculate_statistics_dict(profiles)
    assert isinstance(stats, dict)
    assert 'most_common_blood_type' in stats
    assert 'mean_current_location' in stats
    assert 'oldest_age' in stats
    assert 'average_age' in stats
    assert isinstance(stats['most_common_blood_type'], str)
    assert isinstance(stats['mean_current_location'], float)
    assert isinstance(stats['oldest_age'], int)
    assert isinstance(stats['average_age'], float)


def test_statistics_calculation_speed():
    """Test the performance speed of namedtuple vs dict"""
    start_time = time.time()
    profiles_namedtuple = generate_profiles(10000)
    stats_namedtuple = calculate_statistics(profiles_namedtuple)
    end_time = time.time()
    namedtuple_duration = end_time - start_time

    start_time = time.time()
    profiles_dict = generate_profiles_dict(10000)
    stats_dict = calculate_statistics_dict(profiles_dict)
    end_time = time.time()
    dict_duration = end_time - start_time
    
    assert namedtuple_duration < dict_duration

def test_calculate_dict_oldest_age():
    """Verify that the function correctly identifies the oldest age."""
    profiles = [
        {"name":'Person1', "age":25, "blood_type":'A', "current_location":'40.7128'},
        {"name":'Person2', "age":35, "blood_type":'B', "current_location":'34.0522'},
        {"name":'Person3', "age":45, "blood_type":'AB', "current_location":'37.7749'}
    ]
    statistics = calculate_statistics_dict(profiles)
    assert statistics['oldest_age'] == 45

def test_calculate_dict_average_age():
    """Verify the average age calculation is accurate"""
    profiles = [
        {"name":'Person1', "age":20, "blood_type":'A', "current_location":'40.7128'},
        {"name":'Person2', "age":30, "blood_type":'B', "current_location":'34.0522'},
        {"name":'Person3', "age":40, "blood_type":'AB', "current_location":'37.7749'}
    ]
    statistics = calculate_statistics_dict(profiles)
    assert abs(statistics['average_age'] - (20 + 30 + 40) / 3) < 1e-2

def test_calculate_dict_mean_current_location():
    """Verify the mean current location (latitude) is correctly calculated."""
    profiles = [
        {"name":'Person1', "age":25, "blood_type":'A', "current_location":'40.7128'},
        {"name":'Person2', "age":35, "blood_type":'B', "current_location":'34.0522'},
        {"name":'Person3', "age":45, "blood_type":'AB', "current_location":'37.7749'}
    ]
    statistics = calculate_statistics_dict(profiles)
    expected_mean_location = (40.7128 + 34.0522 + 37.7749) / 3
    assert abs(statistics['mean_current_location'] - expected_mean_location) < 1e-4

def test_calculate_dict_largest_blood_type():
    """Verify that the largest blood type (most common) is calculated correctly"""
    profiles = [
        {"name":'Person1', "age":25, "blood_type":'O', "current_location":'40.7128'},
        {"name":'Person2', "age":35, "blood_type":'O', "current_location":'34.0522'},
        {"name":'Person3', "age":45, "blood_type":'AB', "current_location":'37.7749'},
        {"name":'Person1', "age":25, "blood_type":'O', "current_location":'40.7128'},
    ]
    statistics = calculate_statistics_dict(profiles)
    assert statistics['most_common_blood_type'] == 'O'

#Q3
def test_generate_stocks_count():
    """Generate a list with a specific number of stocks"""
    num_stocks = 10
    stocks = generate_stocks(num_stocks)
    assert len(stocks) == num_stocks

def test_generate_stocks_attributes():
    """ Verify each stock has the correct attributes"""
    num_stocks = 5
    stocks = generate_stocks(num_stocks)
    for stock in stocks:
        assert isinstance(stock, Stock)
        assert isinstance(stock.name, str)
        assert isinstance(stock.symbol, str)
        assert isinstance(stock.open, float)
        assert isinstance(stock.high, float)
        assert isinstance(stock.close, float)
        assert isinstance(stock.weight, float)

def test_generate_stocks_symbol_format():
    """Check stock symbol format"""
    num_stocks = 5
    stocks = generate_stocks(num_stocks)
    for stock in stocks:
        assert len(stock.symbol) >= 5 

def test_generate_stocks_value_ranges():
    """Check if the values are within the expected ranges"""
    num_stocks = 10
    stocks = generate_stocks(num_stocks)
    for stock in stocks:
        assert 100 <= stock.open <= 500
        assert 500 <= stock.high <= 1000
        assert 200 <= stock.close <= 600
        assert 0.5 <= stock.weight <= 2.0
 
def test_calculate_market_values():
    """Calculate market values with a set of stocks"""
    num_stocks = 5
    stocks = generate_stocks(num_stocks)
    result = calculate_market_values(stocks)
    assert 'start_value' in result
    assert 'high_value' in result
    assert 'end_value' in result
    assert isinstance(result['start_value'], float)
    assert isinstance(result['high_value'], float)
    assert isinstance(result['end_value'], float)

def test_calculate_market_values_positive():
    """Check if the calculated market values are positive"""
    num_stocks = 5
    stocks = generate_stocks(num_stocks)
    result = calculate_market_values(stocks)
    assert result['start_value'] >= 0
    assert result['high_value'] >= 0
    assert result['end_value'] >= 0

def test_calculate_market_values_zero_stocks():
    """Validate market values with zero stocks"""
    result = calculate_market_values([])
    assert result['start_value'] == 0
    assert result['high_value'] == 0
    assert result['end_value'] == 0

def test_calculate_market_values_consistency():
    """Test for consistency in the start, high, and end values"""
    num_stocks = 10
    stocks = generate_stocks(num_stocks)
    result = calculate_market_values(stocks)
    assert result['start_value'] >= 0
    assert result['high_value'] >= result['start_value']
    assert result['end_value'] >= 0

def test_calculate_market_values_weights():
    """Check if weights affect the market values"""
    num_stocks = 10
    stocks = generate_stocks(num_stocks)
    weights_before = [stock.weight for stock in stocks]
    result_before = calculate_market_values(stocks)
    
    # Change weights
    for stock in stocks:
        stock._replace(weight = uniform(0.5, 2.0))
    
    result_after = calculate_market_values(stocks)
    
    assert result_before != result_after

def test_generate_stocks_unique_symbols():
    """Tests that all generated stock symbols are unique."""
    num_stocks = 100
    stocks = generate_stocks(num_stocks)
    symbols = [stock.symbol for stock in stocks]
    assert len(symbols) == len(set(symbols)), "Stock symbols are not unique"