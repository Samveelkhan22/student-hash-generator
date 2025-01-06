def hash_seat_number(seat_no, table_size):
    """
    Custom hash function for student seat numbers.
    
    Args:
        seat_no (str): Seat number in the format 'B<year><roll_number>' (e.g., B22110004016).
        table_size (int): Size of the hash table (to reduce collisions).

    Returns:
        int: Hash value (index in the hash table).
    """
    # Ensure the seat number starts with 'B'
    if not seat_no.startswith('B'):
        raise ValueError("Invalid seat number format. Must start with 'B'.")
    
    # Extract year and roll number
    year = int(seat_no[1:3])  # Last two digits of the year (e.g., '22' for 2022)
    roll_number = int(seat_no[3:])  # Remaining part is the unique roll number
    
    # Combine the year and roll number
    combined = (year * 100000) + roll_number  # Ensures unique mapping
    
    # Hash it into the range [0, table_size - 1]
    hash_value = combined % table_size
    
    return hash_value


# Example usage:
seat_no = "B22110004016"  # Example seat number
table_size = 1000         # Size of the hash table
hash_index = hash_seat_number(seat_no, table_size)

print(f"Hash value for seat number {seat_no} is: {hash_index}")
