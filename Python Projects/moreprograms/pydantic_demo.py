from pydantic import BaseModel, EmailStr, conint, ValidationError

# Define User model with validation rules
class User(BaseModel):
    name: str
    age: conint(gt=0)  # Age must be greater than 0
    email: EmailStr  # Ensures valid email format

# Valid user data
try:
    user = User(name="Alice", age=25, email="alice@example.com")
    print("Valid User:", user)
except ValidationError as e:
    print(e)

# Invalid user data (age is negative, email is incorrect)
try:
    invalid_user = User(name="Bob", age=-5, email="invalid-email")
except ValidationError as e:
    print("\nValidation Error:\n", e)