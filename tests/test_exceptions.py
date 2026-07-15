from app.core.exceptions.exceptions import MemoryError

try:
    raise MemoryError("Memory not available")

except MemoryError as e:
    print(e)