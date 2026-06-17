def get_numbers_starting_with_one(max_limit: int) -> list[int]:
    results = []
    current_power = 1
    
    while current_power <= max_limit:
        lower_bound = current_power
        upper_bound = min(max_limit, (current_power * 2) - 1)
        results.extend(range(lower_bound, upper_bound + 1))
        current_power *= 10
        
    return results

if __name__ == "__main__":
    try:
        user_input = int(input())
        if user_input >= 1:
            print(get_numbers_starting_with_one(user_input))
    except ValueError:
        pass
